from tkinter import Canvas
from app.models.TangramPiece import TangramPiece


class FlippableTangramPiece (TangramPiece):
    __flippedCoords = None
    __resetFlippedCoords=None
    
    __dragStartFlippedCoords = None
    
    def __init__(self, canvas: Canvas, *coords, **options):
        #coords consists of a double set of coordinates one for the polygone, one for the flipped version
        polygoneSize = len(coords)//2 
        polygoneCoords = []
        self.__flippedCoords=[]
        for i in range(0, polygoneSize):
            polygoneCoords.append(coords[i])
            self.__flippedCoords.append(coords[i+8])
        self.__resetFlippedCoords = self.__flippedCoords.copy()
        super().__init__(canvas, *polygoneCoords, **options)
        self.bind('<Control-Button-1>', self.onControlClick)
    """
    when the polygone is flipped its coords  are swapped with these of the flipped version
    """   
    def onControlClick(self,event):
        temp = self.coords()
        self.update(self.__flippedCoords)
        self.__flippedCoords = temp
    """
    the rotate method simply performs the duties of the parent and also performs a rotation on the flippedCoords
    just to keep the flipped coords synchronous with the shown polygone
    """
    def rotate(self, angle, *coords):
        self.__flippedCoords = super().rotate(angle,*self.__flippedCoords)
        return super().rotate(angle, *coords)
    
    def reset(self):
        self.__flippedCoords = self.__resetFlippedCoords.copy()
        super().reset()
    """
    onDragStart description
    method perfoms the tasks of the parent and also sets the dragStartFlippedCoords of the flippedCoords
    """   
    def onDragStart(self, event):
        super().onDragStart(event)
        self.__dragStartFlippedCoords =self.__flippedCoords.copy()
    """
    onDrag performs the tasks of the parent and determines the new translated __flippedCcoords of the polygone
    """   
    def onDrag(self, event):
        super().onDrag(event)
        if self.__dragStartFlippedCoords  is not None:
            deltaX = event.x - self._dragStartX
            deltaY = event.y - self._dragStartY
            self.__flippedCoords = self.translate(deltaX, deltaY, self.__dragStartFlippedCoords)
            
    def onDragEnd(self, event):
        super().onDragEnd(event)
        self.__dragStartFlippedCoords = None
    
    def reset(self):
        super().reset()
        self.__flippedCoords = self.__resetFlippedCoords