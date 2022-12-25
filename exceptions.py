import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Sólo se admiten números.")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: No se puede dividir por 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")