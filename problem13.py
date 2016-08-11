# Work out the last ten digits of the sum of the
# following one-hundred 50-digit numbers.

from bignum import bignum

result = 0
numlist = bignum.split()
for num in numlist:
	result += int(num[-10:])

print str(result)[-10:]