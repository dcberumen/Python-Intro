#/usr/bin/env python3.3
#   Course      CPSC 223p
#   Assignment  3 classes
#

from math import *
#two-dimensional cartesian coordinate
# class definition here
class Cartesian2D:
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
        
    def x(self):
        return self._x
        
    def x(self,value):
        self._x = value
        
    def y(self):
        return self._y
        
    def y(self,value):
        self._y = value
        
    def setprec(self,number):
      	return round(number,2)
    
    def distanceTo(self,point):
        return self.setprec(sqrt((point.x - self.x)**2 + (point.y - self.y)**2))
        
    def __add__(self,point):
        return Cartesian2D(self.x+point.x, self.y+point.y)
        
    def __repr__(self):
      	return 'Cartesian2D({0.x:0.2f},{0.y:0.2f})'.format(self)
      	
    def __sub__(self,point):
        return Cartesian2D(self.x-point.x, self.y-point.y)
        
    def __mul__(self,num):
        return Cartesian2D(self.x*num, self.y*num)
        
    def length(self):
        return self.setprec(sqrt(self.x**2+self.y**2))
        
    def normalize(self):
        return Cartesian2D(self.x/self.length(), self.y/self.length())
      	
def dot(v1,v2):
	return '{0:.2f}'.format((v1.x * v2.x) + (v1.y * v2.y))
    
def main( ):
    a = Cartesian2D(2.3,3.4)
    b = Cartesian2D(4.5,1.8)
    c = Cartesian2D(8.1,0.3)
    print("The distance from a to b is {}".format(a.distanceTo(b)))
    print("The distance from b to c is {}".format(b.distanceTo(c)))
    d = a + b
    print("a+b = ({},{})".format(d.x,d.y))
    d = c-b
    print("c-b = ({},{})".format(d.x,d.y))
    print("The length of a is {}".format(a.length()))
    print("The length of b is {}".format(b.length()))
    print("The length of c is {}".format(c.length()))
    #the normalize methof returns a unit length of a vector
    unita = a.normalize()
    unitb = b.normalize()
    unitc = c.normalize()
    print("The length of unit a is {}".format(unita.length()))
    print("The length of unit b is {}".format(unitb.length()))
    print("The length of unit c is {}".format(unitc.length()))
    if a == b:
        print('Somehow a is equal to b?')
    else:
        print('a is not equal to b')
        
    s = 4
    d = unita * s
    print(d)
    print("the length of d is {}".format(d.length()))
    e = unitb * s
    f = dot(a,b)
    g = dot(unita, unitb)
    h = dot(d,e)
    print("dot(a,b) = {}".format(f))
    print("dot(unita,unitb = {}".format(g))
    print("dot(d,e) = {}".format(h))
    
    
if __name__=="__main__":
    main( )
