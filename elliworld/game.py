from tkinter import RIGHT
import pyxel
from enum import Enum

class Direction(Enum):
    IDLE = 4
    UP = 0
    DOWN = 2
    LEFT = 3
    RIGHT = 1

class Player:

    x=60
    y=60
    direction=Direction.IDLE
    offsetx=0
    offsety=0
    speed=2

class Game:
    player=Player()
    def __init__(self) -> None:
        pyxel.init(160,120,"Mecha 8")
        pyxel.load("elli.pyxres")
        pyxel.playm(0,loop=True)
        pyxel.run(self.update,self.draw)
        self.player=Player()

    def update_player(self):
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.player.direction=Direction.RIGHT
            self.player.x = self.player.x + self.player.speed
            self.player.offsetx=self.player.offsetx+1
        else:
            if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
                self.player.direction=Direction.LEFT
                self.player.x = self.player.x - self.player.speed
                if self.player.offsetx>0:
                    self.player.offsetx=self.player.offsetx-1

            else:
                if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
                    self.player.direction=Direction.UP
                    self.player.y=self.player.y - self.player.speed
                    if self.player.offsety>0:
                        self.player.offsety = self.player.offsety-1
                else:
                    if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
                        self.player.direction=Direction.DOWN
                        self.player.y=self.player.y+self.player.speed
                        self.player.offsety = self.player.offsety+1
                    else:
                        self.player.direction=Direction.IDLE
    
    def update(self):
        self.update_player()
        
    def draw(self):
        pyxel.cls(7)
        pyxel.camera()
        pyxel.bltm(0,0,0,self.player.offsetx,self.player.offsety,300,300,12)
        pyxel.blt(self.player.x,
        self.player.y,
        0,
        (pyxel.frame_count%3)*32,
         self.player.direction.value*32,
        32,32,
        8
        )

Game()