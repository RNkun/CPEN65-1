import math

unknown = str(input("Determine the value whether it is in diameter or in radius: "))
value = float(input("Input the value here: "))


class Circle:
  def Area(self):
    if unknown == "radius":
      rad = value**2*(math.pi)
      print("The area of the circle given its radius is ", rad)
      print("Thank you for using the Program.")
    elif unknown == "diameter":
      diam = value**2*(math.pi)*0.25
      print("The area of the circle given its diameter is ", diam)
      print("Thank you for using the Program.")
    else:
      print("Syntax Error")
      print("Thank you for using the Program.")

Circle.Area(0)
