from tkinter import Canvas
from app.models.TangramPiece import TangramPiece


class FlippableTangramPiece (TangramPiece):
    __flippedCoords = None
    __resetFlippedCoords=None
    def __init__(self, canvas: Canvas, *coords, **options):
        #coords consists of a double set of coordinates one for the polygone, one for the flipped version
        polygoneSize = len(coords)//2 
        Coords = []
        self.__flippedCoords=[]
        for i in range(8):
            Coords.append(coords[i])
            self.__flippedCoords.append(coords[i+8])
        self.__resetFlippedCoords = self.__flippedCoords.copy()
        super().__init__(canvas, *Coords, **options)
        self.bind('<Control-Button-1>', self.onControlClick)
        
    def onControlClick(self,event):
        temp = self.coords()
        self.update(self.__flippedCoords)
        self.__flippedCoords = temp
    """
    the rotate method simply performs the duties of the parent and perfors a rotation on the flippedCoords
    just to keep the flipped coords synchronous with the shown polygone
    """
    def rotate(self, angle, *coords):
        self.__flippedCoords = super().rotate(angle,*self.__flippedCoords)
        return super().rotate(angle, *coords)
    
    def reset(self):
        self.__flippedCoords = self.__resetFlippedCoords.copy()
        super().reset()  