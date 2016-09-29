from mouse import Mouse

class Simulation:
    def setUp(self, data):
        self.mice = []
        for mouse in data.keys():
            newMouse = Mouse(mouse)
            newMouse.setUp(data[mouse])
            self.mice.append(newMouse)

    def updateAll(self, time):
        for mouse in self.mice:
            mouse.update(time)

    def getAllPaths(self):
        paths = {}
        for mouse in self.mice:
            paths[mouse.idNum] = mouse.getPath()
        return paths
