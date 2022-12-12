#!/usr/bin/env python
from flask import Flask,request,render_template
import requests
import requests.auth
import urllib

import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID') # Get your client ID set in .env file
CLIENT_SECRET = os.getenv('CLIENT_SECRET') # Get your client secret set in .env file
REDIRECT_URI = os.getenv('REDIRECT_URI')
PORT = os.getenv('PORT')


app = Flask(__name__)
@app.route('/')
def homepage():
    authURL = make_authorization_url()

    
    return render_template('index.html', authURL=authURL)


def make_authorization_url():
    # Generate a random string for the state parameter
    # Save it for use later to prevent xsrf attacks
    
    params = {"client_id": CLIENT_ID,
              "response_type": "code",
              "redirect_uri": REDIRECT_URI}
    url = "https://zoom.us/oauth/authorize?" + urllib.parse.urlencode(params)
    return url



@app.route('/zoom_callback')
def zoom_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    
    code = request.args.get('code')
    access_token = get_token(code)
    # Note: In most cases, you'll want to store the access token, in, say,
    # a session for use in other parts of your web app.
    userData= get_userdata(access_token)
    
    return render_template('userData.html', userData=userData)

def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "authorization_code",
                 "code": code,
                 "redirect_uri": REDIRECT_URI}

    response = requests.post("https://zoom.us/oauth/token",
                             auth=client_auth,
                             data=post_data)
    token_json = response.json()
    
    return token_json["access_token"]
    
    
def get_userdata(access_token):
    
    headers= {"Authorization": "bearer " + access_token}
    response = requests.get("https://api.zoom.us/v2/users/me", headers=headers)
    me_json = response.json()
    return me_json


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
