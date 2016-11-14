from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud... if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed "
        print "your entire crew. You are the last surviving member and your last "
        print "mission is to get the neutron destruct bomb from the Weapons Armory, "
        print "put it in the bridge, and blow the shipup after getting into an "
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when "
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume "
        print "flowing around his hate filled body. He's blocking the door to the "
        print "Armory and about to pull a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out the blaster and fire it at the Gothon. "
            print "His clown costume is flowing and moving around his body, which throws "
            print "off your aim. Your laser hits his costume but misses him entirely. That "
            print "completely ruins his brand new costume his mother bought him, which "
            print "makes him fly into an insane rage and blast you repeatedly in the face. "
            print "Now you are dead and he eats you."
            return 'Death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right "
            print "as the Gothons blaster cranks a laser past your head. "
            print "In the middle of your awful dodge your foot slips and you "
            print "bang your head on the metal wall and pass out. "
            print "You wake up shortly after only to die as the Gothon stomps on "
            print "your head and eats you."
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy. "
            print "You tell the one Gothon joke you know: "
            print "Lbhe iuh auhd iejd ahdku diuehao ahifhi oaoid nebhaq iuhd. "
            print "The Gothon stops, tries no to laugh, then busts out laughing and can't fire. "
            print "While he's laughing you run up and shoot him square in the head "
            print "putting him down, then jump through the Weapon Armory door."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room "
        print "for Gothons. It's quiet. Too quiet."
        print "You search for the neutron bomb and find it in its container but there's "
        print "a keypad lock on the box and you need to find the code to get the bomb "
        print "If you get the code wrong 10 times then the lock closes forever and "
        print "you can't get the bomb. The code is 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != cod and guesses < 10:
            print "BZZZZZZEDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'

        else:
            print "The lock buzzes one last time and then you hear a sickening "
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, finally the Gothons blow up the"
            print "shipt from there ship and you die."
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print "You burst onto the birdge with the neutron bomb under your arm"
        print "but 5 Gothons are tryong to take control of the ship."
        print "They haven't pulled their weapons out yet as they see the"
        print "active bomb under your arm and don't want to set it off."

        action = raw_input("> ")

        if action == "throw the bomb":
            print "Panicked, you throw the bomb at the Gothons, but as soon"
            print "as you turn away to run, one of them shoots you in the back"
            print "You die knowing that you'll see them in hell when the bomb"
            print "goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it and then carefully"
            print "place the bomb on the floor, still pointing your blaster at"
            print "it. You then jump back through the door, punch the close"
            print "button and blast the lock so the Gothons can't get out."
            print "Now that the bomb is place you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'

        else:
            print "DOES NOT COMPUTE!"
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print "You rush through the ship desperately trying to make it to the"
        print "escape pod before the whole ship explodes. It seems like hardly"
        print "any Gothons are on the ship."
        print "You get to the escape pod chamber and pick one. Some of them"
        print "could be damaged but you don't have time to check. There are 5"
        print "pods, which one do you take?"
        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "As you hit the eject button, the pod explodes."
            print "You die."
            return 'death'

        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to the planet"
            print "below. As it flies to the planet you see your ship explode"
            print "killing all the Gothons."
            print "You won!"
            return 'finished'


class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
