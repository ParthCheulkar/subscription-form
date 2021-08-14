from flask import Flask, url_for, request, redirect, jsonify, after_this_request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
ma = Marshmallow()

class Susbscribe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    subscribed = db.Column(db.Integer, default=1)

    def __repr__(self) -> str:
        return '<Task %r>' % self.id

class SubscriptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Susbscribe
        load_instance = True


@app.route('/')
def hello():
    return 'Hello'

@app.route('/post', methods=['POST'])
def index():
    #if user submits
    if request.method == 'POST':
        print(request.data)
        content = json.loads(request.data)
        _email = content['subs']
        new_entry = Susbscribe(email=_email)
        try:
            db.session.add(new_entry)
            db.session.commit()
            # return redirect('/')
            return "Success"
        except:
            return "Error!!"
        
    else:
        return "hello World"

@app.route('/get_subscriptions', methods=['GET'])
def get_subs():

    if request.method == 'GET':
        sub_queries = Susbscribe.query.all()
        sub_schema = SubscriptionSchema(many=True)
        subs = sub_schema.dump(sub_queries)
        print(subs)
        return jsonify({'subs': subs})

if __name__ == "__main__":
    app.run(debug = True)