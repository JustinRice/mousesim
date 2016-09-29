

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

    def advance(self):
        if ((self.moveIndex + 1) >= len(self.data)):
            self.done = True
            self.path.append(self.getLocation())
            self.timeCounter = 0
        else:
            remainder = self.timeCounter - int(self.data[self.moveIndex]["duration"])
            self.path.append(self.getLocation())
            self.moveIndex += 1
            self.timeCounter = remainder
            print("Mouse " + self.idNum + " moved to location " + self.getLocation())

    def update(self, time):
        if (self.done):
            print("Mouse " + self.idNum + " is done moving.")
            print("Mouse " + self.idNum + " is in location " + self.getLocation())
        else:
            self.timeCounter += time
            if (self.timeCounter < int(self.data[self.moveIndex]["duration"])):
                print("Mouse " + self.idNum + " did not move.")
                print("Mouse " + self.idNum + " is in location " + self.getLocation())
            while (self.timeCounter >= int(self.data[self.moveIndex]["duration"])):
                self.advance()

    def getPath(self):
        return self.path
