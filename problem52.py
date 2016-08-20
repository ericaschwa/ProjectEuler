# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.

def getDigitSet(n):
	digitSet = set()
	while n > 0:
		digitSet.add(n % 10)
		n /= 10
	return digitSet

num = 1
while True:
	digitSet = getDigitSet(num)
	digitSet2 = getDigitSet(num * 2)
	if digitSet == digitSet2:
		digitSet3 = getDigitSet(num * 3)
		if digitSet == digitSet3:
			digitSet4 = getDigitSet(num * 4)
			if digitSet == digitSet4:
				digitSet5 = getDigitSet(num * 5)
				if digitSet == digitSet5:
					digitSet6 = getDigitSet(num * 6)
					if digitSet == digitSet6:
						print num
						break
	num += 1

# answer: 142857