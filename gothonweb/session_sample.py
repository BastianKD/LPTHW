from flask import Flask, session

app = Flask(__name__)

@app.route('/count')
def count():
    if 'count' in session:
        session['count'] += 1
    else:

        session['count'] = 0
    return """
    <html>
    <head><title>Counting...</tile><head>
    <body>
    Count %d
    </body>
    <html>
    """ % session['count']

@app.route('/reset')
def reset():
    session.pop('count') # remove'count' from the session
    return "Your session was reset."

app.secret_key = 'replace this with your secret key' # used by Flask to encrypt the session id

if __name__ == "__main__":
    app.run()
