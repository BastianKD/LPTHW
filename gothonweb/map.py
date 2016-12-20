class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction= self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)


# Create the scenes of the game

choose_your_game = Scene("Choose Your Game", "choose_your_game",
"""
Welcome Stranger,
You can choose whether you want to try to solve some riddles, or if you want to
save the world, it's up to you really. Have fun!

Type in 'gothon' if you want to go on an adventure in space or type in 'riddles' if you like to think.

""")

riddle_one = Scene("Riddle #1", "riddle_one",
"""
You will always find me in the past. I can be created in the present, but the
future can never taint me. What am I?

""")

riddle_two = Scene("Riddle #2", "riddle_two",
"""
The man who made it doesn't want it. The man who bought it doesn't need it.
The man who needs it doesn't know it. What am I?

""")

riddle_three = Scene("Riddle #3", "riddle_three",
"""
What can run, but never walks? Has a mouth, but never talks? Has a head,
but never weeps? Has a bed, but never sleeps?

""")

central_corridor = Scene("Central Corridor", "central_corridor",
"""
The Gothons of Planet 'Percal Y25.K04' have returned!
They invaded your ship and destroyed your entire crew in retaliation for
your last encounter with them...
Once again, you are the last surviving member and your last mission (for real
this time!) is to get the neutron-laser-destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an escape pod.

You're running down the central corridor to the Weapons Armory when
a cosplay fanatic Gothon dressed as the Joker but filled with even more hate,
jumps out. He's blocking the door to the Armory and about to pull his weapon
to blast you (type 'help' if you need any)!

The different actions available to you are: 'shoot', 'dodge' or 'tell a joke'!

""")

laser_weapon_armory = Scene("Laser Weapon Armory", "laser_weapon_armory",
"""
Lucky for you, since the Gothons don't speak english (they ate the colons that
were sent to 'Percal Y25.K04' to teach them english), they made you learn
Gothon in the academy. Even though it wasn't really your sthrength, you know one
joke:
Dnauq sed sneg et tnesid uq'sli tneroda l'ruedo sed servil, j'ia sruojuot eivne
ed rednamed: ut sias tnemmoc eril enniotcnof?
The Gothon (who - lucky you - can read) bursts into laughter and rolls around
on the ground. While its laughing you run up and use your copy of Nietzche's
notebooks (translated into Gothon) to lecture the Gothon on the shaky
foundations of its ideologies. While it tries to cope with its existential
crisis, you leap through the Weapon Armory door.
You dive roll into the Weapon Armory, crouch and scan the room for more Gothons
that might be hiding. It's dead quiet, too quiet!
You stand up and run to the far side of the room and find the neutron bomb in
its container. There's a keyboard lock on the box and you need the code to get
the bomb out. If you get the code wrong the alarm is triggered and Gothons will
come and kill you! The code has 3 digits (remember you can get 'help').

You have to find the right combination, it's composed of 3 digits.
Here's a little clue: the first digit in binary is IOOO, the 2nd digit is equal
to the number of possible positions a switch can have and the third digit is
the 2nd squared.

""")

the_bridge = Scene("The Bridge", "the_bridge",
"""
The container clicks open and the seal breaks, letting gas out. You grab the
neutron bomb and run like heck to the bridge where you place it in the
right spot.
You burst into the bridge with the bomb under your arm and surprise 5 Gothons
who are trying to take control of the ship. Each of them has an uglier clown
costume than the last. They don't pull their weapons out of fear that they will
set off the bomb under your arm. You give them your best evil laugh and...

You can either: 'throw the bomb', 'place the bomb carefully', 'shoot them', 'tell your joke'
or 'make fun of them'.

""")

escape_pod = Scene("Escape Pod", "escape_pod",
"""
You gesture towards the bomb and threaten to set it off, the Gothons put up
their arms and ask for a truce. You inch backwards to the door, open it, and
carefully place the bomb on the floor, waving your finger over the detonate
button, thereby rejecting their offer for a truce. Then you jump back through
the door, hit the close button and zap the lock so they can't get out.
Now that the bomb is placed you run to the escape pod.
You rush through the ship desperately trying to make it to the escape pod. It
seems like there's no Gothons around, so you run as fast as possible.
Eventually you reach the room with the escape pods, you now need to pick one to
take. Some of them could be damaged, but you don't have time to look. There's 5
pods, which one will you take?

You have to pick a number between 1-5 to choose the Escape Pod you want to escape with.

""")

the_end_winner = Scene("You Made It!", "the_end_winner",
"""
You jump into the pod and hit the eject button. The pod flies out into space
heading to the planet below - which is not inhabited by Gothons but by Zorgs.
As you're heading down, you look back and see your ship implode and then explode
like a badass supernova, taking down the Gothon ship at the same time.
You made it! You can finally retire.

""")

the_end_loser = Scene ("...", "the_end_loser",
"""
You jump into a random pod and hit the eject button. The pod escapes into space
but you notice the crack in the hull. Uh oh. Before you can do anything, the pod
implodes and you with it. You died... painlessly, but still.

""")

generic_death = Scene("Death...", "death",
"""
You died. It seems like he Gothons have won...
No hard feelings right?
Say hello to your crew when you'll see them!

""")

help_system = Scene("Help", "help_system",
"""
You asked for Help! Here it is...

RIDDLES
Think harder! All the answers are in minuscule and it's never more than two words.

CENTRAL CORRIDOR
The different actions available to you are: 'shoot', 'dodge' or 'tell a joke'!

LASER WEAPON ARMORY
You have to find the right combination, it's composed of 3 digits.
Here's a little clue: the first digit in binary is IOOO, the 2nd digit is equal
to the number of possible positions a switch can have and the third digit is
the 2nd squared.

BRIDGE
You can either: 'throw the bomb', 'place the bomb carefully', 'shoot them', 'tell your joke'
or 'make fun of them'.

ESCAPE POD
You have to pick a number between 1-5 to choose the Escape Pod you want to escape with.

To resume the game and go to your level type:
'rid1' to go to the first riddle,
'rid2' to go to the second riddle,
'rid3' to go to the third riddle,
'pod' to go the Escape Pod,
'bridge' to go to The Bridge,
'armory'  to go to the Laser Weapon Armory,
and 'corridor'  to go to the Central Corridor.

Fun fact: you might want to learn french and think backwards to understand Gothon!

""")


# Define the action commands available in each Scene

help_system.add_paths({
    'help': help_system,
    'rid1': riddle_one,
    'rid2': riddle_two,
    'rid3': riddle_three,
    'pod': escape_pod,
    'bridge': the_bridge,
    'armory': laser_weapon_armory,
    'corridor': central_corridor,
    'escape': choose_your_game
})

the_end_winner.add_paths({
    'help' : help_system,
    'escape' : choose_your_game
})

the_end_loser.add_paths({
    'help' : help_system,
    'escape' : choose_your_game
})

escape_pod.add_paths({
    '2': the_end_winner,
    '4': the_end_winner,
    'help': help_system,
    '*': the_end_loser,
    'escape' : choose_your_game
})

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'place the bomb carefully': escape_pod,
    'help': help_system,
    'shoot them': the_bridge,
    'tell your joke': the_bridge,
    'make fun of them': the_bridge,
    'escape' : choose_your_game
})

laser_weapon_armory.add_paths({
    '824': the_bridge,
    'help': help_system,
    '*': generic_death,
    'escape' : choose_your_game
})

central_corridor.add_paths({
    'shoot': generic_death,
    'dodge': generic_death,
    'tell a joke': laser_weapon_armory,
    'help': help_system,
    'escape' : choose_your_game
})

riddle_three.add_paths({
    'a river': choose_your_game,
    'help': help_system,
    'escape' : choose_your_game
})

riddle_two.add_paths({
    'a coffin': riddle_three,
    'help': help_system,
    'escape' : choose_your_game
})

riddle_one.add_paths({
    'history': riddle_two,
    'help': help_system,
    'escape' : choose_your_game
})

choose_your_game.add_paths({
    'gothon': central_corridor,
    'riddles': riddle_one,
    'help' : help_system
})


# Make some useful variables to be used in the web application
SCENES = {
    choose_your_game.urlname : choose_your_game,
    riddle_one.urlname : riddle_one,
    riddle_two.urlname : riddle_two,
    riddle_three.urlname : riddle_three,
    central_corridor.urlname : central_corridor,
    laser_weapon_armory.urlname : laser_weapon_armory,
    the_bridge.urlname : the_bridge,
    escape_pod.urlname : escape_pod,
    the_end_winner.urlname : the_end_winner,
    the_end_loser.urlname : the_end_loser,
    generic_death.urlname : generic_death,
    the_end_loser.urlname : the_end_loser,
    the_end_winner.urlname : the_end_winner,
    help_system.urlname: help_system
}

START = choose_your_game
