import math as math
import sys

try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *

except:
    print("Error: PyOpengl was not installed correctly")
    sys.exit()

class myGraphics:
    def __init__(self) -> None:
        self.width=600
        self.height=800
        
    
    def Menara(self): 
        
        self.flip = 1
        self.background() # grass, sky
        self.block1() # 1st dome
        self.block2() # building body
        self.block3() # 2nd dome
        self.block4() # side building
        self.block5() # 3rd dome & front door
        self.word() # Menara Kinabalu banner 
        
        self.flip = -1 # use reflection to flip the image/object 
        self.block3() # 2nd dome
        self.block4() # side building
        self.block5() # 3rd dome & front door
         
    
    def background(self):
        
        # grass
        glBegin(GL_POLYGON)
        glColor3f(44/255, 142/255, 10/255)
        self.draw([[-2,-4],
                   [-2,-1]]),
        glColor3f(153/204, 204/204, 0/204)           
        self.draw([[2,-1],
                   [2,-4]])
        glEnd()
        
        # sky
        glBegin(GL_POLYGON)
        glColor3f(204/255, 238/255, 255/255)
        self.draw([[-2,2]]),
        glColor3f(238/255, 215/255, 112/255)           
        self.draw([[2,2]]),
        glColor3f(253/255, 210/255, 134/255)
        self.draw([[2,-1],
                   [-2,-1]])
                        
        glEnd()
    def block1(self):
        
        # dome
        glBegin(GL_POLYGON)
        glColor3f(255/255, 255/255, 230/255)
        glEnd()
        self.drawCircle(0,1.2, radius = 0.18)
        glEnd()
        
        # dome piece
        glBegin(GL_POLYGON)
        glColor3f(241/255, 217/255, 167/255)
        self.draw([[-0.03,1.38],
                  [-0.03,1.4],
                  [0.03,1.4],
                  [0.03,1.38]])
        glEnd()
        
        # dome sharp top
        glBegin(GL_POLYGON)
        glColor3f(255/255, 255/255, 230/255)
        self.draw([[-0.02,1.4],
                  [0.02,1.4],
                  [0,1.7]])
        glEnd()
        
        # dome 1st body
        glBegin(GL_POLYGON)
        glColor3f(241/255, 217/255, 167/255)
        self.draw([[-0.22,1.15],
                  [-0.22,1.2],
                  [0.22,1.2],
                  [0.22,1.15]])
        glEnd()
        
        # dome 2nd body
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[-0.21,1.12],
                  [-0.21,1.15],
                  [0.21,1.15],
                  [0.21,1.12]])
        glEnd()
    
        # dome 3rd body
        glBegin(GL_POLYGON)
        glColor3f(102/102, 51/102, 0/102)
        self.draw([[-0.24,1.08],
                  [-0.24,1.12],
                  [0.24,1.12],
                  [0.24,1.08]])
        glEnd()
        
        # piece under dome
        glBegin(GL_POLYGON)
        glColor3f(241/255, 217/255, 167/255)
        self.draw([[-0.29,0.9],
                  [-0.29,1.12],
                  [0.29,1.12],
                  [0.29,0.9]])
        glEnd()   
        
        # windows
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0,1.015]])
        glColor3f(26/255, 104/255, 210/255)
        self.draw([[-0.26,0.96],
                  [-0.26,1.07],
                  [0.26,1.07],
                  [0.26,0.96],
                  [-0.26,0.96]])
        glEnd()
        
         # lines1
        glBegin(GL_POLYGON)
        glColor3f(241/255, 217/255, 167/255)
        self.draw([[0.17,0.96],
                  [0.17,1.07],
                  [0.20,1.07],
                  [0.20,0.96]])
        glEnd()
        
        # lines2
        glBegin(GL_POLYGON)
        glColor3f(241/255, 217/255, 167/255)
        self.draw([[0.10,0.96],
                  [0.10,1.07],
                  [0.13,1.07],
                  [0.13,0.96]])
        glEnd()
        
        # lines3
        glBegin(GL_POLYGON)
        glColor3f(241/255, 217/255, 167/255)
        self.draw([[0.03,0.96],
                  [0.03,1.07],
                  [0.06,1.07],
                  [0.06,0.96]])
        glEnd()
        
         # lines1
        glBegin(GL_POLYGON)
        glColor3f(241/255, 217/255, 167/255)
        self.draw([[-0.17,0.96],
                  [-0.17,1.07],
                  [-0.20,1.07],
                  [-0.20,0.96]])
        glEnd()
        
        # lines2
        glBegin(GL_POLYGON)
        glColor3f(241/255, 217/255, 167/255)
        self.draw([[-0.10,0.96],
                  [-0.10,1.07],
                  [-0.13,1.07],
                  [-0.13,0.96]])
        glEnd()
        
        # lines3
        glBegin(GL_POLYGON)
        glColor3f(241/255, 217/255, 167/255)
        self.draw([[-0.03,0.96],
                  [-0.03,1.07],
                  [-0.06,1.07],
                  [-0.06,0.96]])
        glEnd()   
    def block2(self):
        
        # big piece (half top)
        glBegin(GL_POLYGON)
        glColor3f(241/255, 228/255, 158/255)
        self.draw([[-0.37,0.2],
                  [-0.37,0.9],
                  [0.37,0.9],
                  [0.37,0.2]])
        glEnd()
        
        # big piece (half top, windows)
        glBegin(GL_POLYGON)
        glColor3f(82/255,150/255,241/255)
        self.draw([[0,0.45]])
        glColor3f(26/255, 104/255, 210/255)
        self.draw([[-0.26,0.2],
                  [-0.26,0.7],
                  [0.26,0.7],
                  [0.26,0.2],
                  [-0.26,0.2]])
        glEnd()
        
        # long horizontal window
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0,0.8]])
        glColor3f(26/255, 104/255, 210/255)
        self.draw([[-0.26,0.85],
                  [-0.26,0.75],
                  [0.26,0.75],
                  [0.26,0.85],
                  [-0.26,0.85]])
        glEnd()
        
        # lines1 (right)
        glBegin(GL_POLYGON)
        glColor3f(241/255, 228/255, 158/255)
        self.draw([[0.17,0.2],
                  [0.17,0.89],
                  [0.20,0.89],
                  [0.20,0.2]])
        glEnd()
        
        # lines2 (right)
        glBegin(GL_POLYGON)
        glColor3f(241/255, 228/255, 158/255)
        self.draw([[0.10,0.2],
                  [0.10,0.89],
                  [0.13,0.89],
                  [0.13,0.2]])
        glEnd()
        
        # lines3 (right)
        glBegin(GL_POLYGON)
        glColor3f(241/255, 228/255, 158/255)
        self.draw([[0.03,0.2],
                  [0.03,0.89],
                  [0.06,0.89],
                  [0.06,0.2]])
        glEnd()
        
         # lines1 (left)
        glBegin(GL_POLYGON)
        glColor3f(241/255, 228/255, 158/255)
        self.draw([[-0.17,0.2],
                  [-0.17,0.89],
                  [-0.20,0.89],
                  [-0.20,0.2]])
        glEnd()
        
        # lines2 (left)
        glBegin(GL_POLYGON)
        glColor3f(241/255, 228/255, 158/255)
        self.draw([[-0.10,0.2],
                  [-0.10,0.89],
                  [-0.13,0.89],
                  [-0.13,0.2]])
        glEnd()
        
        # lines3 (left)
        glBegin(GL_POLYGON)
        glColor3f(241/255, 228/255, 158/255)
        self.draw([[-0.03,0.2],
                  [-0.03,0.89],
                  [-0.06,0.89],
                  [-0.06,0.2]])
        glEnd()
        
        
        # right window1
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0.315,0.8]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[0.29,0.85],
                  [0.29,0.75],
                  [0.34,0.75],
                  [0.34,0.85],
                  [0.29,0.85]])
        glEnd()
        
        # right window2
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0.29,0.55],
                  [0.29,0.70],
                  [0.32,0.72],
                  [0.34,0.70],
                  [0.34,0.55]])
        glEnd()
        
        # right window3
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0.29,0.46],
                  [0.29,0.50],
                  [0.34,0.50],
                  [0.34,0.46]])
        glEnd()
        
        # right window4
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0.29,0.22],
                  [0.29,0.44],
                  [0.34,0.44],
                  [0.34,0.22]])
        glEnd()
        
        # left window1
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[-0.315,0.8]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[-0.29,0.85],
                  [-0.29,0.75],
                  [-0.34,0.75],
                  [-0.34,0.85],
                  [-0.29,0.85]])
        glEnd()
        
        # left window2
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[-0.29,0.55],
                  [-0.29,0.70],
                  [-0.32,0.72],
                  [-0.34,0.70],
                  [-0.34,0.55]])
        glEnd()
        
        # left window3
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[-0.29,0.46],
                  [-0.29,0.50],
                  [-0.34,0.50],
                  [-0.34,0.46]])
        glEnd()
        
        # left window4
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[-0.29,0.22],
                  [-0.29,0.44],
                  [-0.34,0.44],
                  [-0.34,0.22]])
        glEnd()
        
        # big piece (half middle)
        glBegin(GL_POLYGON)
        glColor3f(243/255, 187/255, 110/255)
        self.draw([[-0.37,-0.5],
                  [-0.37,0.2],
                  [0.37,0.2],
                  [0.37,-0.5]])
        glEnd()
        
        # window
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0,-0.15]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[-0.26,-0.4],
                  [-0.26,0.1],
                  [0.26,0.1],
                  [0.26,-0.4],
                  [-0.26,-0.4]])
        glEnd()
        
        # lines1 (right)
        glBegin(GL_POLYGON)
        glColor3f(243/255, 187/255, 110/255)
        self.draw([[0.17,-0.4],
                  [0.17,0.1],
                  [0.20,0.1],
                  [0.20,-0.4]])
        glEnd()
        
        # lines2 (right)
        glBegin(GL_POLYGON)
        glColor3f(243/255, 187/255, 110/255)
        self.draw([[0.10,-0.4],
                  [0.10,0.1],
                  [0.13,0.1],
                  [0.13,-0.4]])
        glEnd()
        
        # lines3 (right)
        glBegin(GL_POLYGON)
        glColor3f(243/255, 187/255, 110/255)
        self.draw([[0.03,-0.4],
                  [0.03,0.1],
                  [0.06,0.1],
                  [0.06,-0.4]])
        glEnd()
        
         # lines1 (left)
        glBegin(GL_POLYGON)
        glColor3f(243/255, 187/255, 110/255)
        self.draw([[-0.17,-0.4],
                  [-0.17,0.1],
                  [-0.20,0.1],
                  [-0.20,-0.4]])
        glEnd()
        
        # lines2 (left)
        glBegin(GL_POLYGON)
        glColor3f(243/255, 187/255, 110/255)
        self.draw([[-0.10,-0.4],
                  [-0.10,0.1],
                  [-0.13,0.1],
                  [-0.13,-0.4]])
        glEnd()
        
        # lines3 (left)
        glBegin(GL_POLYGON)
        glColor3f(243/255, 187/255, 110/255)
        self.draw([[-0.03,-0.4],
                  [-0.03,0.1],
                  [-0.06,0.1],
                  [-0.06,-0.4]])
        glEnd()
        
        # horizontal line
        glBegin(GL_POLYGON)
        glColor3f(243/255, 187/255, 110/255)
        self.draw([[-0.26,-0.30],
                  [-0.26,-0.25],
                  [0.26,-0.25],
                  [0.26,-0.30]])
        glEnd()
        
        # small window1 (right)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0.32,0.12],
                  [0.32,0.17],
                  [0.35,0.17],
                  [0.35,0.12]])
        glEnd()
        
        # small window2 (right)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0.28,0.12],
                  [0.28,0.17],
                  [0.31,0.17],
                  [0.31,0.12]])
        glEnd()
        
        # long window1 (right)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0.28,-0.4],
                  [0.28,0.10],
                  [0.31,0.10],
                  [0.31,-0.4]])
        glEnd()
        
        # long window2 (right)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0.32,-0.4],
                  [0.32,0.10],
                  [0.35,0.10],
                  [0.35,-0.4]])
        glEnd()
        
        # small window1 (left)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[-0.32,0.12],
                  [-0.32,0.17],
                  [-0.35,0.17],
                  [-0.35,0.12]])
        glEnd()
        
        # small window2 (left)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[-0.28,0.12],
                  [-0.28,0.17],
                  [-0.31,0.17],
                  [-0.31,0.12]])
        glEnd()
        
        # long window1 (left)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[-0.28,-0.4],
                  [-0.28,0.10],
                  [-0.31,0.10],
                  [-0.31,-0.4]])
        glEnd()
        
        # long window2 (left)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[-0.32,-0.4],
                  [-0.32,0.10],
                  [-0.35,0.10],
                  [-0.35,-0.4]])
        glEnd()
        
        # big piece (half bottom)
        glBegin(GL_POLYGON)
        glColor3f(205/255, 103/255, 76/255)
        self.draw([[-0.37,-1.1],
                  [-0.37,-0.4],
                  [0.37,-0.4],
                  [0.37,-1.1]])
        glEnd()
        
        # window
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0,-0.78]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[-0.26,-1.1],
                  [-0.26,-0.46],
                  [0.26,-0.46],
                  [0.26,-1.1],
                  [-0.26,-1.1]])
        glEnd()
        
        # lines1 (right)
        glBegin(GL_POLYGON)
        glColor3f(205/255, 103/255, 76/255)
        self.draw([[0.17,-1.1],
                  [0.17,-0.46],
                  [0.20,-0.46],
                  [0.20,-1.1]])
        glEnd()
        
        # lines2 (right)
        glBegin(GL_POLYGON)
        glColor3f(205/255, 103/255, 76/255)
        self.draw([[0.10,-1.1],
                  [0.10,-0.46],
                  [0.13,-0.46],
                  [0.13,-1.1]])
        glEnd()
        
        # lines3 (right)
        glBegin(GL_POLYGON)
        glColor3f(205/255, 103/255, 76/255)
        self.draw([[0.03,-1.1],
                  [0.03,-0.46],
                  [0.06,-0.46],
                  [0.06,-1.1]])
        glEnd()
        
        # long curve window (right)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0.32,-0.46]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[0.28,-0.8],
                  [0.28,-0.46],
                  [0.32,-0.44],
                  [0.35,-0.46],
                  [0.35,-0.8],
                  [0.28,-0.8]])
        glEnd()    
        
         # lines1 (left)
        glBegin(GL_POLYGON)
        glColor3f(205/255, 103/255, 76/255)
        self.draw([[-0.17,-1.1],
                  [-0.17,-0.46],
                  [-0.20,-0.46],
                  [-0.20,-1.1]])
        glEnd()
        
        # lines2 (left)
        glBegin(GL_POLYGON)
        glColor3f(205/255, 103/255, 76/255)
        self.draw([[-0.10,-1.1],
                  [-0.10,-0.46],
                  [-0.13,-0.46],
                  [-0.13,-1.1]])
        glEnd()
        
        # lines3 (left)
        glBegin(GL_POLYGON)
        glColor3f(205/255, 103/255, 76/255)
        self.draw([[-0.03,-1.1],
                  [-0.03,-0.46],
                  [-0.06,-0.46],
                  [-0.06,-1.1]])
        glEnd()
        
        # long curve window (left)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[-0.32,-0.46]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[-0.28,-0.8],
                  [-0.28,-0.46],
                  [-0.32,-0.44],
                  [-0.35,-0.46],
                  [-0.35,-0.8],
                  [-0.28,-0.8]])
        glEnd()       
    def block3(self):
        
        # bridge
        glBegin(GL_POLYGON)
        glColor3f(241/255, 228/255, 158/255)
        self.draw([[0.37,-1.1],
                  [0.37,-0.75],
                  [0.85,-0.75],
                  [0.85,-1.1]])
        glEnd()
        
        # bridge window1
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0.615,-0.95]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[0.59,-1.05],
                  [0.59,-0.80],
                  [0.66,-0.80],
                  [0.66,-1.05],
                  [0.59,-1.05]])
        glEnd()
        
        # bridge window2
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0.745,-0.95]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[0.71,-1.05],
                  [0.71,-0.80],
                  [0.78,-0.80],
                  [0.78,-1.05],
                  [0.71,-1.05]])
        glEnd()  
        
        # dome back body
        glBegin(GL_POLYGON)
        glColor3f(203/255, 95/255, 66/255)
        self.draw([[-0.53,-1.2],
                  [-0.53,-0.70],
                  [0.53,-0.70],
                  [0.53,-1.2]])
        glEnd()
        
        # dome back body window (right)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0.425,-0.87]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[0.37,-0.99],
                  [0.37,-0.75],
                  [0.48,-0.75],
                  [0.48,-0.99],
                  [0.37,-0.99]])
        glEnd()
        
        # dome back body window (left)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[-0.425,-0.87]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[-0.37,-0.99],
                  [-0.37,-0.75],
                  [-0.48,-0.75],
                  [-0.48,-0.99],
                  [-0.37,-0.99]])
        glEnd()
        
        # 2nd dome
        glBegin(GL_POLYGON)
        glColor3f(255/255, 255/255, 230/255)
        glEnd()
        self.drawCircle(0,-0.92, radius = 0.27)
        glEnd()
        
        # 2nd dome body
        glBegin(GL_POLYGON)
        glColor3f(115/255, 110/255, 101/255)
        self.draw([[-0.47,-1.2],
                  [-0.47,-0.95],
                  [0.47,-0.95],
                  [0.47,-1.2]])
        glEnd() 
        
        # 2nd dome sharp small bottom piece
        glBegin(GL_POLYGON)
        glColor3f(241/255, 217/255, 167/255)
        self.draw([[-0.036,-0.65],
                  [-0.036,-0.62],
                  [0.036,-0.62],
                  [0.036,-0.65]])
        glEnd()
        
        # 2nd dome bottom piece2
        glBegin(GL_POLYGON)
        glColor3f(241/255, 217/255, 167/255)
        self.draw([[-0.27,-0.95],
                  [-0.27,-0.89],
                  [0.27,-0.89],
                  [0.27,-0.95]])
        glEnd()
        
        # 2nd dome bottom piece1
        glBegin(GL_POLYGON)
        glColor3f(241/255, 228/255, 158/255)
        self.draw([[-0.27,-0.89],
                  [-0.3,-0.84],
                  [0.3,-0.84],
                  [0.27,-0.89]])
        glEnd()
        
        # 2nd dome sharp top
        glBegin(GL_POLYGON)
        glColor3f(255/255, 255/255, 230/255)
        self.draw([[-0.032,-0.62],
                  [0,-0.38],
                  [0.032,-0.62]])
        glEnd()
    def block4(self):
        
        # side building (bottom part)
        glBegin(GL_POLYGON)
        glColor3f(203/255, 95/255, 66/255)
        self.draw([[0.85,-1.15],
                  [0.85,-0.70],
                  [1.5,-0.70],
                  [1.5,-1.15]])
        glEnd()
        
        # side building floor
        glBegin(GL_POLYGON)
        glColor3f(134/255, 129/255, 121/255)
        self.draw([[0.85,-1.15],
                  [0.85,-0.99],
                  [1.5,-0.99],
                  [1.5,-1.15]])
        glEnd()
        
        # side building bottom window1
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0.945,-0.865]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[0.89,-0.98],
                  [0.89,-0.75],
                  [1,-0.75],
                  [1,-0.98],
                  [0.89,-0.98]])
        glEnd()
        
        # side building bottom window2
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[1.405,-0.865]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[1.35,-0.98],
                  [1.35,-0.75],
                  [1.46,-0.75],
                  [1.46,-0.98],
                  [1.35,-0.98]])
        glEnd()
        
        # side building bottom hiasan1
        glBegin(GL_POLYGON)
        glColor3f(243/255, 187/255, 110/255)
        self.draw([[1.05,-0.99],
                  [1.05,-0.71],
                  [1.1,-0.71],
                  [1.1,-0.99]])
        glEnd()
        
        # side building bottom hiasan2
        glBegin(GL_POLYGON)
        glColor3f(243/255, 187/255, 110/255)
        self.draw([[1.25,-0.99],
                  [1.25,-0.71],
                  [1.3,-0.71],
                  [1.3,-0.99]])
        glEnd()
        
        # side building door
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[1.17,-1.075]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[1.08,-1.15],
                  [1.08,-1],
                  [1.26,-1],
                  [1.26,-1.15],
                  [1.08,-1.15]])
        glEnd()
        
        # door roof
        glBegin(GL_POLYGON)
        glColor3f(174/255, 155/255, 124/255)
        self.draw([[0.97,-1.05],
                  [0.97,-0.98],
                  [1.37,-0.98],
                  [1.37,-1.05]])
        glEnd()
        
        # door roof top
        glBegin(GL_POLYGON)
        glColor3f(241/255, 228/255, 158/255)
        self.draw([[0.94,-1.02],
                  [1.18,-0.92],
                  [1.40,-1.02]])
        glEnd()
        
        # side building (left part)
        glBegin(GL_POLYGON)
        glColor3f(241/255, 228/255, 158/255)
        self.draw([[0.85,-0.70],
                  [0.85,-0.35],
                  [1.25,-0.35],
                  [1.25,-0.70]])
        glEnd()
        
        # tiny hiasan1
        glBegin(GL_POLYGON)
        glColor3f(174/255, 155/255, 124/255)
        self.draw([[0.87,-0.52],
                  [0.87,-0.43],
                  [0.91,-0.43],
                  [0.91,-0.52]])
        glEnd()
         
        # tiny hiasan2
        glBegin(GL_POLYGON)
        glColor3f(174/255, 155/255, 124/255)
        self.draw([[0.87,-0.67],
                  [0.87,-0.55],
                  [0.91,-0.55],
                  [0.91,-0.67]])
        glEnd()
         
        # side building (left part, edge)
        glBegin(GL_POLYGON)
        glColor3f(163/255, 140/255, 78/255)
        self.draw([[0.84,-0.39],
                  [0.84,-0.34],
                  [1.25,-0.34],
                  [1.25,-0.39]])
        glEnd()
        
        # side building (right part)
        glBegin(GL_POLYGON)
        glColor3f(220/255, 203/255, 159/255)
        self.draw([[1.25,-0.70],
                  [1.25,-0.35],
                  [1.50,-0.35],
                  [1.50,-0.70]])
        glEnd()
        
        # side building (right part, edge)
        glBegin(GL_POLYGON)
        glColor3f(185/255, 168/255, 123/255)
        self.draw([[1.23,-0.39],
                  [1.23,-0.33],
                  [1.52,-0.33],
                  [1.52,-0.39]])
        glEnd()
        
        # side building (middle part, top)
        glBegin(GL_POLYGON)
        glColor3f(204/255, 173/255, 124/255)
        self.draw([[0.935,-0.44],
                  [0.935,-0.40],
                  [1.25,-0.40],
                  [1.25,-0.44]])
        glEnd()
        
        # side building (middle part, bottom)
        glBegin(GL_POLYGON)
        glColor3f(204/255, 173/255, 124/255)
        self.draw([[0.935,-0.70],
                  [0.935,-0.52],
                  [1.25,-0.52],
                  [1.25,-0.70]])
        glEnd()
    def block5(self):
        
        # 3rd dome
        glBegin(GL_POLYGON)
        glColor3f(255/255, 255/255, 230/255)
        glEnd()
        self.drawCircle(0,-1.02, radius = 0.15)
        glEnd()
        
        # 3rd dome body 
        glBegin(GL_POLYGON)
        glColor3f(171/255, 138/255, 82/255)
        self.draw([[-0.27,-1.2],
                  [-0.27,-0.99],
                  [0.27,-0.99],
                  [0.27,-1.2]])
        glEnd() 
        
        # 3rd dome piece
        glBegin(GL_POLYGON)
        glColor3f(241/255, 228/255, 158/255)
        self.draw([[-0.14,-1.2],
                  [-0.14,-0.95],
                  [0.14,-0.95],
                  [0.14,-1.2]])
        glEnd() 
        
        # 3rd dome sharp piece holder
        glBegin(GL_POLYGON)
        glColor3f(174/255, 155/255, 124/255)
        self.draw([[-0.02,-0.87],
                  [-0.02,-0.85],
                  [0.02,-0.85],
                  [0.02,-0.87]])
        glEnd() 
        
        # 3rd dome sharp piece
        glBegin(GL_POLYGON)
        glColor3f(255/255, 255/255, 230/255)
        self.draw([[-0.02,-0.85],
                  [0.02,-0.85],
                  [0,-0.77]])
        glEnd() 
        
        # door
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[-0.065,-1.095]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[-0.13,-1.2],
                  [-0.13,-0.99],
                  [0,-0.99],
                  [0,-1.2],
                  [-0.13,-1.2]])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[0.065,-1.095]])
        glColor3f(26/255,104/255,210/255)          
        self.draw([[0,-1.2],
                  [0,-0.99],
                  [0.13,-0.99],
                  [0.13,-1.2],
                  [0,-1.2]])
        glEnd() 
        
        # tiang
        glBegin(GL_POLYGON)
        glColor3f(241/255, 228/255, 158/255)
        self.draw([[-0.25,-1.2],
                  [-0.25,-0.99],          
                  [-0.21,-0.99],
                  [-0.21,-1.2]])
        glEnd()  
        
        # gerbang edge
        glBegin(GL_POLYGON)
        glColor3f(174/255, 155/255, 124/255)
        self.draw([[-0.27,-1.05],
                  [-0.27,-0.98],
                  [0.27,-0.98],
                  [0.27,-1.05]])
        glEnd() 
        
        # side building (middle part, window1)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[1.1,-0.48]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[0.95,-0.52],
                  [0.95,-0.44],
                  [1.25,-0.44],
                  [1.25,-0.52],
                  [0.95,-0.52]])
        glEnd()
        
        
        # side building (window divider1)
        glBegin(GL_POLYGON)
        glColor3f(204/255, 173/255, 124/255)
        self.draw([[1,-0.52],
                  [1,-0.44],
                  [1.02,-0.44],
                  [1.02,-0.52]])
        glEnd()
        
        # side building (window divider2)
        glBegin(GL_POLYGON)
        glColor3f(204/255, 173/255, 124/255)
        self.draw([[1.08,-0.52],
                  [1.08,-0.44],
                  [1.10,-0.44],
                  [1.10,-0.52]])
        glEnd()
        
        # side building (window divider3)
        glBegin(GL_POLYGON)
        glColor3f(204/255, 173/255, 124/255)
        self.draw([[1.16,-0.52],
                  [1.16,-0.44],
                  [1.18,-0.44],
                  [1.18,-0.52]])
        glEnd()
        
        
        # side building (middle part, bottom window1)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[1.01,-0.61]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[0.98,-0.68],
                  [0.98,-0.54],
                  [1.04,-0.54],
                  [1.04,-0.68],
                  [0.98,-0.68]])
        glEnd()
        
         # side building (middle part, bottom window2)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[1.09,-0.61]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[1.06,-0.68],
                  [1.06,-0.54],
                  [1.12,-0.54],
                  [1.12,-0.68],
                  [1.06,-0.68]])
        glEnd()
        
         # side building (middle part, bottom window3)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[1.17,-0.61]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[1.14,-0.68],
                  [1.14,-0.54],
                  [1.2,-0.54],
                  [1.2,-0.68],
                  [1.14,-0.68]])
        glEnd()
        
        # side building (right part window)
        glBegin(GL_POLYGON)
        glColor3f(82/255, 150/255, 241/255)
        self.draw([[1.375,-0.585]])
        glColor3f(26/255,104/255,210/255)
        self.draw([[1.31,-0.70],
                  [1.31,-0.47],
                  [1.375,-0.40],
                  [1.44,-0.47],
                  [1.44,-0.70],
                  [1.31,-0.70]])
        glEnd()
    def word(self):
        
        glBegin(GL_POLYGON)
        glColor3f(240/255, 137/255, 28/255)
        self.draw([[-0.79,-1.87],
                  [-0.79,-1.36],
                  [0.79,-1.36],
                  [0.79,-1.87]])
        glEnd() 
        
        glBegin(GL_POLYGON)
        glColor3f(232/255, 58/255, 30/255)
        self.draw([[-0.75,-1.8],
                  [-0.75,-1.4],
                  [0.75,-1.4],
                  [0.75,-1.8]])
        glEnd() 
        
        glColor3f(0,0,0)
        glRasterPos2f(-0.62,-1.63)
        glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24,b"SABAH MAJU JAYA")  
        
    def tiang(self):
        glBegin(GL_POLYGON)
        glColor3f(241/255, 228/255, 158/255)
        self.draw([[-0.25,-1.2],
                  [-0.25,-1.045],          
                  [-0.21,-1.045],
                  [-0.21,-1.2]])
        glEnd()    
    def movetiang(self): # function to perform translation transformation
         glTranslatef(-0.06,0,0)
         self.tiang()
         glTranslatef(-0.34,0,0)
         self.tiang()
         glTranslatef(-0.055,0,0)
         self.tiang()
         glTranslatef(-0.84,0.05,0)
         self.tiang()
         glTranslatef(-0.22,0,0)
         self.tiang()
         glTranslatef(-0.05,0,0)
         self.tiang()
         glTranslatef(0.32,0,0)
         self.tiang()
         glTranslatef(2.03,0,0)
         self.tiang()
         glTranslatef(0.05,0,0)
         self.tiang()
         glTranslatef(0.21,0,0)
         self.tiang()
         glTranslatef(0.05,0,0)
         self.tiang()
   

    def draw(self, vertex):
        # to set a coordinate of x and y
        # to create any polygon with any number of sides
        for i in range(len(vertex)):
            x = self.flip*vertex[i][00]
            y = vertex[i][1]
            glVertex2f(x, y)     
    def drawCircle(self, posx=0, posy=0, radius=1):
        # to draw a circle
        side = 99
        glBegin(GL_POLYGON)
        for i in range (100):
            cosine = radius*math.cos(i*2*math.pi/side) + posx
            sine = radius*math.sin(i*2*math.pi/side) + posy
            self.draw([[cosine,sine]])
    
    
    def initScene(self):
        glClearColor(1, 1, 1, 1) #clear the color of the window
        glClearDepth(1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

    def drawScene(self): # creates the building and the background 
        self.Menara()
        self.movetiang()
        
    
    def display(self):
        self.initScene()
        glLoadIdentity()
        gluLookAt(0, 1.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0) #set the camera angle
        self.drawScene()
        glutSwapBuffers()
        
    def keyPressed(self,*args): # set certain key to press to exit
        if args[0] == b'e':
            os._exit()
        if args[0] == b'E':
            os._exit()
        glutPostRedisplay()

    def reshape(self,width,height):
        width=self.width
        height=self.height
        if height == 0:
            height=1

        glViewport(0,0,(int)(width),(int)(height))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (float)(width)/(float)(height),0.1,100.0)
        glMatrixMode(GL_MODELVIEW)

    def sceneLoop(self):
        glutInit(sys.argv) #initialize the program.
        glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH) #set up a basic display buffer(only singular for now)
        glutInitWindowSize(self.width, self.height)  # window size
        glutInitWindowPosition(0, 0)  # window position
        glutCreateWindow(b"MENARA KINABALU")  # show window
        glutDisplayFunc(self.display)  # draw callback function call the display function to draw our world
        glutReshapeFunc(self.reshape)  # resize callback function
        glutIdleFunc(self.display)
        glutKeyboardFunc(self.keyPressed)
        glutMainLoop() # initialize the OpenGL loop cycle

def main():
    myCg=myGraphics()
    myCg.sceneLoop()

if __name__ == "__main__":
    main()
