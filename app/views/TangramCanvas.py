import tkinter as tk
from app.models.FlippableTangramPiece import FlippableTangramPiece

from app.models.TangramPiece import TangramPiece

class TangramCanvas(tk.Canvas):
    
    tangramPieces = None
    
    def __init__(self, parent, **options):
        super().__init__(parent,**options)
        self.tangramPieces = []
        options ={'fill':'black','activefill':'grey','outline':'white','activeoutline': 'black','width':'3'}
        self.tangramPieces.append(TangramPiece(self, 0, 0, 0,200, 100,100,**options))
        self.tangramPieces.append(TangramPiece(self, 0, 0, 200,0, 100,100,**options))
        self.tangramPieces.append(TangramPiece(self, 150, 50, 200,0, 200,100,**options))
        self.tangramPieces.append(TangramPiece(self, 100, 100, 150,50, 200,100,150,150 ,**options))
        self.tangramPieces.append(TangramPiece(self, 50, 150, 100,100, 150,150,**options))
        self.tangramPieces.append(FlippableTangramPiece(self,   0, 200, 50,150, 150,150,100,200,
                                                                50, 200, 0,150, 100,150,150,200,**options))
        self.tangramPieces.append(TangramPiece(self, 100, 200, 200,100, 200,200,**options))
        
    def resetGame(self):
        for tangramPiece in self.tangramPieces:
            tangramPiece.reset()
    
    def changeTheme(self, backgroundColor):
        self.configure(background=backgroundColor)
        if backgroundColor=='white':
            for tangramPiece in self.tangramPieces:
                tangramPiece.configure(outline='black', activeoutline = 'red')
        elif backgroundColor == 'red':
            for tangramPiece in self.tangramPieces:
                tangramPiece.configure(outline='white', activeoutline = 'black')
            
          
        

   