# 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is
# 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

import math


def sumFact(n):
	num = math.factorial(n)
	result = 0
	while num > 0:
		result += num % 10
		num = num / 10
	return result

print sumFact(10) # 27
print sumFact(100) # 648

