# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is  3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 2640

# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def diffSumSquares(n):
	sumFirstNums = n * (n + 1) / 2
	squareOfSum = (sumFirstNums * sumFirstNums)
	sumOfSquares = 0
	for i in range(1, n + 1):
		sumOfSquares += (i * i)
	return squareOfSum - sumOfSquares


print diffSumSquares(10)