import time
import math

n = int(input("Sample input:\n"))
t = int(input())
time.sleep(t/1000)
result = math.sqrt(n)
print(f"Square root of {n} after {t} milliseconds is {result}")