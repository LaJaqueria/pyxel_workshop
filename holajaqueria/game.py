import pyxel


class App:
    colour=1
    def __init__(self) -> None:
         pyxel.init(160, 120, title="Hello Jaqueria")
         pyxel.run(self.update,self.draw)
         self.colour=1
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.colour=self.colour+1
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.colour=self.colour-1
            if self.colour< 0:
                self.colour=15
    def draw(self):
        pyxel.text(50,50,"Hello Jaqueria",col=self.colour % 16)
App()