from components import *
from tkinter import *
import time
root=Tk()
mymaze=MazeGUI(3,root)


print("maze:\n",mymaze.cmaze)
print("\nmaze list:\n",mymaze.maze_list)
print("\n maze each char:\n", mymaze.each_char)
print("\n maze 2d list:\n",mymaze.maze_2dlist)
print("\n list w ball:\n", mymaze.list_w_ball)
print("\n index of ball:\n",mymaze.ball_index)
print("Index of ball in sublist:",mymaze.index_ball_in_sublist)
print("Index of sublist with ball:",mymaze.index_list_w_ball)


print("maze moving downwards :\n",mymaze.cmaze)
print("\nmaze list:\n",mymaze.maze_list)
print("\n maze each char:\n", mymaze.each_char)
print("\n maze 2d list:\n",mymaze.maze_2dlist)
print("\n list w ball:\n", mymaze.list_w_ball)
print("\n index of ball:\n",mymaze.ball_index)
print("Index of ball in sublist:",mymaze.index_ball_in_sublist)
print("Index of sublist with ball:",mymaze.index_list_w_ball)

def down_and_update(event):
    pass

mymaze.canvas.bind("<Button-1>",down_and_update)
root.mainloop()

root2= Tk()
mymaze.canvas.configure(root2)
mymaze.canvas.pack()
root2.mainloop()
# test=['r','o','m','e','r','o']
# test[0],test[1]=test[1],test[0]
# a='eee'
# help(a.join)
# def print(event):
#     global rect
#     global canvas
#     canvas.coords("rectangle",250,250,450,450)
#     canvas.itemconfig("rectangle",fill="blue")
#
#
# root = Tk()
# canvas = Canvas(root,height=500,width=500,bg="green")
# canvas.grid(row=1,column=0)
# middlex = middley = 250
# rect=canvas.create_rectangle(middlex-100,middley-100,middlex+100,middley+100,fill="green",outline="green",tag="rectangle")
# canvas.tag_bind("rectangle", "<Button-1>", print)
#
# root.mainloop()