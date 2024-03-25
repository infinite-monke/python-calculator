print("Welcome to the Python Calculator! (v2.0)")

import math
import cmath
import random
def funstuff():
  print("Oooh, what shall it be today? Here's a list of all the advanced operations:")
  print('''Square root (sqrt)\nReturn value of pi (pi)\nReturn value of Euler's constant (e)\nRandom number generator (rand)\nFactorial (fact)\nQuadratic formula (quad)\nDistance formula (dist)\nArea (area)''')
  choice = input("\n")
  if choice == "quad":
    a = float(input("A:"))
    b = float(input("B:"))
    c = float(input("C:"))
    print("Plus shown first, then minus, as complex numbers.")
    print(((-b + cmath.sqrt((b ** 2) - (4 * a * c)))/(2 * a)))
    print(((-b - cmath.sqrt((b ** 2) - (4 * a * c)))/(2 * a)))
  elif choice == "fact":
    num = int(input("Factorial of: "))
    print(math.factorial(num))
  elif choice == "pi":
    print(math.pi)
  elif choice == "sqrt":
    num = float(input("Square root of: "))
    print(math.sqrt(num))
  elif choice == "e":
    print(math.e)
  elif choice == "dist":
    p = input("First point: (x, y)\n")
    q = input("Second point: (x, y)\n")
    p = [float(x) for x in p.strip('()').split(',')]
    q = [float(x) for x in q.strip('()').split(',')]
    print(math.dist(p, q))
  elif choice == "area":
    shape = input("Name your shape.\n")
    if shape == "square":
      s = float(input("Síde length:\n"))
      print(s ** 2)
    elif shape == "triangle":
      b = float(input("Base length:\n"))
      h = float(input("Height:\n"))
      print(0.5 * b * h)
    elif shape == "rectangle":
      s1 = float(input("Side length:\n"))
      s2 = float(input("Other side length:\n"))
      print(s1 * s2)
    elif shape == "circle":
      pi = math.pi
      r = float(input("Radius:\n"))
      print(pi * (r ** 2))
    elif shape == "trapezoid":
      h = float(input("Height:\n"))
      b1 = float(input("Base:\n"))
      b2 = float(input("Other base:\n"))
      print(0.5 * h * (b1 + b2))
    elif shape == "hexagon":
      s = float(input("Side length:"))
      print((3 * math.sqrt(3) * s ** 2) / 2)
    elif shape == "pentagon":
      s = float(input("Side length:"))
      print((1.25 * math.sqrt(1 + (2/math.sqrt(5))) * s ** 2))
    else:
      print("Sorry, unsupported shape at the moment. The next version will have it, though, thanks to you!")
  elif choice == "rand":
    min = float(input("Minimum number:\n"))
    max = float(input("Maximum number:\n"))
    print(random.uniform(min, max))
def calculator():
  operation = input("Pick an operation: add, subtract, multiply, divide, or exponent?\n")
  if operation == "add":
    num1 = float(input("First number:\n"))
    num2 = float(input("Second number:\n"))
    print(num1 + num2)
  elif operation == "subtract":
    num1 = float(input("First number:\n"))
    num2 = float(input("Second number:\n"))
    print(num1 - num2)
  elif operation == "multiply":
    num1 = float(input("First number:\n"))
    num2 = float(input("Second number:\n"))
    print(num1 * num2)
  elif operation == "divide":
    num1 = float(input("First number:\n"))
    num2 = float(input("Second number:\n"))
    print(num1 / num2)
  elif operation == "exponent":
    num1 = float(input("Base:\n"))
    num2 = float(input("Exponent:\n"))
    print(num1 ** num2)
  elif operation == "MORE":
    funstuff()
  else:
    print("Input not recognized. For more advanced operations, type \"MORE.\"")
    calculator()
  global yn 
  yn = input("Got more operations? (y/n)\n")
calculator() 
while yn == "y":
    calculator()
if yn != "y":
  print("All done!")