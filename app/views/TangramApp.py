
import tkinter as tk
from tkinter import ttk

from app.views.TangramCanvas import TangramCanvas


class TangramApp(tk.Tk):
    __canvas = None
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry("800x800")
        self.__canvas =  TangramCanvas(self,width=700, height=700,bg="red")
        self.__canvas.grid(row=0, column=0,columnspan=2,pady=(30, 10),padx=50,sticky=tk.NSEW)
        style = ttk.Style()
        style.configure('my.TButton', font=('Helvetica', 18,'bold'), padding = 4)
        button = ttk.Button(self, text='reset game',style='my.TButton')
        button.grid(row=1,column =0, sticky =tk.E)
        button.bind("<ButtonRelease>",self.onReset)
        button = ttk.Button(self, style='my.TButton',text='white')
        button.grid(row =1, column = 1, sticky =tk.W)
        button.bind("<ButtonRelease>",self.onThemeChange)
        
    def onReset(self, event) :
        self.__canvas.resetGame()  
        
        
    def onThemeChange(self, event):
        # event.widget.configure(text="test")
        colour = event.widget.cget('text')
        # if event.widget.cget('text') == 'white':
        # print(text)  
        self.__canvas.changeTheme(colour) 
        if colour == 'white':
            event.widget.configure(text="red")
        else:
            event.widget.configure(text="white")
            
        
    def start(self):
        self.mainloop()
        
    