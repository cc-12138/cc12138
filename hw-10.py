import tkinter
import tkinter.messagebox
import os

class My_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)

        self.radio_var=tkinter.IntVar()
        self.radio_var.set(1)
        self.rb1 = tkinter.Radiobutton(self.top_frame,text='Click here to input info. to test.txt',variable=self.radio_var,value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,text='Click here to load info. to test.txt',variable=self.radio_var,value=2)
        self.rb1.pack()
        self.rb2.pack()

        self.ok_button = tkinter.Button(self.bottom_frame,text='OK',command=self.choose)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit',command=self.main_window.destroy)
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()
    def choose(self):
        self.main_window.destroy()
        if self.radio_var.get()==1:
            s=Savefile()
        if self.radio_var.get()==2:
            l=Loadfile()

class Savefile:
    def __init__(self):
        self.window=tkinter.Tk()
        self.top_frame=tkinter.Frame(self.window)
        self.middle1_frame=tkinter.Frame(self.window)
        self.middle2_frame=tkinter.Frame(self.window)
        self.bottom_frame=tkinter.Frame(self.window)

        self.entry_notice=tkinter.Label(self.top_frame,text='input info. to test.txt:')
        self.entry=tkinter.Entry(self.top_frame,width=30)
        self.entry_notice.pack(side='left')
        self.entry.pack(side='left')

        self.file_notice=tkinter.Label(self.middle1_frame,text='The file position:')
        self.position_label=tkinter.Label(self.middle1_frame,text='D:\\aa学习资料\\python\\作业源代码\\hw-10\\test.txt')
        self.file_notice.pack(side='left')
        self.position_label.pack(side='left')

        self.strnum=tkinter.StringVar()
        self.str_notice=tkinter.Label(self.middle2_frame,text='You have entry string number:')
        self.str_label=tkinter.Label(self.middle2_frame,textvariable=self.strnum)
        self.str_notice.pack(side='left')
        self.str_label.pack(side='left')

        self.ok_button=tkinter.Button(self.bottom_frame,text='OK',command=self.save)
        self.back_button=tkinter.Button(self.bottom_frame,text='back',command=self.back)
        self.quit_button=tkinter.Button(self.bottom_frame,text='quit',command=self.window.destroy)
        self.ok_button.pack(side='left')
        self.back_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle1_frame.pack()
        self.middle2_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()
    def save(self):
        self.message='Save Successfully'
        string=str(self.entry.get())
        self.strnum.set(len(string))
        f=open("D:/aa学习资料/python/作业源代码/hw-10/test.txt","w")
        f.write(string)
        tkinter.messagebox.showinfo('Selection',self.message)
        f.close()
    def back(self):
        self.window.destroy()
        m=My_GUI()

class Loadfile:
    def __init__(self):
        self.window=tkinter.Tk()
        self.top_frame=tkinter.Frame(self.window)
        self.middle1_frame=tkinter.Frame(self.window)
        self.middle2_frame=tkinter.Frame(self.window)
        self.bottom_frame=tkinter.Frame(self.window)

        self.position_notice=tkinter.Label(self.top_frame,text='The file position is:')
        self.position=tkinter.Label(self.top_frame,text='D:/aa学习资料/python/作业源代码/hw-10/test.txt')
        self.position_notice.pack(side='left')
        self.position.pack(side='left')

        self.read_notice=tkinter.Label(self.middle1_frame,text='The file\'s info. is:')
        self.read_notice.pack(side='left')

        self.back_button=tkinter.Button(self.bottom_frame,text='back',command=self.back)
        self.quit_button=tkinter.Button(self.bottom_frame,text='quit',command=self.window.destroy)
        self.back_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.info=tkinter.StringVar()
        self.file_read()
        self.file_info=tkinter.Label(self.middle1_frame,textvariable=self.info)
        self.file_info.pack(side='left')

        self.top_frame.pack()
        self.middle1_frame.pack()
        self.middle2_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()
    def file_read(self):
        self.message='Read Successfully'
        f=open("D:/aa学习资料/python/作业源代码/hw-10/test.txt","r")
        s=str(f.read())
        string=self.info.set(s)
        f.close()
        tkinter.messagebox.showinfo('Selection',self.message)
    def back(self):
        self.window.destroy()
        m=My_GUI()

my_gui=My_GUI()