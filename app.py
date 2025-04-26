from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///triggers.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#Database logic
class Incident(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    description = db.Column(db.Text, nullable = False)
    severity = db.Column(db.String(10), nullable = False)
    reported_time = db.Column(db.DateTime, default = datetime.utcnow)

    def to_dict(self):
        return{
            "id" : self.id,
            "title" : self.title,
            "description" : self.description,
            "severity" : self.severity,
            "reported_time" : self.reported_time.isoformat()
        }


#Centralized error handling
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error" : "Bad request",  "details" : str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error" : "Not found", "details" : str(error)}), 404

@app.errorhandler(IntegrityError)
def integrity_error(error):
    db.session.rollback()
    return jsonify({"error" : "Integrity Error", "details" : str(error)}), 400

@app.errorhandler(SQLAlchemyError)
def sqlalchemy_error(error):
    db.session.rollback()
    return jsonify({"error" : "SQLAlchemy Error i.e database error", "details" : str(error)}), 500

@app.errorhandler(Exception)
def exception_error(error):
    return jsonify({"error" : "Unexpected error", "details" : str(error)}), 500


#Defining routes
@app.route("/")
def test():
    return 'Welcome!!'

@app.route('/health', methods=['GET'])
def health_check():
    db.session.execute(text('SELECT 1'))
    return jsonify({"Status" : "Healthy"}), 200


@app.route('/triggers', methods=['GET'])
def get_all_trigger():
    trigger=Incident.query.all()
    result=[i.to_dict() for i in trigger]
    return jsonify(result), 200

@app.route('/triggers/<int:id>',methods=['GET'])
def get_trigger(id):
    trigger=Incident.query.get_or_404(id)
    return jsonify(trigger.to_dict()), 200

@app.route('/triggers',methods=['POST'])
def add_trigger():
    data = request.get_json()

    if not data:
        abort(400, description = "Invalid JSON")
    
    title = data.get("title")
    description = data.get("description")
    severity = data.get("severity")
    
    missing_input = [input for input in["title","description","severity"] if not data.get(input)]
    if(missing_input):
        abort(400, description = f"missing inputs: {', '.join(missing_input)}")
    
    valid_severity = ["Low", "Medium", "High", "low", "medium", "high"]
    if severity not in valid_severity:
        abort(400, description = f"severity is valid only if it one of the among: {', '.join(valid_severity)}")

    new_trigger = Incident(title=title, description=description, severity=severity)
    db.session.add(new_trigger)
    db.session.commit()

    return jsonify(new_trigger.to_dict()), 201

@app.route('/triggers/<int:id>',methods=['DELETE'])
def delete_trigger(id):
    trigger=Incident.query.get_or_404(id)
    db.session.delete(trigger)
    db.session.commit()
    return 'Successfully Deleted', 204

#Main function
if __name__ == ("__main__"):
    try:
        with app.app_context():
            db.create_all()

            if not Incident.query.first():
                sample_trigger = [
                    Incident(
                        title = "AI chatbot malfunction",
                        description = "giving abusive responses",
                        severity = "High"
                    ),
                    Incident(
                        title = "Image classifier bias",
                        description = "classified labelled person inaccurately",
                        severity = "Medium"
                    ),
                    Incident(
                        title = "wrong output",
                        description = "Giving irrelevant answers",
                        severity = "Low"
                    )
                ]
                db.session.add_all(sample_trigger)
                db.session.commit()
    except SQLAlchemyError as e:
        print("Error intializing the database:", e)
    app.run(debug=True)