from math import *
from tkinter import Canvas
class TangramPiece:
      __canvas = None
      __id = None
      _X = 0
      _Y = 0
      _dragStartX = None
      _dragStartY = None
      _dragStartCoords = None
      __resetCoords = None
      
      def __init__(self, canvas : Canvas, *coords,**options):
            self.__canvas = canvas
            self.__resetCoords =coords
            self.__id = self.__canvas.create_polygon(coords, options);
            self.setCenter(coords)
            #de twee handlers worden gkoppeld; alle andere handlers worden in onDragStart gekoppeld
            # en weer verwijderd in onDragEnd, dus motion and dragend handlers zijn er enkel bij noodzaak
            self.bind('<ButtonPress>', self.onDragStart )
            self.bind('<Double-Button>', self.onDoubleClick)
        
      def onDoubleClick(self,event):
            coords = self.coords()
            newcoords = self.rotate(45,*coords) 
            self.update(newcoords)
            
           
      """
      description of onDragStart(self,event)
      the method is a handler for ButtonPress
      it sets a number of properties of the tangrampiece nessecary for 
      updating when being dragged to be specific.
      dragStartX and dragStartY are the position where the drag started. These are used to determine the 
      distance moved by the mouse
      dragStartCoords are the coordinates of the polygone at start drag
      once the distance moved is known it can be added to the dragStartCoords to find nwew coords for the polygone
      :event is the event that is generated and recieved by the handler
      the method sets the mousepoition on dragstart and sets the cornercoordinates of the piece.
      """  
      def onDragStart(self , event):
            self._dragStartX = event.x
            self._dragStartY = event.y
            self._dragStartCoords = self.coords()
            self.bind("<Motion>", self.onDrag)
            self.bind('<ButtonRelease>', self.onDragEnd)
      
      
      """
      the description of onDragEnd(self, event)
      the method erases all memory of the startdrag details that were set previously
      """          
      def onDragEnd(self , event):
            self._dragStartX = None
            self._dragStartY = None
            self._dragStartCoords = None
            self.unbind("<Motion")
            self.unbind('<ButtonRelease')
            

      """
      description of onDrag(self,event); it is a handler for draghandling 
      :event is the event that is generated and recieved by the handler
      the method determines new coords for the corners of the tangrampiece and 
      determines the new center of mass of the systenm ie its self._X and self._Y
      after that it updates the tangrampiece polygone on the canvas
      """  
      def onDrag(self,event):
            if self.dragStarted:
                  deltaX = event.x - self._dragStartX
                  deltaY = event.y - self._dragStartY
                  newCoords = self.translate(deltaX, deltaY,self._dragStartCoords)
                  self.setCenter(newCoords)
                  self.update(newCoords)
                  
      def translate(self, deltaX, deltaY, coords):
            
            newCoords = []
            count =0
            for coord in coords:
                  if count%2 == 0:
                        newCoords.append(coord + deltaX)
                  else:
                        newCoords.append(coord + deltaY)
                  count +=1
            return newCoords
      
      def setCenter(self, coords):
            self._X = 0
            self._Y = 0
            count = 0
            numberOfCorners = len(coords)/2
            for coord in coords:
                  if count%2 ==  0:
                        self._X += coord
                  else:
                        self._Y+= coord
                  count +=1
            self._X = self._X/numberOfCorners
            self._Y = self._Y/numberOfCorners
            
      """
            description of rotate(self,angle,*coords)
            this method will rotate the tangrampiece over a given amount of degrees
            rotation direction is counterclockwise. Rotation is performed round _X and _Y 
            being the center of the Tangrampiece
            :angle in degrees
            *coords the coordinates as a list of the polygone
            returns the rotated coords of the polygone
      """         
      def rotate(self,angle,*coords):
            newcoords = []
            cosAngle = cos(angle*pi/180)
            sinAngle = sin(angle*pi/180)
            
            for i in range(0,len(coords)):
                  if i%2 ==0:
                        xrel = coords[i] - self._X
                  else:
                        yrel = coords[i] - self._Y
                        newcoords.append( cosAngle*xrel + sinAngle*yrel + self._X)
                        newcoords.append(-sinAngle*xrel + cosAngle*yrel +self._Y)
            return newcoords
                  
      """
      description of update(self,coords)
      :coords is a new full list consisting of all the x,y values of corners
      the method gives the shape a new form determined by the set of given coords
      """      
      def update(self, coords):
            self.canvas.coords(self.id,coords)
            self.__canvas.tkraise(self.id)
      
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
      
      def unbind(self, event):
            self.canvas.tag_unbind(self.id,event)

      def reset(self):
            self.update(self.__resetCoords)
            
      @property
      def dragStarted(self):
            return self._dragStartX is not None  and self._dragStartY is not None and self._dragStartCoords is not None 
            
      
      @property 
      def id(self):
            return self.__id
      @property
      def canvas (self):
            return self.__canvas
        
      def configure(self, **options):
            self.canvas.itemconfigure(self.id, **options)
        
        
      
  
  