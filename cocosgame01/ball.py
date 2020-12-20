# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:04:55 2020

@author: Roy
"""

import cocos
from pyglet.window import key
from collections import defaultdict


class MainLayer(cocos.layer.Layer):
    is_event_handler = True
    
    
    def init(self):
        super(MainLayer, self).__init__()
        self.player = cocos.sprite.Sprite('ball.png')
        self.player.color = (0,0,255)
        self.player.position = (320,240)
        self.add(self.player)
        self.speed = 100.00
        self.pressed = defaultdict(int)
        self.schedule(self.update)
        
        
    def on_key_press(self, k, m):
        print('pressed', key.symbol_string(k))
        self.pressed[k] = 1
        
    def on_key_release(self, k, m):
        print("Released", key.symbol_string(k))
        self.pressed[k] = 0
        
    def update(self, dt):
        x = self.pressed[key.RIGHT] - self.pressed[key.LEFT]
        y = self.pressed[key.UP] - self.pressed[key.DOWN]
        if x != 0 or y != 0:
            pos = self.player.position
            new_x = pos[0] + self.speed *x *dt
            new_y = pos[1] + self.seppd *y *dt
            self.player.pposition = (new_x,new_y)
            
class Actor(cocos.sprite.Sprite):
    def __init__(self, x, y, color):
        
        
        
        
if __name__ == "__main__":
    cocos.director.director.init(caption = "Ball Game for Hello Cocos")
    layer = MainLayer()
    scene = cocos.scene.Scene(layer)
    cocos.director.director.run(scene)
        