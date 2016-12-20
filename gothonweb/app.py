# The first step is to import Flask and some classes and objects to work with.
from flask import Flask, session, request
from flask import url_for, redirect, render_template
# We also need map because app.py is our engine and it's basically running map.py.
import map

# Here an instance of a Flask class is created.
# Flask needs it to know where to look for templates, static and test files.
app = Flask(__name__)

# Then we use the 'route()' decorator to tell Flask what URL should trigger the function.
# We give it a name used to generate the URL for the function and an HTTP method.
# The method basically tells the server what the client wants to do with the requested page.
# With methods=['GET'] we (the browser in fact) tell the server tho get the information stored
# on that page and send it
@app.route('/game', methods=['GET'])
def game_get():
    # That's a condition: if we have 'scene' in session (session is a tool that makes it
    # possible to remember information from one request to another) the template showscene
    # should be returned. If there's no 'scene' in the session, the template you_died
    # should be returned.
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        # The user doesn't have a session...
        # What should your code do in response?
        return render_template('you_died.html')

# Here we use the 'route()' decorator once more (also to tell Flask what URL should
# trigger the function), only this time the method is different.
# The 'POST' method tells the server that it wants to post some new information to that URL
# and that the server should check that the data is properly stored. This method is the
# way HTML forms usualy transmit data to the server.
@app.route('/game', methods=['POST'])

# Here we define a function 'game_post'.
# In this function we'll call userinput what we get from the form.
def game_post():
    userinput = request.form.get('userinput')
    # Here we have another, it's very similar to th previous one: if we have 'scene'
    # in session but no user input, the template you_died is returned.
    if 'scene' in session:
        if userinput is None:
            # Weird, a POST request o /game with no user input... what should your code do?
            return render_template('you_died.html')
        # Here the variable 'currentscene' and 'nextscene' are created: currentscene is
        # the scene you are in in map.py if you have 'scene' in session; and 'nextscene'
        # is the scene you go to when you have your userinput.
        # If you have no nextscene then the template you_died is returned, if you have
        # 'scene' in session then the template show_scene is returned.
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                # There's no transition for that user input.
                # What should your code do in response?
                return render_template('you_died.html')
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    # If 'scene' is not in session than the template you_died is returned.
    else:
        # There's no session, how could the user get here?
        # What should your code do in response?
        return render_template('you_died.html')

# This URL initializes the session with starting values.
# The route() decorator again but this time without a method.
# We define a new function 'index' in which is written that 'scene' is in session,
# the urlname which is in START which is in map, should be used.
# The . (dot) notation enable us to tell an instance of a class to use one of the
# methods or function inside that class.
@app.route('/')
def index():
    session['scene'] = map.START.urlname
    # We want to redirect the browser to the url for game_get.
    return redirect(url_for('game_get'))

# The secret key has to be set to use sessions.
# Sessions allows you to store information from a user from one request to the next.
# To do this, sessions uses cookies, but to protect the information in the cookie they're
# signed cryptographically, someone can look at the content of a cookie but not modify it
# unless he has the secret key which is used for signing. So here the secrey key is set.
app.secret_key = 'replace this with your secret key'

# Here the app is run only if it is run as a script (not as a module), so the file
# should be run directly and not imported.
if __name__=="__main__":
    app.run()
