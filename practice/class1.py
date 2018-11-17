class mystuff(object):
    def __init__(self,data):
        self.data = data
    def good(self,last):
        print(last)
        for j in last:
            print("This is the first line")
        for i in self.data:
            print("i am a good boy")
thing = mystuff('this is in the last data')
thing.good('jk')