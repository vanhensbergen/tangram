from tkinter import Canvas
class TangramPiece:
      __canvas = None
      __id = None
      __X = 0
      __Y = 0
      dragStartX = None
      dragStartY = None
      dragStartCoords = None
      
      def __init__(self, canvas : Canvas, *coords):
        self.__canvas = canvas
        self.__id = self.__canvas.create_polygon(coords);
        count = 0
        numberOfCorners = len(coords)/2
        for coord in coords:
            if count%2 ==  0:
                  self.__X += coord
            else:
                  self.__Y+= coord
            count +=1
        self.__X = self.__X/numberOfCorners
        self.__Y = self.__Y/numberOfCorners
        self.bind("<Motion>", self.onMouseMove);
        self.bind('<ButtonPress>', self.onMousePressed )
        self.bind('<ButtonRelease>', self.onMouseReleased)
        
      def onMousePressed(self , event):
            self.dragStartX = event.x
            self.dragStartY = event.y
            self.dragStartCoords = self.canvas.coords(self.id)
            
            
      def onMouseReleased(self , event):
            self.dragStartX = None
            self.dragStartY = None
            self.dragStartCoords = None

        
      def onMouseMove(self,event):
            if self.dragStarted:
                  deltaX = event.x - self.dragStartX
                  deltaY = event.y - self.dragStartY
                  newCoords = self.dragStartCoords.copy()
                  for i in range(0,len(newCoords)):
                        if i %2 == 0:
                              newCoords[i] += deltaX
                        else:
                              newCoords[i] += deltaY
                  self.moveTo(newCoords)
            
      def rotate(self):
            pass
            
      def moveTo(self, coords):
             self.canvas.coords(self.id,coords)
        
      def bind(self, event, callback:str):
            self.canvas.tag_bind(self.id,event, callback)
      
      @property
      def dragStarted(self):
            return self.dragStartX is not None  and self.dragStartY is not None and self.dragStartCoords is not None 
            
      @property
      def X(self): return self.__X
      
      @property
      def Y(self): return self.__Y
      
      @property 
      def id(self):
            return self.__id
      @property
      def canvas (self):
            return self.__canvas
        
            
        
        
      
  
  