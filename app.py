#!/usr/bin/env python
from flask import Flask, abort, request,render_template
from uuid import uuid4
import requests
import requests.auth
import urllib
CLIENT_ID = "Your Client ID" # Fill this in with your client ID
CLIENT_SECRET = "Your Client Secret" # Fill this in with your client secret
REDIRECT_URI = "http://localhost:65010/zoom_callback"



app = Flask(__name__)
@app.route('/')
def homepage():
    text = '<a href="%s">Authenticate with Zoom</a>' % make_authorization_url()

    
    return text


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
    return "Your user info is: %s" % get_username(access_token)

def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "authorization_code",
                 "code": code,
                 "redirect_uri": REDIRECT_URI}

    response = requests.post("https://zoom.us/oauth/token",
                             auth=client_auth,
                             data=post_data)
    token_json = response.json()
    print(token_json)
    return token_json["access_token"]
    
    
def get_username(access_token):
    
    headers= {"Authorization": "bearer " + access_token}
    response = requests.get("https://api.zoom.us/v2/users/me", headers=headers)
    me_json = response.json()
    return me_json


if __name__ == '__main__':
    app.run(debug=True, port=65010)
