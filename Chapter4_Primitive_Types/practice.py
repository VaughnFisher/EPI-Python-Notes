''' TIPS
-bitwise operators
-how to use masks and create them machine independently
-fast ways to clear lowestmost set bit
-undesrtand signedness and shifting
-consider using a cache
-commutativity and associativity can be used to perform operations
	in parallel and reorder operations
'''

''' REVIEW
-bitwise operators &,|,>>,<<,~,^
-2's complement
-key methods for numeric types are abs(x), math.ceil(x), math.floor(x),
	min(x,y), max(x,y), pow(x,y), and math.sqrt(x)
-interconvert integers and strings, e.g., str(42), int('42'), floats and
	strings, e.g., str(3.14), float('3.14')
-refer to infinity as float('inf')
-consider using math.isclose() when comparing floating point values
-key methods in random are random.randrange(28), random.randint(8,16),
	random.random(), random.shuffle(A), and random.choice(A)
'''

### BC ###
# Write a program that counts the number of bits set to 1
# in a nonnegative integer
##########

def countBits(x: int) -> int:
	numBits = 0
	while x:
		numBits += x & 1	#checks if rightmost bit is 1
		x >>= 1				#shifts next bit to the left 
	return numBits
'''
-since its O(1) computation per bit, time complexity is O(n)
'''

### 4.1 ###
# Write a program that computes the parity of a very large number
# of 64-bit words
###########

def parity(x: int) -> int:
	result = 0				#parity defaults at zero
	while x:
		result ^= x & 1		#flips result after every 1 found
		x >>= 1				#shift left
	return result
'''
-time complexity O(n), n being the word size
-brute force so not optimal
+PRO TIP: x&(x-1) equals x with its lowest bit erased
'''

def parity(x: int) -> int:
	result = 0
	while x:
		result ^= 1			#flips result every iteration
		x &= x - 1			#drops lowest set bit
	return result
'''
-this is O(k), k being the number of bits set to 1
-what if you compute the parity of a huge number of 64-bit words, though?
	we must process multiple bits at one time, and cache the results in 
	an array-based lookup table.
-Let's start with an example using a 2 bit word.
	parities of 00, 01, 10, and 11 are [0, 1, 1, 0]
	precomputed = [0, 1, 1, 0]
'''

def parity(x):
    MASK_SIZE = 2 # 2 bit words, up tp 8 bit int
    BIT_MASK = 0b0011
    return (precomputed[x >> (3*MASK_SIZE)] ^
            precomputed[(x >> (2*MASK_SIZE)) & BIT_MASK] ^
            precomputed[(x >> MASK_SIZE) & BIT_MASK] ^
            precomputed[x & BIT_MASK])

### 4.2 ###
# Write a program that swaps a pair of bits
###########

def swapBits(x, i, j):					#x int, i and j to be swapped
    if (x >> i) & 1 != (x >> j) & 1:	#check if bits are not the same
        bit_mask = (1 << i) | (1 << j)	#create mask
        x ^= bit_mask 					#apply mask
    return x
'''
- time complexity is O(1)
'''

### 4.3 ###
# Write a program that reverses the order of bits of a 64-bit signed integer
###########

def reverseBits(x):
    for i in range(32):
        bitmask = (1 << i) | (1 << 63 - i)
        x ^= bitmask
    return x
'''
-brute force ew
-a lookup table is the best way to improve this
'''

def reverseBits(x):
    maskSize = 16
    bitMask = 0xFFFF
    return (precomputedReverse[x & bitMask] << (3 * maskSize)
            | precomputedReverse[(x >> maskSize) & bitMask] <<
            (2 * maskSize) |
            precomputedReverse[(x >> (2 * maskSize)) & bitMask] << maskSize
            | precomputedReverse[(x >> (3 * maskSize)) & bitMask])
'''
-time complexity O(n/L), for n-bit integers and L-bit cache keys
-this program performs many reverses in an array based lookup table
-EX. if the input is (10010011), its reverse is rev(11),rev(00),
	rev(01), rev(10)
'''

### 4.4 ###
# Write a program that finds the closest integer with the same weight
# i.e. not equal to x but has same number of 1 bits, and |x-y| is smallest
###########

def closestIntSameBitCount(x):

    numUnsignedBits = 64
    for i in range(numUnsignedBits - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:	#find lowest pair of different bits
            x ^= (1 << i) | (1 << (i + 1))  	#Swaps bit-i and bit-(i + 1).
            return x

    # Raise error if all bits of x are 0 or 1.
    raise ValueError('All bits are 0 or 1')

'''
-we want to start from the LSB to make the smallest change
-we traverse bits right to left to find a pair that are not the same
-flip the bits to maintain same weight
-time complexity is O(n)
'''

### 4.5 ###
# Write a program that multiplies two nonnegative integers while only
# using assignment, bitwise operators, and equality checks/Boolean combinations
###########

def multiply(x, y):
	def add(a, b):
		while b:
			carry = a & b
			a = a ^ b
			b = carry << 1
		return a

	runningSum = 0

	while x:
		if x & 1:
			runningSum = add(runningSum, y)
		x >>= 1
		y <<= 1
	return runningSum

'''
-to multiply x and y, we initialize the result to 0 and iterate through
	the bits of x, adding (2^k)y to the result if the kth bit of x is 1
-(2^k)y can be found by left shifting y by k
-EX. multiply(13,9) (1101)x(1001)
	check first bit, 1 so set result to 1x1001 (1001)
	check second bit, 0 so move on
	check third bit, 1 so shift (1001) to the left by 2 (100100)
		then add to running total to get (101101)
	check fourth bit, 1 so shift (1001) to the left by 3 (1001000)
		then add to running total to get (1110101)
'''

 