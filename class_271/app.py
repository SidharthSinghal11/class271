from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant


app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/token')
def generate_token():
    #add your twilio credentials 
    TWILIO_ACCOUNT_SID='AC4682f21112eae096047a6d02be8c2db3'
    TWILIO_SYNC_SERVICE_SID='IS6d4445bddbd13ea280526ea23781fe6b'
    TWILIO_API_KEY='SKdaab7d24e63e0ed11615d902497780ab'
    TWILIO_API_SECRET='Yvk0LgnmAgYSxDkzeDd8kglme5Zm9uKq'

    username = request.args.get('username', fake.user_name())
    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)
    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt().decode())



if __name__ == "__main__":
    app.run(port=5001)

