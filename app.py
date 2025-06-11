from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='new')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    incidents = Incident.query.all()
    return render_template('index.html', incidents=incidents)

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    new_incident = Incident(title=data['title'], description=data['description'])
    db.session.add(new_incident)
    db.session.commit()
    return jsonify({'success': True})

@app.route('/resolve/<int:id>', methods=['POST'])
def resolve(id):
    incident = Incident.query.get(id)
    if incident:
        incident.status = 'resolved'
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
