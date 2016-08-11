# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# I solve this in O(1) time

def sumMultiples(n, factor):
	# number of multiples of "factor" below "n"
	timesDivisible = (n - 1) / factor
	return factor * timesDivisible * (timesDivisible + 1) / 2


# the subtraction is necessary to avoid double-counting of numbers
# that are under 1000 and factors of both 3 and 5	
print sumMultiples(10, 3) + sumMultiples(10, 5) - sumMultiples(10, 3 * 5)

print sumMultiples(1000, 3) + sumMultiples(1000, 5) - \
      sumMultiples(1000, 3 * 5)
