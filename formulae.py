import math
delta = b * b - 4 * a * c
if delta >= 0:
  x1 = (-b - math.sqrt(delta)) / (2 * a)
  x2 = (-b + math.sqrt(delta)) / (2 * a)
  provex1 = a * x1 * x1 + b * x1 + c
  provex2 = a * x2 * x2 + b * x2 + c
else:
  x1 = 0
  x2 = 0
  provex1 = 0
  provex2 = 0