

class Mouse:
    def __init__(self, idNum):
        self.moveIndex = 0
        self.timeCounter = 0
        self.idNum = idNum
        self.done = False
        self.path = []

    def setUp(self, data):
        self.data = data

    def getLocation(self):
        return self.data[self.moveIndex]["location"]

    def advance(self, time):
        if ((self.moveIndex + 1) >= len(self.data)):
            self.done = True
        else:
            remainder = (self.timeCounter + time) - int(self.data[self.moveIndex]["duration"])
            self.path.append(self.getLocation())
            self.timeCounter = remainder
            self.moveIndex += 1
            print("Mouse " + self.idNum + " moved to location " + self.getLocation())
            if(remainder > int(self.data[self.moveIndex]["duration"])):
                self.timeCounter = 0
                self.advance(remainder)
            else:
                self.timeCounter = remainder

    def update(self, time):
        if (self.done):
            print("Mouse " + self.idNum + " is done moving.")
            print("Mouse " + self.idNum + " is in location " + self.getLocation())
        else:
            if (self.timeCounter + time > int(self.data[self.moveIndex]["duration"])):
                self.advance(time)
            else:
                self.timeCounter += time
                print("Mouse " + self.idNum + " did not move.")
                print("Mouse " + self.idNum + " is in location " + self.getLocation())

    def getPath(self):
        return self.path
