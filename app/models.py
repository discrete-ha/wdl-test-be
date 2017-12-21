from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
import os

db = SQLAlchemy()

class Account(db.Model):
	__tablename__ = 'account'
	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True)

	def serialize(self):
		return {
			'user_id': self.user_id, 
			'username': self.username
		}
