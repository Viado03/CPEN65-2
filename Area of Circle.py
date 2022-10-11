class Circle:                   #Circle aa the class name
  def __init__(self, radius):   #Radius as the Attribute
    self.radius = radius

  def Area(self):         #Area() as the Method
    return (3.14 *(self.radius * self.radius))

input_area = float(input("Input radius: "))
radius1 = Circle(input_area)  #radius1 as the object name

print("The area of a cirle is",round(radius1.Area(),3))

