
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
        self.__canvas.grid(row=0, column=0,pady=(30, 10),padx=50,sticky=tk.NSEW)
        style = ttk.Style()
        style.configure('my.TButton', font=('Helvetica', 18,'bold'), padding = 4)
        button = ttk.Button(self, text='reset game',style='my.TButton')
        button.grid(row=1,column =0)
        button.bind("<ButtonRelease>",self.onReset)
        
    def onReset(self, event) :
        self.__canvas.resetGame()  
        
    def start(self):
        self.mainloop()
        
    