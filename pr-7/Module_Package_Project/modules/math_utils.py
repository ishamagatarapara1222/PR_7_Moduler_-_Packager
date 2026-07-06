import math


def calculate_factorial(n):
    result = math.factorial(n)
    print(f"Factorial: {result}")


def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    ci = amount - principal
    print(f"Compound Interest: {ci:.2f}")


def trigonometric_calculations(angle_deg):
    angle_rad = math.radians(angle_deg)
    print(f"sin({angle_deg}) = {math.sin(angle_rad):.4f}")
    print(f"cos({angle_deg}) = {math.cos(angle_rad):.4f}")
    print(f"tan({angle_deg}) = {math.tan(angle_rad):.4f}")


def area_of_shapes(shape, *args):
    shape = shape.lower()
    if shape == "circle":
        r = args[0]
        area = math.pi * r * r
        print(f"Area of Circle (r={r}): {area:.4f}")
    elif shape == "rectangle":
        l, w = args[0], args[1]
        area = l * w
        print(f"Area of Rectangle ({l}x{w}): {area:.4f}")
    elif shape == "triangle":
        b, h = args[0], args[1]
        area = 0.5 * b * h
        print(f"Area of Triangle (b={b}, h={h}): {area:.4f}")
    else:
        print("Unknown shape.")
