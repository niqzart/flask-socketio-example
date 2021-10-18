# Flask SocketIO Example

### Why?
I haven't found a good described example for that. Ones I found are either too old and use old versions of used libraries (which is not ideal) or don't work because of a version compatibility issue(s). I managed to make it work, but it did take a few hours. 

*I hope this example will help someone to not waste the same amount of time.*

### What does it do?
It's a python web server that serves an HTML page with a chat-like interface. You can send messages, which are processed by flask-soketio and broadcasted to everyone connected to the main page.

The example is hosted on heroku, you can visit it and try it out for yourself [here](https://flask-socketio-example.herokuapp.com/). Open up two tabs with it and chat!

### A bit on how I will try to make this example future-proof
1. All requirements are marked as exact versions, so version compatibility shouldn't become a problem
2. I'm still working on an app with flask-socketio, this repo will be updated from time to time (last update date == last commit date)
3. If some links go dead, I'll replace them, you can report such links in issues

### What should be redone for production environment?
CORS policy. Currently it's allowing any origins, that should never be a thing in a production environment. See `flask-socketio` documentation for info on [CORS configuration](https://flask-socketio.readthedocs.io/en/latest/deployment.html#cross-origin-controls)

### Hot to run it locally?
1. Clone the repo
2. Create a virtual python environment (https://docs.python.org/3/library/venv.html)
3. Open a console & activate the virtual environment
4. Install requirements: `pip install -r requirements.txt`
5. Run the main file: `python main.py`
6. Done! Web server should be running at `http://localhost:5000/`

### How to deploy this to heroku?
1. Clone the repo
2. Open a console in repo's folder
3. Create an application on heroku
4. Login to heroku CLI: `heroku login`
5. Attach your heroku app as a git remote: `heroku git:remote -a your-app-name-here`
6. Push it to heroku: `git push heroku master`
7. Wait for it to deploy, when visit your applications page, and you're done!

### Links

- Why an older version of eventlet is used:
    - https://stackoverflow.com/questions/67409452/gunicorn-importerror-cannot-import-name-already-handled-from-eventlet-wsgi

- Deployment of flask-socketio applications:
    - https://flask-socketio.readthedocs.io/en/latest/deployment.html

- Client configuration:
    - https://socket.io/docs/v4/client-installation/#standalone-build

