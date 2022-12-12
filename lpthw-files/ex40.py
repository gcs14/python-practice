class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


kanye_stronger = Song(["N-n-now that that don't kill me",
                        "Can only make me stronger",
                        "I need you to hurry up now",
                        "'Cause I can't wait much longer"])

print("\n")
kanye_stronger.sing_me_a_song()
