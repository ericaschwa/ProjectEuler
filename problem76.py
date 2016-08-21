# It is possible to write five as a sum in exactly six different ways:

#		4 + 1
#		3 + 2
#		3 + 1 + 1
#		2 + 2 + 1
#		2 + 1 + 1 + 1
#		1 + 1 + 1 + 1 + 1

# How many different ways can 100 be written as a sum of >=2 positive ints?

# 		<2: 0
#		2: 1 		1 + 1
#		3: 2 		1 + 1 + 1, 1 + 2
#		4: 4 (
#			1		1 + 1 + 1 + 1

#			2		1 + 1 + 2, _2 + 2_ 					2 						(total for 4 - 2, rows up to 3) PLUS 1 = 1 + 1 = 2

#			1		3 + 1
#		)
#		5: 6 (
#			1		1 + 1 + 1 + 1 + 1

#			2		1 + 1 + 1 + 2, 1 + 2 + 2			2 						(total for 5 - 2, rows up to 2) PLUS 0 = 2 + 0 = 2 2 is less than half 5
#			2		3 + 1 + 1, _3 + 2_ 					2 			    		(total for 5 - 3, rows up to 3) PLUS 1 = 1 + 1 = 2

#			1		1 + 4
#		)
#		6: 10 (
#			1 		1 + 1 + 1 + 1 + 1 + 1

#			3 		1 + 1 + 1 + 1 + 2, 1 + 1 + 2 + 2, 2 + 2 + 2 				(total for 6 - 2, rows up to 2) PLUS 0 = 3 + 0 = 3 2 is less than half 6
#			3 		1 + 2 + 3, 1 + 1 + 1 + 3, _3 + 3_							(total for 6 - 3, rows up to 3) PLUS 1 = 2 + 1 = 3
#			2  		1 + 1 + 4, _2 + 4_											(total for 6 - 4, rows up to 4) PLUS 1 = 1 + 1 = 2

#			1		1 + 5
#		)

# 		7: 14 (
#			1 		1 + 1 + 1 + 1 + 1 + 1 + 1
#			3 		1 + 1 + 1 + 1 + 1 + 2, 1 + 1 + 1 + 2 + 2, 1 + 2 + 2 + 2 	(total for 7 - 2, rows up to 2) PLUS 0 = 3 + 0 = 3  2 is less than half 7
#			4 		1 + 1 + 1 + 1 + 3, 1 + 1 + 2 + 3, 2 + 2 + 3, 1 + 3 + 3 		(total for 7 - 3, rows up to 3) PLUS 0 = 4 + 0 = 4  3 is less than half 7
#			3 		1 + 1 + 1 + 4, 1 + 2 + 4, 3 + 4 							(total for 7 - 4, rows up to 4) PLUS 1 = 2 + 1 = 3
#			2 		1 + 1 + 5, 2 + 5 											(total for 7 - 5, rows up to 5) PLUS 1 = 1 + 1 = 2
#			1 		1 + 6
#		)

# 		...

def rowsOfListUpTo(l, n):
	i = 0
	total = 0
	while i < len(l) and i < n:
		total += l[i]
		i += 1
	return total

def waysToWriteAsSum(n):
	sumNums = [[0],[0],[1],[1,1]]
	for i in range(4, n + 1):
		thisNum = [1]
		for j in range(1, i - 2):
			thisSum = rowsOfListUpTo(sumNums[i - j], j)
			if j < i / 2:
				thisSum += 1
			thisNum.append(thisSum)
		thisNum.append(1)
		sumNums.append(thisNum)
	return sum(sumNums[n])

print waysToWriteAsSum(4) # 4
print waysToWriteAsSum(5) # 6
print waysToWriteAsSum(6) # 10
print waysToWriteAsSum(7) # 14

print waysToWriteAsSum(100) # 8083904

