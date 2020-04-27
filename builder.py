from tkinter import *

class Builder(object):
    def __init__(self):
        self.screen = Tk()
        self.screen.geometry("400x350+350+200")
        self.layouts= []
        self.canvas=Canvas(self.screen,height=300, width=400,bg="blue")
        self.canvas.grid(row=0, column=0,columnspan=3)
        for row in range(0,400,10):
            for column in range(0,300,10):
                self.canvas.create_rectangle(row,column,row+10,column+10,outline="black",fill="blue",tag=f"rect{row}{column}")
                self.canvas.tag_bind(f'rect{row}{column}','<B1-Motion>', self._editable)
                self.canvas.tag_bind(f'rect{row}{column}', '<B3-Motion>', self._erase)

        def saveDraw():
            layout = ""
            for column in range(0, 300, 10):
                for row in range(0, 400, 10):
                    id = self.canvas.find_closest(row,column)
                    color = self.canvas.itemcget(id,"fill")
                    if color == "blue":
                        layout += " "
                    elif color == "black":
                        layout += "X"
                layout += '\n'
            self.layouts.append(layout)
            clearScreen()
        def clearDB():
            self.layouts = []
        self.clearDBbutton = Button(self.screen,text= 'EMPTY LAYOUTS', command= clearDB)
        self.clearDBbutton.grid(row=1,column=2)



        self.saveButton = Button(self.screen, text="SAVE", command= saveDraw)
        self.saveButton.grid(row=1,column=0)


        def clearScreen():
            for row in range(0, 400, 10):
                for column in range(0, 300, 10):
                    self.canvas.itemconfigure(f'rect{row}{column}',outline="black",fill="blue")


        self.clearButton = Button(self.screen, text="CLEAR",command=clearScreen)
        self.clearButton.grid(row=1, column=1)



        self.screen.mainloop()

    def _editable(self,event):
        id = event.widget.find_closest(event.x, event.y)
        self.canvas.itemconfigure(id,fill='black')
    def _erase(self,event):
        id = event.widget.find_closest(event.x, event.y)
        self.canvas.itemconfigure(id, fill='blue')


def test():
    builder = Builder()
    for layout in builder.layouts:
        print(f"layout:\n{layout}\n")
test()