# To run the app: 

$ python3 oAuth_app.py 

$ flask run -h localhost -p 65010

Creating a virtual environment
$ python3 -m venv env

Activating a virtual environment & deactivate

$ source env/bin/activate
$ deactivate

# Install 
$ pip3 install requests
$ pip3 install flask  

Sign to your account

First, create a new folder in the project directory called templates. This naming is important. Now create a new file in the templates folder naming “index.html”. Then insert the below code in the file.

Run the command pip install -r requirements.txt to install all the packages required in your virtual environment.

```bash
pip install -r requirements.txt
```

Run python main.py this will run the program.

You can create a style.css style sheet file to add CSS to your application. First, create a directory called static inside your main flask_oauth directory:

```
mkdir static

```

Then create another directory called css inside the static directory to host .css files.

```
mkdir static/css

```

Then create and open a style.css file inside the css directory for editing:

```
touch style.css 

```

Add the following CSS rule to your style.css file. Save and close the file.

```
@import url('https://fonts.googleapis.com/css?family=Open+Sans:400,600&display=swap');@import url('https://necolas.github.io/normalize.css/8.0.1/normalize.css');html {color: #232333;font-family: 'Open Sans', Helvetica, Arial, sans-serif;-webkit-font-smoothing: antialiased;-moz-osx-font-smoothing: grayscale;}h2 {font-weight: 700;font-size: 24px;}h4 {font-weight: 600;font-size: 14px;}.container {margin: 24px auto;padding: 16px;max-width: 720px;}.info {display: flex;align-items: center;}.info>div>span, .info>div>p {font-weight: 400;font-size: 13px;color: #747487;line-height: 16px;}.info>div>span::before {content: "👋";}.info>div>h2 {padding: 8px 0 6px;margin: 0;}.info>div>p {padding: 0;margin: 0;}.info>img {background: #747487;height: 96px;width: 96px;border-radius: 31.68px;overflow: hidden;margin: 0 20px 0 0;}.response {margin: 32px 0;display: flex;flex-wrap: wrap;align-items: center;justify-content: space-between;}.response>a {text-decoration: none;color: #2D8CFF;font-size: 14px;}.response>pre {overflow-x: scroll;background: #f6f7f9;padding: 1.2em 1.4em;border-radius: 10.56px;width: 100%;box-sizing: border-box;}


```

Next, open the index.html template file for editing:

```html
. . .
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{{ url_for('static', filename= 'css/style.css') }}">
    <title>FlaskBlog</title>
</head>
. . .

```

Here you use the url_for() helper function to generate the appropriate location of the file. The first argument specifies that you’re linking to a static file and the second argument is the path of the file inside the static directory.

Save and close the file.