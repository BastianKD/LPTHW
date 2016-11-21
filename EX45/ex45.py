# To program this game I used Zed Shaw's game from ex43.py and the chatbot.py
# we programed during the seminar as blueprints.


class Room(object):

    def enter(self):
        exit(1)


class Engine(object):

    def __init__(self, room_map):
        self.room_map = room_map

    def start(self):
        current_room = self.room_map.opening_room()
        last_room = self.room_map.next_room('done')

        while current_room != last_room:
            next_room_name = current_room.enter()
            current_room = self.room_map.next_room(next_room_name)

        # print the scene
        current_room.enter()


class Death(Room):

    Goodbye = [
        "You died. Get a life you freak!",
        "If you were a cat, you could continue, but I know you're not. Too bad.",
        "You lose. Sorry for your loss.",
        """RIP
        John/Joan Doe
        XXXX - just now
        Unskilled brother/wife/adult/parent/dog""",
        "Sleep well.",
        "You were drunk anyway amirite?"
    ]

    def enter(self):
        print Death.Goodbye[randint(0, len(self.Goodbye)-1)]
        exit(1)


class Entrance(Room):

    def enter(self):
        print "You just entered an ancient Inca temple searching for the "
        print "treasure of Wiraqucha the 8th Sapa Inca."
        print "Since you're not the only one looking for the treasure: beware!"
        print "Find the treasure before anyone else does and make sure you "
        print "haven't been seen or followed by anyone. \nGood luck!"
        print "\n"
        print "You're now in a long corridor leading to the unknown."
        print "You hear some voices in the distance. What do you do?"
        print "You can either try to 'hide', enter the 'tunnel' you've seen "
        print "or 'continue' to walk down the corridor."

        action = raw_input("\t> ")

        if action == "hide":
            print "You found a place to hide. Well played. Don't move until "
            print "the voices are gone."
            print "..."
            print "Woaw you're hiding for so long. You're thirsty."
            print "Wanna drink something?"

            drink = raw_input("\t> ")

            if drink == "yes":
                print "Unfortunately, they heard you opening your backpack."
                print "They decided to kill you since bad guys don't like "
                print "to compete..."
                return 'death'

            elif drink == "no":
                print "Unfortunately, you died of thirst!"
                return 'death'

            else:
                print "Try again."
                return 'entrance'

        elif action == "tunnel":
            return 'tunnel'

        elif action == "continue":
            print "The people in front of you have noticed you. You can either "
            print "go to them to 'say hi' or 'run'!"

            nextmove = raw_input("\t> ")

            if nextmove == "say hi":
                print "These people weren't so happy to see you and killed you "
                print "because they had guns and you didn't."
                return 'death'

            elif nextmove == "run":
                print "As you run the ground collapses under your feet, "
                print "the bad guys didn't follow you but you fell in an "
                print "underground river."
                return 'river'

            else:
                "Get your shit together mate..."
                return 'entrance'

        else:
            print "What was that?"
            return 'entrance'


class SecretTunnel(Room):

    def enter(self):
        print "The tunnel seems to be safe but apparently it leads not to "
        print "the inside of the temple but outside..."
        print "At the end of the tunnel there is a cave with an "
        print "underground river. You can 'follow the river' or 'go back' "
        print "to where you came from."

        whatdoyoudo = raw_input("\t> ")

        if whatdoyoudo == "go back":
            return 'entrance'

        elif whatdoyoudo == "follow the river":
            return 'river'

        else:
            print "I beg your pardon?"
            return 'tunnel'


class UndergroundRiver(Room):

    def enter(self):
        print "You let yourself drift in the cold water. You can see a light "
        print "in the distance and on there are some rocks which lead to a "
        print "hole in the wall. You have to choose whether you want to 'stay "
        print "in the water' to be carried to the light or if you want "
        print "to 'climb the rocks' you see on the side."

        act = raw_input("\t> ")

        if act == "stay in the water":
            print "The stream takes you to the light but you realize that it "
            print "is taking you outside."
            print "Since the water is very cold, you may die before "
            print "reaching the outside of the cave and you can't get out of "
            print "the water now because the current is too strong."

            life = "%d" % (randint(1,2))

            if life == "1":
                print "You survived! You have failed your mission, but "
                print "you're still alive."
                return 'outside'
            elif life == "2":
                print "Unfortunately you died because the water was too cold."
                return 'death'

        elif act == "climb the rocks":
            print "You have managed to get out of the water."
            print "Soon enough you realize, that the hole in the leads to the "
            print "treasure. Well done!"
            return 'treasure'


class Outside(Room):

    def enter(self):
        print "You're out of the temple and alive. Do you want to try again?"

        anothertry = raw_input("\t> ")

        if anothertry == "yes":
            print "Let's do it again!"
            return 'entrance'

        elif anothertry == "no":
            print "Too bad. See you later!"
            exit(1)


class TreasureRoom(Room):

    def enter(self):
        print "You made it, you found the treasure! Contact a Museum and you'll"
        print "get a reward!"
        return 'done'


class Done(Room):

    def enter(self):
        print "You did it! Nice job dude!"
        return 'done'


class Map(object):

    rooms = {
        'entrance': Entrance(),
        'tunnel': SecretTunnel(),
        'river': UndergroundRiver(),
        'outside': Outside(),
        'treasure': TreasureRoom(),
        'death': Death(),
        'done': Done(),
    }

    def __init__(self, starting_room):
        self.starting_room = starting_room

    def next_room(self, room_name):
        nex = Map.rooms.get(room_name)
        return nex

    def opening_room(self):
        return self.next_room(self.starting_room)


# run the game
from sys import exit
from random import randint
the_map = Map('entrance')
the_game = Engine(the_map)
the_game.start()
