class Polygon:
    def __init__(self,no_of_sides):
        self.nosides=no_of_sides
        self.sides=[0 for i in range(0,self.nosides)]
    def inputSides(self):
        self.sides=[float(input("side : ")) for i in range(self.nosides)]
    def despSides(self):
        for i in self.sides:
            print("sides : ",i)

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    def findArea(self):
        a,b,c=self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %f' %area)

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)
    def RectangleArea(self):
        d,e=self.sides
        recarea=d*e
        print("Area of rectangle is %f" %recarea)
class Square(Polygon):
    def __init__(self):
        Polygon.__init__(self,1)
    def SquareArea(self):
        g=self.sides
        
        squarearea=g[0]*g[0]
        print("Area of Square is %f" %squarearea)
        
        

p=Triangle()
p.inputSides()
p.despSides()
p.findArea()

q=Rectangle()
q.inputSides()
q.despSides()
q.RectangleArea()

r=Square()
r.inputSides()
r.despSides()
r.SquareArea()


