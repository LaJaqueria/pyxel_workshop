
import pyxel

DIRECTION_RIGTH=96
DIRECTIONY_RIGTH=0
DIRECTION_LEFT=0
DIRECTIONY_LEFT=32
IDLE=96
DIRECTIONY_IDLE=64
speed=3

class Game:
    playerx=60
    playery=80
    direction=IDLE;
    directiony=DIRECTIONY_IDLE
    def __init__(self) -> None:
        pyxel.init(160, 120, title="Retro vara")
        pyxel.load("varaman.pyxres")
        pyxel.run(self.update,self.draw)
    def update(self) -> None:
        if pyxel.btn(pyxel.KEY_ESCAPE):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.playerx<136:
                self.playerx=self.playerx+speed
            self.direction=DIRECTION_RIGTH
            self.directiony=DIRECTIONY_RIGTH
        else:
            if pyxel.btn(pyxel.KEY_LEFT):
                if self.playerx>-8:
                    self.playerx=self.playerx-speed
                self.direction=DIRECTION_LEFT
                self.directiony=DIRECTIONY_LEFT
            else:
                self.direction=IDLE
                self.directiony=DIRECTIONY_IDLE
    def draw(self) -> None:
        pyxel.blt(self.playerx,self.playery,0,self.direction+32*(pyxel.frame_count%3),self.directiony,32,32,12)

Game()