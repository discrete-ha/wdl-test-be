from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import Account
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

@app.route('/')
def home():
	return jsonify({'message':"hi"})

@app.route('/user/all')
def getUserAll():
	try:
		accounts = Account.query.all()
		return jsonify( users=[ a.serialize() for a in accounts ] )
	except Exception as e:
		print(e)
		return jsonify({"error": e})

@app.route('/user/<int:user_id>')
def getUser(user_id):
	try:
		user = Account.query.get(user_id)
		return jsonify(user.serialize())
	except Exception as e:
		print(e)
		return jsonify({"error": e})

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))