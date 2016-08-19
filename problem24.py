# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

permutations = []

def findPermutations(head, tail):
	if len(tail) == 0:
		permutations.append(head)
	for i in range(0, len(tail)):
		findPermutations(head + tail[i], tail[:i] + tail[i+1:])

findPermutations("", ["0", "1", "2"])
print permutations # ['012', '021', '102', '120', '201', '210']

findPermutations("", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
print permutations[1000000] # 2783914605