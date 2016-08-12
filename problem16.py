# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

def digitsInBigNum(n, base):
	digits = []
	while n > 0:
		digits.append(n%base)
		n /= base
	return digits

bignumdigits = digitsInBigNum(pow(2,15), 10)
print sum(bignumdigits)

