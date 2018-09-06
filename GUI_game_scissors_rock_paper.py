# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 17:27:36 2018

@author: Ya-Ting Chuang

gif website: http://gifmaker.me/
"""

import pyglet
import random
from pyglet.window import key

# 設定窗口的大小
window = pyglet.window.Window(800, 500)
# set screen bg = white
pyglet.gl.glClearColor(255,255,255,255)
# 如果需要展示的GIF图未在工作目录下，这里需要先指明目标文件夹
#pyglet.resource.path = ['/img']
# animation中需要填入的是目标文件的文件名
animation = pyglet.resource.animation("img/Webp.net-gifmaker.gif")
animation1 = pyglet.resource.animation("img/Webp.net-gifmaker_1.gif")
you_scissors_img = pyglet.resource.image("img/you_scissors.PNG")
you_paper_img = pyglet.resource.image("img/you_paper.PNG")
you_rock_img = pyglet.resource.image("img/you_rock.PNG")
rival_scissors_img = pyglet.resource.image("img/rival_scissors.PNG")
rival_paper_img = pyglet.resource.image("img/rival_paper.PNG")
rival_rock_img = pyglet.resource.image("img/rival_rock.PNG")
player_select_img = pyglet.resource.image("img/player_select.png")

sprite = pyglet.sprite.Sprite(animation, x=10, y=170)
sprite1 = pyglet.sprite.Sprite(animation1, x=400, y=170)

class Game(object):
    def __init__(self):
        self.score = 0
        self.gameover = False
        self.player1_select = 0
        self.c_choice=random.randint(0,2)+1
        self.w_l=""

game = Game()

score_label = pyglet.text.Label(str(game.score),
                                #x=250,
                                x=window.width//2,
                                y=440,
                                anchor_x='center',
                                font_name='Arial',
                                font_size=22,
                                color=(0, 0, 255, 255))


def judge_win_lose(choice, c_choice):
  if choice==2:
    if c_choice==2:
      game.w_l="你出剪刀,對手出剪刀,平分秋色"
    elif c_choice==3:
      game.w_l="你出剪刀,對手出石頭,你輸了"
    elif c_choice==1:
      game.w_l="你出剪刀,對手出布,你贏了"
  elif choice==3:
    if c_choice==2:
      game.w_l="你出石頭,對手出剪刀,你贏了"
    elif c_choice==3:
      game.w_l="你出石頭,對手出石頭,平分秋色"
    elif c_choice==1:
      game.w_l="你出石頭,對手出布,你輸了"
  elif choice==1:
    if c_choice==2:
      game.w_l="你出布,對手出剪刀,你輸了"
    elif c_choice==3:
      game.w_l="你出布,對手出石頭,你贏了"
    elif c_choice==1:
      game.w_l="你出布,對手出布,平分秋色"
  return game.w_l



@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP: # replay
        game.player1_select=0
        #print('UP')
        game.c_choice=random.randint(0,2)+1
        #print('c_choice:' + str(game.c_choice))
    
    elif symbol == key.RIGHT and game.player1_select==0: # paper
        game.player1_select=1
        game.w_l=judge_win_lose(game.player1_select,game.c_choice)
        #print(w_l)
    
    elif symbol == key.LEFT and game.player1_select==0: # scissors
        game.player1_select=2
        game.w_l=judge_win_lose(game.player1_select,game.c_choice)
        #print(w_l)
    
    elif symbol == key.DOWN and game.player1_select==0: # rock
        game.player1_select=3
        game.w_l=judge_win_lose(game.player1_select,game.c_choice)
        #print(w_l)
    
    
        


@window.event
def on_draw():
    if not game.gameover:
        window.clear()
        
        player_select_img.blit(210,5)
                        
        if game.player1_select == 0:
            sprite.draw()
            sprite1.draw()
            

        elif game.player1_select == 2:
            you_scissors_img.blit(10,150)
            
            if game.c_choice == 2:
                rival_scissors_img.blit(400,165)
                
            elif game.c_choice == 1:
                rival_paper_img.blit(400,170)
                
            elif game.c_choice == 3:
                rival_rock_img.blit(400,165)
            #print(game.w_l)
            
        elif game.player1_select == 1:
            you_paper_img.blit(10,170)
            
            if game.c_choice == 2:
                rival_scissors_img.blit(400,165)
                
            elif game.c_choice == 1:
                rival_paper_img.blit(400,170)
                
            elif game.c_choice == 3:
                rival_rock_img.blit(400,165)
            #print(game.w_l)
            
        elif game.player1_select == 3:
            you_rock_img.blit(10,170)
            
            if game.c_choice == 2:
                rival_scissors_img.blit(400,165)
                
            elif game.c_choice == 1:
                rival_paper_img.blit(400,170)
                
            elif game.c_choice == 3:
                rival_rock_img.blit(400,165)
            #print(game.w_l)
            
        score_label.text = str(game.w_l)
        score_label.draw()
        

pyglet.app.run()
