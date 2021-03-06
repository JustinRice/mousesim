from mouse import Mouse

class Simulation:
    def setUp(self, data):
        self.mice = []
        self.totalTime = 0
        for mouse in data.keys():
            newMouse = Mouse(mouse)
            newMouse.setUp(data[mouse])
            self.mice.append(newMouse)

    def updateAll(self, time):
        for mouse in self.mice:
            mouse.update(time)
        self.keepTime(time)

    def getAllPaths(self):
        paths = {}
        for mouse in self.mice:
            paths[mouse.idNum] = mouse.getPath()
        return paths

    def getAllHeatData(self):
        data = {}
        for mouse in self.mice:
            data[mouse.idNum] = mouse.getHeatData()
        return data

    def isDone(self):
        for mouse in self.mice:
            if (not mouse.isDone()):
                return False
        return True

    def keepTime(self, time):
        if (not self.isDone()):
            self.totalTime += time

    def oneStep(self, time):
        while not self.isDone():
            self.updateAll(time)

    def getTotalTime(self):
        return self.totalTime
