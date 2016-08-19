# Starting with the number 1 and moving to the right in a clockwise direction,
# a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?

# pattern in 1, (3, 5, 7, 9), (13, 17, 21, 25)
# group increment:   +2 		    +4                +6      ...
# (while increment < size ...)
# group start:  + 2, + 4, (+ new increment)


def sumSpiralDiags(size):
	total = 1
	curr = 1
	increment = 2
	while increment < size:
		total += ((curr + 1 * increment) +
				  (curr + 2 * increment) +
				  (curr + 3 * increment) +
				  (curr + 4 * increment))
		curr = curr + 4 * increment
		increment += 2
	return total

print sumSpiralDiags(5) # 101
print sumSpiralDiags(1001) # 669171001