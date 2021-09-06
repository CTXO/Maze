from tkinter import *
class Maze(object):
    # Creating mazes(easy, medium and hard)
    maze1= '\n'+ \
            "XXXXXXXXXXXXXXXXXXSSX\n" +\
            "X                X  X\n" +\
            "X  XXXXXXXXXXXX  X  X\n" +\
            " O      X     X  X  X\n" +\
            "        X     X  X  X\n" +\
            "X  XXX  X  X  X  X  X\n" +\
            "X  XXX     X  X  X  X\n" +\
            "X  XXX     X  x  X  X\n" +\
            "X  XXX     X  X  X  X\n" +\
            "X  XXX     X  X  X  X\n" +\
            "X  XXXXXXXXX  XXXX  X\n" +\
            "X          X        X\n" +\
            "X  XXXX  XXXXXXXXX  X\n" +\
            "X              X    X\n" +\
            "X              X    X\n" +\
            "XXXXXXXXXXXXXXXXXXXXX\n"

    maze2=  "X  XXXXXXXXXXXXXXXXXXXXXX\n" +\
            "X O    X      X         X\n" +\
            "X      X      X         X\n" +\
            "X  XX  X  XX  X  XXXX   X\n" +\
            "X  X   X   X     X  X   X\n" +\
            "X  X   X   X     X  X   X\n" +\
            "X  XXXXXX  XXXX  X  X   X\n" +\
            "X   X   X     X     X   X\n" +\
            "X   X  XX     X     X   X\n" +\
            "XXX X  X      XXXXXXX   X\n" +\
            "X      X    X    X      X\n" +\
            "X  XXXXX    XXXXXX      X\n" +\
            "X        X    X         X\n" +\
            "X        X    X         X\n" +\
            "XXXXXXXXXXXXXXXXXXXXXXSSX\n"
    maze3='\n'+\
            "                                                                 \n"+ \
            "                                                                 \n" + \
            "                                                                 \n" + \
            "        XSSSSX                         \n" +\
            "        X    X                          \n" +\
            "        X    X                         \n" +\
            "        X    X                          \n" +\
            "        XXXXXX                           \n" +\
            "        X    X                           \n" +\
            "        X    X                           \n" +\
            "        X    X                          \n" +\
            "        X    X                          \n" +\
            "        X    X                           \n" +\
            "        X O  X                            \n" +\
            "        X    X                            \n" +\
            "                                           \n" + \
          "                                              \n" + \
          "                                               \n" + \
          "                                                 \n" + \
          "                                                \n" + \
     "                                                                \n"
    mazes = [maze1,maze2,maze3]
    # Boolean values to check player status
    found_exit = False
    hit_wall = False
    keep_playing = True
    out_of_moves = False
    won = True

    # Converting maze to lists and matrices

    def __init__(self , maze_num):
        self.maze_num=maze_num

        if maze_num==1:
            self.cmaze = self.mazes[0]
            self.moves = 75
        elif maze_num == 2:
            self.cmaze = self.mazes[1]
            self.moves = 60
        elif maze_num == 3:
            self.cmaze = self.mazes[2]
            self.moves = 21
        else:
            raise ValueError("Type '1','2' or '3' as parameter ")

        self.maze_list = self.cmaze.split("\n")
        self.each_char= [char for char in self.cmaze[:]]
        self.maze_2dlist=[]
        for line in self.maze_list[:]:
            temp_list=[]
            for char in line:
                temp_list.append(char)
            self.maze_2dlist.append(temp_list)
        self.ball_index=self.each_char.index("O")
        self.list_w_ball=[char for list in self.maze_2dlist[:] for char in list if "O" in list]
        self.index_ball_in_sublist=self.list_w_ball.index('O')
        self.index_list_w_ball=self.maze_2dlist.index(self.list_w_ball)
        self.backup=self.cmaze

    def right(self):
        if self.each_char[self.ball_index+1] == "X":
            self.hit_wall = True
        elif self.each_char[self.ball_index+1] == "S":
            self.found_exit = True
        if self.moves == 0:
            self.out_of_moves = True
        self.moves -= 1
        self.each_char[self.ball_index],self.each_char[self.ball_index+1]= \
            self.each_char[self.ball_index + 1], self.each_char[self.ball_index]

        self.cmaze=''.join(self.each_char)
        self.maze_list = self.cmaze.split("\n")
        self.maze_2dlist = []
        for line in self.maze_list[:]:
            temp_list = []
            for char in line:
                temp_list.append(char)
            self.maze_2dlist.append(temp_list)
        self.list_w_ball = [char for list in self.maze_2dlist[:] for char in list if "O" in list]
        self.ball_index += 1
        self.index_ball_in_sublist +=1


    def left(self):
        if self.each_char[self.ball_index-1] == "X":
            self.hit_wall = True
        elif self.each_char[self.ball_index-1] == "S":
            self.found_exit = True
        if self.moves == 0:
            self.out_of_moves = True
        self.moves -= 1

        self.each_char[self.ball_index], self.each_char[self.ball_index - 1] = \
            self.each_char[self.ball_index - 1], self.each_char[self.ball_index]

        self.cmaze = ''.join(self.each_char)
        self.maze_list = self.cmaze.split("\n")
        self.maze_2dlist = []

        for line in self.maze_list[:]:
            temp_list = []
            for char in line:
                temp_list.append(char)
            self.maze_2dlist.append(temp_list)
        self.list_w_ball = [char for list in self.maze_2dlist[:] for char in list if "O" in list]
        self.ball_index -= 1
        self.index_ball_in_sublist -= 1


    def up(self):
        if self.maze_2dlist[self.index_list_w_ball-1][self.index_ball_in_sublist] == "X":
            self.hit_wall = True
        elif self.maze_2dlist[self.index_list_w_ball-1][self.index_ball_in_sublist] == "S":
            self.found_exit = True
        if self.moves == 0:
            self.out_of_moves = True
        self.moves -= 1
        self.maze_2dlist[self.index_list_w_ball][self.index_ball_in_sublist],self.maze_2dlist[self.index_list_w_ball-1][self.index_ball_in_sublist] = \
            self.maze_2dlist[self.index_list_w_ball - 1][self.index_ball_in_sublist],self.maze_2dlist[self.index_list_w_ball][self.index_ball_in_sublist]
        self.maze_list=[]
        for list in self.maze_2dlist:
            str=""
            for char in list:
                str+=char
            self.maze_list.append(str)

        self.cmaze = '\n'.join(self.maze_list)
        self.each_char= [char for char in self.cmaze[:]]
        self.list_w_ball = [char for list in self.maze_2dlist[:] for char in list if "O" in list]
        self.index_list_w_ball -= 1
        self.ball_index=self.each_char.index("O")

    def down(self):
        if self.maze_2dlist[self.index_list_w_ball+1][self.index_ball_in_sublist] == "X":
            self.hit_wall = True
        elif self.maze_2dlist[self.index_list_w_ball+1][self.index_ball_in_sublist] == "S":
            self.found_exit = True
        if self.moves == 0:
            self.out_of_moves = True
        self.moves -= 1
        self.maze_2dlist[self.index_list_w_ball][self.index_ball_in_sublist],self.maze_2dlist[self.index_list_w_ball+1][self.index_ball_in_sublist]= \
            self.maze_2dlist[self.index_list_w_ball + 1][self.index_ball_in_sublist],self.maze_2dlist[self.index_list_w_ball][self.index_ball_in_sublist]
        self.maze_list = []

        for list in self.maze_2dlist:
            str = ""
            for char in list:
                str+=char
            self.maze_list.append(str)

        self.cmaze = '\n'.join(self.maze_list)
        self.each_char= [char for char in self.cmaze[:]]
        self.list_w_ball = [char for list in self.maze_2dlist[:] for char in list if "O" in list]
        self.index_list_w_ball += 1
        self.ball_index=self.each_char.index("O")

    def reset(self):
        self.__init__(self.maze_num)


class MazeGUI(Maze):
    attempt = True
    close = False
    def tryAgain(self):
        self.root.destroy()
        self.attempt=True

    def __init__(self, maze_num, root):
        Maze.__init__(self, maze_num)
        self.next_level=False
        self.root=root
        self.canvas=Canvas(root,height=300, width=400,bg="blue")
        self.canvas.grid(row=1, column=0, columnspan=5)
        self.initx, self.inity =88 , 30
        count = 0
        tag_count = 0
        self.f_ball_index=self.ball_index
        self.cmoves = self.moves
        self.canvas.create_text(200, 10, text=f"Level {self.maze_num}",font=20)
        self.canvas.create_text(345, 225, text=f"{self.cmoves} moves left", tags="moves")
        for i in self.each_char:

            self.canvas.create_rectangle(self.initx + count * 10, self.inity +
                                         10, self.initx + 10 + count * 10, self.inity + 20, tags=f"char{tag_count}",
                                         outline="", fill="blue")
            count += 1
            if i == "\n":
                self.inity += 10
                count = 0
            if i == "X":
                self.canvas.itemconfig(f"char{tag_count}", fill="black")

            if i == "S":
                self.canvas.itemconfig(f"char{tag_count}", fill="green")
            if i == "O":
                self.canvas.create_oval(self.canvas.coords(f"char{tag_count}"), fill="red",tags="ball")
                self.first_ball_tag=f"char{tag_count}"
            tag_count += 1

        if maze_num == 3:
            self.canvas.create_text(345, 205, text=f"{self.cmoves} moves left", tags="moves",font=20)

        self.canvas.bind("<Left>",self.leftGUI)
        self.canvas.bind("<Right>",self.rightGUI)
        self.canvas.bind("<Up>",self.upGUI)
        self.canvas.bind("<Down>",self.downGUI)
        self.canvas.focus_set()

        self.tryagain = Button(self.root, text="Try Again", command=self.tryAgain, state="disabled", width=20)
        self.tryagain.grid(row=2, column=0, sticky=W, padx=7)

        self.next = Button(self.root, text="Next Level", command=self.nextLevel, state="disabled", width=20)
        self.next.grid(row=2, column=4)
        if self.maze_num == 3:
            self.next.configure(text="FINISH")
        self.root.protocol("WM_DELETE_WINDOW", self.closeWindow)

    def nextLevel(self):
        self.attempt = False
        self.next_level=True
        self.root.destroy()
    def closeWindow(self):
        self.close  = True
        self.root.destroy()
    def update(self):
        self.cmoves-=1
        self.canvas.delete("ball")

        def ignore(event):
            pass

        tag_count=0
        for i in self.each_char:
            if i =="O":
                self.canvas.create_oval(self.canvas.coords(f"char{tag_count}"), fill="red", tags="ball")
            tag_count+=1
        self.canvas.itemconfig("moves", text=f"{self.cmoves} moves left")


        if (self.hit_wall or self.moves == 0) and not self.found_exit:

            self.canvas.bind("<Left>", ignore)
            self.canvas.bind("<Right>", ignore)
            self.canvas.bind("<Up>", ignore)
            self.canvas.bind("<Down>", ignore)
            self.tryagain.configure(state="normal")

        elif self.found_exit:
            self.canvas.bind("<Left>", ignore)
            self.canvas.bind("<Right>", ignore)
            self.canvas.bind("<Up>", ignore)
            self.canvas.bind("<Down>", ignore)
            self.next.configure(state="normal")

    def leftGUI(self, event):
        self.left()
        self.update()

    def rightGUI(self, event):
        self.right()
        self.update()

    def upGUI(self, event):
        self.up()
        self.update()

    def downGUI(self, event):
        self.down()
        self.update()





