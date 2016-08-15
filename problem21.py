# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).

# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def sumDivisors(n):
	sumD = 0
	for i in range(1,n):
		if n % i == 0:
			sumD += i
	return sumD

print sumDivisors(220) #284
print sumDivisors(284) #220

divisorSums = {}
amicableNums = set()
for i in range(0,10000):
	iDivisorSum = sumDivisors(i)
	if iDivisorSum in divisorSums and divisorSums[iDivisorSum] == i:
		amicableNums.add((iDivisorSum, divisorSums[iDivisorSum]))
	divisorSums[i] = iDivisorSum

print amicableNums