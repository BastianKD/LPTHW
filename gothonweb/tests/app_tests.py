# I enhanced the tests so that they'd test more of the game, there are still
#some issues I couldn't fix though, but te game runs fine!

from nose.tools import *
from app import app
from tests.tools import assert_response

client = app.test_client() # create a testing client (like a fake web browser)
client.testing = True # enable this so that errors in your web app bubble up to the test client

def test_index():
    global client # let python know you want to use the global client variable in this function
    resp = client.get('/') # with this client you can do all kind of stuff
    assert_response(resp, status=302) # the root url should give back a redirect

    resp = client.get('/game')
    assert_response(resp) # just make sure you got a valid response

    resp = client.post('/game') # use POST but provide no data
    assert_response(resp, contains="You Died!")

    resp = client.post('/game') # use POST but provide no data
    assert_response(resp, contains="Play Again?")

    # Go to another scene in the game
    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Laser Weapon Armory")

    # Go to another scene in the game
    testdata = {'userinput': 'help'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Help")

    # Go to another scene in the game
    testdata = {'userinput': 'dodge', 'shoot': 'throw the bomb'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="You Died!")
