class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets fill of shells"])

let_it_be = Song(["When I find myself in times of trouble",
                  "Mother Mary comes to me",
                  "Speking words of wisdom",
                  "Let it be"])

times_changing = Song(["Come gather 'round people wherever you roam",
                       "And admit that the waters around us have grown"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

let_it_be.sing_me_a_song()

times_changing.sing_me_a_song()
