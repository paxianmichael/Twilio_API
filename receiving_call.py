#receiving phone call
"""
ngrok http 3000 set up before executing the code
"""

from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    resp = VoiceResponse()

    resp.say("Hello world!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)