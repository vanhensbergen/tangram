import tkinter as tk

from app.models.TangramPiece import TangramPiece

class TangramCanvas(tk.Canvas):
    
    tangramPieces = None
    
    def __init__(self, parent, **options):
        super().__init__(parent,**options)
        self.tangramPieces = []
        
    def showTriangle(self):
        self.tangramPieces.append(TangramPiece(self, 100,100, 200,100, 200,200))
        

    