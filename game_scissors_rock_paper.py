# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 2018

@author: Ya-Ting Chuang

practice for python
"""

import random
import tkinter as tk

def judge_win_lose(choice, c_choice):
  w_l=""
  if choice==0:
    if c_choice==0:
      w_l="你出剪刀,對手出剪刀,平分秋色"
    elif c_choice==1:
      w_l="你出剪刀,對手出石頭,你輸了"
    elif c_choice==2:
      w_l="你出剪刀,對手出布,你贏了"
  elif choice==1:
    if c_choice==0:
      w_l="你出石頭,對手出剪刀,你贏了"
    elif c_choice==1:
      w_l="你出石頭,對手出石頭,平分秋色"
    elif c_choice==2:
      w_l="你出石頭,對手出布,你輸了"
  elif choice==2:
    if c_choice==0:
      w_l="你出布,對手出剪刀,你輸了"
    elif c_choice==1:
      w_l="你出布,對手出石頭,你贏了"
    elif c_choice==2:
      w_l="你出布,對手出布,平分秋色"
  print(w_l)
  
# window setting
window=tk.Tk()
window.wm_attributes('-topmost',1)
window.title('Welcome to the game!')
window.geometry('900x450')

# image setting
canvas=tk.Canvas(window,height=400, width=500)
#you_rock_image_file=tk.PhotoImage(file='./img/you_rock.PNG')
you_rock_image_file=tk.PhotoImage(file='./img/ezgif.com-optimize.gif')
you_rock_img = tk.Label(window,image=you_rock_image_file)



you_rock_img.pack(padx=10,pady=0,side='left')

window.mainloop()



command=0
while command<1:
  command=int(input("是否開始對戰?  0.開始對戰  1.走為上策"))

  if command==0:
    choice=int(input("請問你要出 0.剪刀  1.石頭  2.布"))
    c_choice=random.randint(0,2)
    judge_win_lose(choice,c_choice)

  elif command==1:
    print("結束對戰!!")