from tkinter import Canvas
from app.models.TangramPiece import TangramPiece


class FlippableTangramPiece (TangramPiece):
    __flippedCoords = None
    __resetFlippedCoords=None
    def __init__(self, canvas: Canvas, *coords, **options):
        #coords consists of a double set of coordinates one for the polygone, one for the flipped version
        polygoneSize = len(coords)/2 
        Coords = []
        self.__FlippedCoords=[]
        for i in range(polygoneSize):
            Coords.append(coords[i])
            self.__FlippedCoords.append(coords(i+polygoneSize))
        self.__resetFlippedCoords = self.__FlippedCoords.copy()
        super().__init__(canvas, Coords, **options)