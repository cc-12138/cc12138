import tkinter

class My_GUI:
    def __init__(self):
        self.window=tkinter.Tk()

        self.cavans=tkinter.Canvas(self.window, width=500, height=500)

        self.cavans.create_line(150,150,150,400)
        self.cavans.create_oval(150,150,400,400)
        self.cavans.create_rectangle(350,400,500,500)

        self.cavans.pack()
        tkinter.mainloop()

my_gui=My_GUI()