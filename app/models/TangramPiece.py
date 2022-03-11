from ast import Lambda
from math import *
from tkinter import Canvas
class TangramPiece:
      __canvas = None
      __id = None
      __X = 0
      __Y = 0
      __dragStartX = None
      __dragStartY = None
      __dragStartCoords = None
      __resetCoords = None
      
      def __init__(self, canvas : Canvas, *coords,**options):
        self.__canvas = canvas
        self.__resetCoords =coords
        self.__id = self.__canvas.create_polygon(coords, options);
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
        self.bind("<Motion>", self.onDrag);
        self.bind('<ButtonPress>', self.onDragStart )
        self.bind('<ButtonRelease>', self.onDragEnd)
        self.bind('<Double-Button>', self.onDoubleClick)
        #self.bind('<Leave>',lambda event: print("test"))
        
      def onDoubleClick(self,event):
            self.rotate(45) 
      """
      description of onDragStart(self,event)
      the method is a handler for ButtonPress
      it sets a number of properties of the tangrampiece nessecary for 
      updating when being dragged.
      :event is the event that is generated and recieved by the handler
      the method sets the mousepoition on dragstart and sets the cornercoordinates of the piece.
      """  
      def onDragStart(self , event):
            self.__dragStartX = event.x
            self.__dragStartY = event.y
            self.__dragStartCoords = self.coords()
      
      """
      the description of onDragEnd(self, event)
      the method erases all memory of the startdrag details that were set previously
      """          
      def onDragEnd(self , event):
            self.__dragStartX = None
            self.__dragStartY = None
            self.__dragStartCoords = None
            

      """
      description of onDrag(self,event); it is a handler for draghandling 
      :event is the event that is generated and recieved by the handler
      the method determines new coords for the corners of the tangrampiece and 
      determines the new center of mass of the systenm ie its self.__X and self.__Y
      after that it updates the tangrampiece
      """  
      def onDrag(self,event):
            if self.dragStarted:
                  deltaX = event.x - self.__dragStartX
                  deltaY = event.y - self.__dragStartY
                  numberOfCorners = len(self.__dragStartCoords)
                  newCoords = self.__dragStartCoords.copy()
                  self.__X =0
                  self.__Y =0
                  for i in range(0,numberOfCorners):
                        if i %2 == 0:
                              newCoords[i] += deltaX
                              self.__X += newCoords[i]
                        else:
                              newCoords[i] += deltaY
                              self.__Y += newCoords[i]
                              
                  self.__X = 2*self.__X /numberOfCorners
                  self.__Y = 2*self.__Y /numberOfCorners
                  self.update(newCoords)
                  
                  
      """
            description of rotate(self,angle)
            this method will rotate the tangrampiece over a given amount of degrees
            rotation direction is counterclockwise. Rotation is performed round X and Y 
            being the center of the Tangrampiece
            :angle in degrees
            result a rotated tangrampiece in the given rotation direction
      """         
      def rotate(self,angle):
            coords = self.coords()
            newcoords = []
            cosAngle = cos(angle*pi/180)
            sinAngle = sin(angle*pi/180)
            
            for i in range(0,len(coords)):
                  if i%2 ==0:
                        xrel = coords[i] - self.__X
                  else:
                        yrel = coords[i] - self.__Y
                        newcoords.append( cosAngle*xrel + sinAngle*yrel + self.__X)
                        newcoords.append(-sinAngle*xrel + cosAngle*yrel +self.__Y)
            self.update(newcoords)
                  
      """
      description of update(self,coords)
      :coords is a new full list consisting of all the x,y values of corners
      the method gives the shape a new form determined by the set of given coords
      """      
      def update(self, coords):
            self.canvas.coords(self.id,coords)
      
      """
      description of coords(self)
      this method returns the set of present xy values of the TangramPiece
      it gives them as a list with the values forming two bu two a set of 
      coordinates of a corner  of the piece           
      """
      def coords(self) :
            return self.canvas.coords(self.id) 
      """
      description of bind(self, event, callback)
      this method allows you to bind callback for specified events 
      :event an eventtype like <Motion> or <MouseRelease>
      :callback the function to handle the event; must have an eventargument
      """
      def bind(self, event, callback:str):
            self.canvas.tag_bind(self.id,event, callback)
      
      def reset(self):
            self.update(self.__resetCoords)
            
      @property
      def dragStarted(self):
            return self.__dragStartX is not None  and self.__dragStartY is not None and self.__dragStartCoords is not None 
            
      
      @property 
      def id(self):
            return self.__id
      @property
      def canvas (self):
            return self.__canvas
        
            
        
        
      
  
  