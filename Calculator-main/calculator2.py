print("Welcome to the Python Calculator! (v2.4)")
# new version created 12:50 PM 3/19/2024
import math
import cmath
import random
e = math.e
inf = math.inf
nan = math.nan
pi = math.pi
tau = math.tau
def devloop():
  pass
  
def sine():
  x = float(input("Sine of: "))
  print(math.sin(x))
def cosine():
  x = float(input("Cosine of: "))
  print(math.cos(x))
def tangent():
  x = float(input("Tangent of: "))
  print(math.tan(x))
def cosecant():
  x = float(input("Cosecant of: "))
  print(1/(math.sin(x)))
def secant():
  x = float(input("Secant of: "))
  print(1/(math.cos(x)))
def cotangent():
  x = float(input("Cotangent of: "))
  print(1/(math.tan(x)))
def arcsin():
  x = float(input("Inverse sine of: "))
  print(math.asin(x))
def arccos():
  x = float(input("Inverse cosine of: "))
  print(math.acos(x))
def arctan():
  x = float(input("Inverse tangent of: "))
  print(math.atan(x))
def arccsc():
  x = float(input("Inverse cosecant of: "))
  print(math.asin(1/x))
def arcsec():
  x = float(input("Inverse secant of: "))
  print(math.acos(1/x))
def arccot():
  x = float(input("Inverse cotangent of: "))
  print(math.atan(1/x))
def sinh():
  x = float(input("Hyperbolic sine of: "))
  print(math.sinh(x))
def cosh():
  x = float(input("Hyperbolic cosine of: "))
  print(math.cosh(x))
def tanh():
  x = float(input("Hyperbolic tangent of: "))
  print(math.tanh(x))
def csch():
  x = float(input("Hyperbolic cosecant of: "))
  print((1/math.sinh(x)))
def sech():
  x = float(input("Hyperbolic secant of: "))
  print((1/math.cosh(x)))
def coth():
  x = float(input("Hyperbolic cotangent of: "))
  print((1/math.tanh(x)))
def asinh():
  x = float(input("Inverse hyperbolic sine of: "))
  print(math.asinh(x))
def acosh():
  x = float(input("Inverse hyperbolic cosine of: "))
  print(math.acosh(x))
def atanh():
  x = float(input("Inverse hyperbolic tangent of: "))
  print(math.atanh(x))
def acsch():
  x = float(input("Inverse hyperbolic cosecant of: "))
  print(math.asinh(1/x))
def asech():
  x = float(input("Inverse hyperbolic secant of: "))
  print(math.acosh(1/x))
def acoth():
  x = float(input("Inverse hyperbolic cotangent of: "))
  print(math.atanh(1/x))
def comb():
  n = int(input("Number of items to choose from: "))
  k = int(input("Number of possibilities to choose: "))
  print(math.comb(n, k))
def perm():
  n = int(input("Number of items to choose from: "))
  k = int(input("(Optional) Number of items to choose: "))
  print(math.perm(n, k))
def atan2():
  x = float(input("X (Denominator):\n")
  y = float(input("Y (Numerator):\n")
  print(math.atan2(y, x))
def cbrt():
  x = float(input("Square root of: ")
  print(math.cbrt(x))
def ceil():
  x = float(input("Round up: ")
  print(math.ceil(x))
def copysign():
  x = float(input("Number to copy:\n")
  y = float(input("Use sign of:\n")
  print(math.copysign(x, y)
def degrees():
  x = float(input("Radians to degrees: ")
  print(math.degrees(x))
def erf():
  x = float(input("Error function at: ")
  print(math.erf(x))
def erfc():
  x = float(input("Complementary error function at: ")
  print(math.erfc(x))
def exp():
  x = float(input("E raised to power of: ")
  print(math.exp(x))
def exp2():
  x = float(input("2 raised to the power of: ")
  print(math.exp2(x))
def expm1():
  x = float(input("E raised to the power of: (minus 1)\n")
  print(expm1(x))
#6:56 PM 3/23/2024
def fabs():
  x = float(input("Absolute value of: ")
  print(math.fabs(x))
def floor():
  x = float(input("Round down: ")
  print(math.floor(x))
def fmod():
  x = float(input("Numerator/Dividend:\n")
  y = float(input("Denominator/Divisor:\n")
  print(math.fmod(x, y))
def frexp():
  x = float(input("Mantissa and exponent of: ")
  print(math.frexp(x))
def fsum():
  seq = input("Sum of: (format [a, b, c, ...]")
  seq = [float(x) for x in seq.strip('[]').split(',')]
  print(math.fsum(seq))
def gamma():
  x = float(input("Gamma function at: ")
  print(math.gamma(x))
def gcd():
  seq = int(input("Greatest common divisor of: [a, b, ...]"))
  seq = [float(x) for x in seq.strip('[]').split(',')]
  print(math.gcd(seq))
def hypot():
  x = float(input("Length of first leg:\n")
  y = float(input("Length of second leg:\n")
  print(math.hypot(x, y))
#9:32 PM 3/23/2024


def funstuff():
  print("Oooh, what shall it be today? Here's a list of all the advanced operations:")
  print('''Square root (sqrt)\nReturn value of pi (pi)\nReturn value of Euler's constant (e)\nReturn value of tau (tau)\nReturn value of infinity (inf)\nReturn value of Not a Number (nan)\nRandom number generator (rand)\nFactorial (fact)\nQuadratic formula (quad)\nDistance formula (dist)\nArea (area)\nTrigonometric functions (sin, cos, tan, csc, sec, cot, asin, acos, atan, acsc, asec, acot,\nsinh, cosh, tanh, csch, sech, coth, asinh, acosh, atanh, acsch, asech, acoth)\nCombinations (comb)\nPermutations (perm)\n''')
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
  elif choice == "sin":
    sine()
  elif choice == "cos":
    cosine()
  elif choice == "tan":
    tangent()
  elif choice == "csc":
    cosecant()
  elif choice == "sec":
    secant()
  elif choice == "cot":
    cotangent()
  elif choice == "asin":
    arcsin()
  elif choice == "acos":
    arccos()
  elif choice == "atan":
    arctan()
  elif choice == "acsc":
    arcsc()
  elif choice == "asec":
    arcsec()
  elif choice == "acot":
    arccot()
  elif choice == "sinh":
    sinh()
  elif choice == "cosh":
    cosh()
  elif choice == "tanh":
    tanh()
  elif choice == "csch":
    csch()
  elif choice == "sech":
    sech()
  elif choice == "coth":
    coth()
  elif choice == "asinh":
    asinh()
  elif choice == "acosh":
    acosh()
  elif choice == "atanh":
    atanh()
  elif choice == "acsch":
    acsch()
  elif choice == "asech":
    asech()
  elif choice == "acoth":
    acoth()
  elif choice == "sqrt":
    num = float(input("Square root of: "))
    print(math.sqrt(num))
  elif choice == "pi":
    print(pi)
  elif choice == "e":
    print(e)
  elif choice == "inf":
    print(inf)
  elif choice == "nan":
    print(nan)
  elif choice == "tau":
    print(tau)
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
  elif choice == "comb":
    comb()
  elif choice == "perm":
    perm()
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
  elif operation == "devloop":
    devloop()
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