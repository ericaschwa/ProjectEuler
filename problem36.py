# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic
# in base 10 and base 2.

# (Please note that the palindromic number, in either base,
# may not include leading zeros.)

# from http://stackoverflow.com/questions/699866/python-int-to-binary

def int2bin(i):
    if i == 0: return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i /= 2
    return s

def isBiPalindromic(n):
	digits = str(n)
	binary = int2bin(n)
	for i in range(0, len(digits) / 2):
		if digits[i] != digits[len(digits) - i - 1]:
			return False
	for i in range(0, len(binary) / 2):
		if binary[i] != binary[len(binary) - i - 1]:
			return False
	return True

def sumBiPalindromics(n):
	total = 0
	while n > 0:
		if isBiPalindromic(n):
			total += n
		n -= 1
	return total

print isBiPalindromic(585) # True
print isBiPalindromic(4) # False
print isBiPalindromic(9) # True
print isBiPalindromic(15) # False

print sumBiPalindromics(10) # 1 + 3 + 5 + 7 + 9 = 25
print sumBiPalindromics(1000000) # 872187