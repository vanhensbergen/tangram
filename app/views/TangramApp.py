import tkinter as tk

from app.views.TangramCanvas import TangramCanvas


class TangramApp(tk.Tk):
    
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry("800x800")
        canvas =  TangramCanvas(self,width=700, height=700,bg="red")
        canvas.grid(row=0, column=0,pady=50,padx=50,sticky=tk.NSEW)
        canvas.showTriangle()
        
        
        
    def start(self):
        self.mainloop()
        
    