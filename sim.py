import math

x = 1.7
y = -1.2
rate = 0.001
steps = 100

while steps != 0:
    steps = steps - 1
    x = x + rate * (2 * x + 20 * math.pi * math.sin(2 * math.pi * x))
    y = y + rate * (2 * y + 20 * math.pi * math.sin(2 * math.pi * y))
print(x, y)
