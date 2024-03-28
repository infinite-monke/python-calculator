print("Welcome to the Python Calculator! (v2.5)")
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
  print("Nice try, but there's nothing here yet. You probably knew that, though ;-P")
  
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
  x = float(input("X (Denominator):\n"))
  y = float(input("Y (Numerator):\n"))
  print(math.atan2(y, x))
def cbrt():
  x = float(input("Square root of: "))
  print(math.cbrt(x))
def ceil():
  x = float(input("Round up: "))
  print(math.ceil(x))
def copysign():
  x = float(input("Number to copy:\n"))
  y = float(input("Use sign of:\n"))
  print(math.copysign(x, y))
def degrees():
  x = float(input("Radians to degrees: "))
  print(math.degrees(x))
def erf():
  x = float(input("Error function at: "))
  print(math.erf(x))
def erfc():
  x = float(input("Complementary error function at: "))
  print(math.erfc(x))
def exp():
  x = float(input("E raised to power of: "))
  print(math.exp(x))
def exp2():
  x = float(input("2 raised to the power of: "))
  print(math.exp2(x))
def expm1():
  x = float(input("E raised to the power of: (minus 1)\n"))
  print(expm1(x))
#6:56 PM 3/23/2024
def fabs():
  x = float(input("Absolute value of: "))
  print(math.fabs(x))
def floor():
  x = float(input("Round down: "))
  print(math.floor(x))
def fmod():
  x = float(input("Numerator/Dividend:\n"))
  y = float(input("Denominator/Divisor:\n"))
  print(math.fmod(x, y))
def frexp():
  x = float(input("Mantissa and exponent of: "))
  print(math.frexp(x))
def fsum():
  seq = input("Sum of: (format [a, b, c, ...]")
  seq = [float(x) for x in seq.strip('[]').split(',')]
  print(math.fsum(seq))
def gamma():
  x = float(input("Gamma function at: "))
  print(math.gamma(x))
def gcd():
  seq = int(input("Greatest common divisor of: [a, b, ...]"))
  seq = [float(x) for x in seq.strip('[]').split(',')]
  print(math.gcd(seq))
def hypot():
  x = float(input("Length of first leg:\n"))
  y = float(input("Length of second leg:\n"))
  print(math.hypot(x, y))
#9:32 PM 3/23/2024
#7:10 PM 3/24/2024
def isclose():
  x = float(input("First number:\n"))
  y = float(input("Second number:\n"))
  output = math.isclose(x, y)
  if output == True:
    print("Yes")
  if output == False:
    print("No")
def isnumber():
  x = float(input("Number to test:\n"))
  y = math.isnan(x)
  if y == True:
    print("Value is not a number (NaN)")
  elif y == False:
    print("Value is a number...")
  z = math.isinf(x)
  if z == True:
    print("Value is infinite.")
  elif z == False:
    print("Value is not infinite...")
  a = math.isfinite(x)
  if a == True:
    print("Value is a finite number.")
  else:
    print("Input not recognized.")
def isqrt():
  x = int(input("Integer part of sqrt of: "))
  print(math.isqrt(x))
def lcm():
  seq = int(input("Least common multiple of: (Format [a, b, c...])\n"))
  seq = [float(x) for x in seq.strip('[]').split(',')]
  print(math.lcm(seq))
def ldexp():
  x = float(input("Multiplier:"))
  i = float(input("Exponent:"))
  print(math.ldexp(x, i))
def lgamma():
  x = float(input("Natural log of abs value of gamma function at:\n"))
  print(math.lgamma(x))
def log():
  x = float(input("Log of: "))
  b = float(input("Base: "))
  print(math.log(x, base=b))
def log10():
  x = float(input("Log base 10 of: "))
  print(math.log10(x))
def log1p():
  x = float(input("Natural log of 1 +: "))
  print(math.log1p(x))
def log2():
  x = float(input("Log base 2 of: "))
  print(math.log2(x))
def modf():
  x = float(input("Return fractional and integer parts of: "))
  print(math.modf(x))
def nextafter():
  x = float(input("Steps after: "))
  y = float(input("Steps towards: "))
  s = int(input("Number of steps: "))
  print(math.nextafter(x, y, steps=s))
def pow():
  x = float(input("Base: "))
  y = float(input("Exponent: "))
def prod():
  seq = float(input("Product of all numbers (format [a, b, c...])\n"))
  seq = [float(x) for x in seq.strip('[]').split(',')]
  print(math.prod(seq))
def rad():
  x = float(input("Convert degrees to radians: "))
  print(math.radians(x))
def rem():
  x = float(input("Numerator/dividend:\n"))
  y = float(input("Denominator/divisor:\n"))
  print(math.remainder(x, y))
def sumprod():
  p = float(input("List 1 of numbers to multiply (format [a, c, c...]):\n"))
  q = float(input("List 2 of numbers to multiply (format [a, b, c...]): \n"))
  p = [float(x) for x in p.strip('[]').split(',')]
  q = [float(x) for x in q.strip('[]').split(',')]
  print(math.sumprod(p, q))
def trunc():
  x = float(input("Truncate: "))
  print(math.trunc(x))
def ulp():
  x = float(input("Least significant bit of: "))
  print(math.ulp(x))
def funstuff():
  print("Oooh, what shall it be today? Here's a list of all the advanced operations:")
  print('''Square root (sqrt)\nReturn value of pi (pi)\nReturn value of Euler's constant (e)\nReturn value of tau (tau)\nReturn value of infinity (inf)\nReturn value of Not a Number (nan)\nRandom number generator (rand)\nFactorial (fact)\nQuadratic formula (quad)\nDistance formula (dist)\nArea (area)\nTrigonometric functions (sin, cos, tan, csc, sec, cot, asin, acos, atan, acsc, asec, acot,\nsinh, cosh, tanh, csch, sech, coth, asinh, acosh, atanh, acsch, asech, acoth)\nCombinations (comb)\nPermutations (perm)\nReturn arc tangent of y/x (atan2)\nReturn cube root of x (cbrt)\nReturn ceiling of x as an integral (ceil)\nReturn float with value of x and sign of y (copysign)\nConvert angle from radians to degrees (degrees)\nError function at x (erf)\nComplementary error function at x (erfc)\nReturn e raised to x (exp)\nReturn 2 raised to x (exp2)\nReturn exp(x) minus 1 (expm1)\nReturn absolute value of floating-point x (fabs)\nReturn floor of x (floor)\nReturn fmod(x, y) (fmod)\nReturn mantissa and exponent of x as pair (m, e) (frexp)\nReturn sum of values in a list (fsum)\nGamma function at x (gamma)\nGreatest common divisor (gcd)\nHypotenuse of a right triangle (hypot)\nDetermine whether two values are close (isclose)\nDetermine kind of number (isnumber)\nInteger part of sqrt of input (isqrt)\nLeast common multiple (lcm)\nReturn (x * (2^i)) (ldexp)\nNatural logarithm of abs. value of gamma function at x (lgamma)\nLogarithm of x at given base (log)\nLog base 10 of x (log10)\nNatural log of 1+x (log1p)\nLog base 2 of x (log2)\nFractional and integer parts of x (modf)\nReturn x to the power of y (pow)\nConvert angle from degrees into radians (rad)\nRemainder of x/y (rem)\nSum of products of values from 2 lists (sumprod)\nTruncate x to the nearest integral toward 0 (trunc)\nReturn value of least significant bit of float x (ulp)''')
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
  elif choice == "atan2":
    atan2()
  elif choice == "cbrt":
    cbrt()
  elif choice == "ceil":
    ceil()
  elif choice == "copysign":
    copysign()
  elif choice == "degrees":
    degrees()
  elif choice == "erf":
    erf()
  elif choice == "erfc":
    erfc()
  elif choice == "exp":
    exp()
  elif choice == "exp2":
    exp2()
  elif choice == "exp1m":
    exp1m()
  elif choice == "fabs":
    fabs()
  elif choice == "floor":
    floor()
  elif choice == "fmod":
    fmod()
  elif choice == "frexp":
    frexp()
  elif choice == "fsum":
    fsum()
  elif choice == "gamma":
    gamma()
  elif choice == "gcd":
    gcd()
  elif choice == "hypot":
    hypot()
  elif choice == "isclose":
    isclose()
  elif choice == "isnumber":
    isnumber()
  elif choice == "isqrt":
    isqrt()
  elif choice == "lcm":
    lcm()
  elif choice == "ldexp":
    ldexp()
  elif choice == "lgamma":
    lgamma()
  elif choice == "log":
    log()
  elif choice == "log10":
    log10()
  elif choice == "log1p":
    log1p()
  elif choice == "log2":
    log2()
  elif choice == "modf":
    modf()
  elif choice == "nextafter":
    nextafter()
  elif choice == "pow":
    pow()
  elif choice == "prod":
    prod()
  elif choice == "rad":
    rad()
  elif choice == "rem":
    rem()
  elif choice == "sumprod":
    sumprod()
  elif choice == "trunc":
    trunc()
  elif choice == "ulp":
    ulp()

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
