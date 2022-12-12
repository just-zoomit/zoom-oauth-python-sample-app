# About

Sample Zoom Oauth App using FLASK Web Server to call Zoom's APIs


Use of this sample app is subject to our [Terms of Use](https://zoom.us/docs/en-us/zoom_api_license_and_tou.html)

This is a Hello World app using an OAuth Marketplace App client ID and Secret to create an OAuth token, used to call the Zoom API.

Follow allong with relevant Zoom OAuth documentation as we set this up:

OAuth with Zoom
Create an OAuth App
Get Started Instructions: 

# Setup app locally

First, if virtualenv not installed, run following commands to install and create virtual environment.

```bash
$ pip install  virtualenv
$ python3 -m venv env
```
Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH.

```bash
$ source env/bin/activate
```

Run the command pip install -r requirements.txt to install all the packages required in your virtual environment.

```bash
pip install -r requirements.txt
```

### Setup dotenv 
Create a `.env` file in which to store your PORT, access credentials, and Redirect URL.

```bash
touch .env
```

Copy the following into this file, which we'll add your own values to:

```
CLIENT_ID = "Fill this in with your client ID" 
CLIENT_SECRET = "Fill this in with your client secret" 
REDIRECT_URI = "Fill this in with your redirect URI" 
```

> Remember: Never share or store your client credentials publicly. Your `.env` is included in the `.gitignore` file to ensure these files won't be included in a git workflow.


## Run server
To run the appilcation, run the following command : 

```bash
$ python3 OAuth2.py
or 
$ flask run -h localhost -p 4000
```
## Next steps 

Follow our documentation on OAuth with Zoom for more information on building a user-level app on the Zoom App Marketplace. 

Code happy!

## Need help?

If you're looking for help, try [Developer Support](https://devsupport.zoom.us) or our [Developer Forum](https://devforum.zoom.us). Priority support is also available with [Premier Developer Support](https://zoom.us/docs/en-us/developer-support-plans.html) plans.




