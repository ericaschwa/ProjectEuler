# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# algebra
# a^2 + b^2 = c^2
# a^2 + b^2 + c^2 + ab + bc + ac = 1000000
# 2c^2 + ab + bc + ac = 1000000
# c(a + b +  c) + c^2 + ab = 1000000
# 1000c + c^2 + ab = 1000000

# slightly impoved version of brute force
def findAnswer(n):
	amax = n / 3
	bmax = n / 2 - 1
	cmax = n - 3
	for a in range(1, amax):
		asquared = a * a
		for b in range(a + 1, bmax):
			bsquared = b * b
			absum = a + b
			absquaredsum = asquared + bsquared
			for c in range(b + 1, cmax):
				if absquaredsum == c * c and absum + c == 1000:
					return [a, b, c]

print findAnswer(1000)