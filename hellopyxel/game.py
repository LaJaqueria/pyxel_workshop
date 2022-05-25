
import pyxel

class Game:
    def __init__(self) -> None:
        pyxel.init(160,120,"Hello Pyxel")
        pyxel.run(self.update,self.draw)

    def update(self):
        pass
    def draw(self):
        pyxel.rect(20,20,20,10,3)

Game()

