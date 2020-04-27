from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from components import MazeGUI

# Initializing first screen
start_screen=Tk()
start_screen.geometry("400x300+350+200")
start_screen.configure()

# Button methods
def start_game():
    global button_clicked
    start_screen.destroy()
    button_clicked=True


# creating button
start_btn=Button(start_screen,text="START",command=start_game,width=20,height=2,bg="light blue",cursor="hand2")
button_clicked=False


#messages in the first screen
welcome=Label(start_screen,text="WELCOME TO THE AMAZEING GAME",font=40)
welcome.grid(row=0,column=0,columnspan=2,padx=55)

inst_header=Label(start_screen,text="INSTRUCTIONS:",font=20)
inst_header.grid(row=1,column=0,pady=(30,10),sticky='w')

inst_1=Label(start_screen,text="-To go to the next level, head to the exit door(SS)")
inst_1.grid(row=2,column=0,sticky=W)

inst_2=Label(start_screen,text="-Do not go beyond the screen's limits")
inst_2.grid(row=3,column=0,sticky=W)

inst_3=Label(start_screen,text="-Do not hit the walls (X)")
inst_3.grid(row=4,column=0,sticky=W)

inst_4=Label(start_screen,text="-Do not run out of moves")
inst_4.grid(row=5,column=0,sticky=W)

# Placing start button on the screen
start_btn.grid(row=6,column=0,pady=40,sticky="W",padx=120)

# Forever loop to the first screen
start_screen.mainloop()

# Going to second screen if button is pressed

if button_clicked:
   #  easy_screen=Tk()
   #  easy_screen.geometry("400x330")
   #
   #
   #
   #  # Instantiating easy maze
   #  easy_maze=MazeGUI(1,easy_screen)
   #
   # # easy_screen.mainloop()0
    while True:
        easy_screen = Tk()
        easy_screen.geometry("400x335+500+200")
        easy_maze=MazeGUI(1, easy_screen)
        if easy_maze.found_exit:
            easy_maze.next_level=True
        easy_screen.mainloop()

        if easy_maze.next_level or easy_maze.close:
            break




    if easy_maze.next_level:
        while True:
            medium_screen = Tk()
            medium_screen.geometry("400x335+500+200")
            medium_maze = MazeGUI(2, medium_screen)
            if medium_maze.found_exit:
                medium_maze.next_level = True
            medium_screen.mainloop()

            if medium_maze.next_level or medium_maze.close:
                break


        if medium_maze.next_level:
            while True:
                hard_screen = Tk()
                hard_screen.geometry("400x335+500+200")
                hard_maze = MazeGUI(3, hard_screen)
                if hard_maze.found_exit:
                    hard_maze.next_level = True

                hard_screen.mainloop()

                if hard_maze.next_level or hard_maze.close:
                    break
            r=Tk()
            r.wm_withdraw()
            messagebox.showinfo("Victory", "Congratulations, human! You've won the game!")

            r.mainloop()







