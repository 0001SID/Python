class Song(object):
    def __init__(self,lyric):
        self.lyric = lyric
        print(self.lyric)
    def sing_me_a_song(self):
       #print(self.lyric)
        for line in self.lyric:
            print(line)
happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])
test = Song('This is a test lien')
test.sing_me_a_song()

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()