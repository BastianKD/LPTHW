# I enhanced the tests so that they'd test more of the game, there are still
#some issues I couldn't fix though, but te game runs fine!

from nose.tools import *
from map import *

def test_room():
    central_corridor = Scene("Central Corridor", "central_corridor",
    """
    The Gothons of Planet 'Percal Y25.K04' have returned!
    They invaded your ship and destroyed your entire crew in retaliation for
    your last encounter with them...
    """)
    assert_equal(central_corridor.title, "Central Corridor")
    assert_equal(central_corridor.urlname, central_corridor)

def test_gothongame_map():
    assert_equal(START.go('shoot'), generic_death)
    assert_equal(START.go('dodge'), generic_death)
    room = START.go('tell me a joke')
    assert_equal(room, laser_weapon_armory)

    assert_equal(START.go('help'), help_system)
    assert_equal(START.go('*'), generic_death)
    room = START.go('824')
    assert_equal(room, the_bridge)

    assert_equal(START.go('throw the bomb'), generic_death)
    assert_equal(START.go('shoot them'), the_bridge)
    assert_equal(START.go('tell your joke'), the_bridge)
    assert_equal(START.go('make fun of them'), the_bridge)
    room = START.go('place the bomb carefully')
    assert_equal(room, escape_pod)

    assert_equal(START.go('*'), the_end_loser)
    room = START.go('2', '4')
    assert_equal(room, the_end_winner)

    assert_equal(START.go('pod'), escape_pod)
    assert_equal(START.go('corridor'), central_corridor)
    assert_equal(START.go('bridge'), the_bridge)
    assert_equal(START.go('armory'), laser_weapon_armory)
    room = START.go('escape')
    assert_equal(room, central_corridor)
