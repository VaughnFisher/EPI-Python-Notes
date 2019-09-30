''' TIPS
-brute force is usually easy to find 0(n) space, there are solutions that
	use the array itself to reduce space complexity to 0(n)
-see if its possible to write values from the back
-consider overwriting entry rather than deleting
-when working with integers encoded by an arrayn consider processing the
	digits from the back of the array. Alternatively, reverse the array
	so the LSD is the first entry
-be comfortable with writing code that operates on subarrays
-watch out for off-by-1 errors
-dont worry about integrity of array until its time to return
-arrays are most useful when you know the distribution of the elements
	in advance. Ex.Boolean array with length W
-use parallel logic for rows and columns on 2D arrays
-"sometimes its easier to simulate the specification, than to analytically
	solve for the result. For example, rather than writing a formula for the i-th
	entry in the spiral order for an nxn matrix, just compute the output
	from the beginning"
'''

''' REVIEW
-syntax for instantiating list, e.g., [3,5,7], [1]+[0]*10, list(range(100))
-basic operations len(A), A.append(42), A.remove(2), A.insert(3,28)
-instantiate 2D array, e.g., [[1,2,3],[3,4],[13]]
-understand how copy works. Difference between B=A and B=list(A)
-difference between deep copy and shallow copy
-key list methods like min(A), max(A), binary search for sorted lists
	(bisect.bisect(A,6), bisect.bisect_left(A,6), and bisect.bisect_right(A,6))
	A.reverse() (in place), reversed(A)(returns an iterator), A.sort()(in place),
	sorted(A)(returns a copy), del A[i](deletes the ith element) and del A[i:j]
	removes the slice
-slicing form A[i:j:k], A[::-1] reverses list, A[k:] + A[:k] rotates list
	by k to the left, B= A[:] does a shallow copy
'''

### BC ###
# Reorder an array so the even entries appear first, use O(1) space
##########

def evenOdd(A: List[int]):
	x = 0								#starting index
	y = len(A) - 1						#last index
	while x < y:			
		if A[x] % 2 == 0:				#if starting index is even
			x += 1						#keep even there and shift start right 1
		else:
			A[x], A[y] = A[y], A[x]		#otherwise swap odd to the back
			y -= 1						#and shift last index left 1
'''
-constant amount of processing per entry, time complexity is O(n), space O(1)
-be more pythonic by using list comprehensions
	list comprehension involves:
		1. an input sequence
		2. an iterator over the input sequence
		3. a logical condition over the iterator(optional)
		4. an expression that yields the elements of the derived list
	Ex. [x**2 for x in range(6)] yeilds [0,1,4,9,16,25] and
		[x**2 for x in range(6) if x % 2 == 0] yeilds [0,4,16]
'''

### 5.1 ###
# Write a program that takes an array A and an index i into A, and
# rearranges the elements such that all elements less than A[i] (the pivot)
# appear first, followed by elements equal, followed by elements greater
###########

def dutchFlagPartition(pivotIndex, A):
	pivot = A[pivotIndex]
	newList = []
	for item in A:
        if item < pivot:
            newList.insert(0, item)
        elif item == pivot:
            newList.append(item)
    for item in A:
        if item > pivot:
            newList.append(item)
    return newList
'''
-lazy brute force, O(n) solution
-lets find a solution using a partition step like quicksort
'''

def dutchFlagPartition(pivotIndex, A):
	pivot = A[pivotIndex]
	smaller = 0									#set start index
	for i in range(len(A)):						#traverse whole array
		if A[i] < pivot:						#if less than pivot
			A[i], A[smaller] = A[smaller], A[i]	#swap elements
			smaller += 1						#shift start 1

	larger = len(A) - 1
	for i in reversed(range(len(A))):			#do the same as above
		if A[i] > pivot:						#but from the other side
			A[i], A[larger] = A[larger], A[i]	#swapping the larger elements
			larger -= 1
'''
-first pass moves all smaller to the beginning, second pass moves larger to the end
-time complexity O(n) and space O(1)
-lets try to do all this in a single pass
'''

def dutchFlagPartition(pivotIndex, A):
	pivot = A[pivotIndex]
	smaller = 0
	equal = 0
	larger = len(A)
	while equal < larger
		if A[equal] < pivot:
			A[smaller], A[equal] = A[equal], A[smaller]
			smaller, equal = smaller + 1, equal + 1
		elif A[equal] == pivot:
			equal += 1
		else:
			larger -= 1
			A[equal], A[larger] = A[larger], A[equal]
'''
-this version has an 'unclassified group' that decreases in size each iteration
-time complexity is O(n) and space is still O(1)
-there are 4 varients to this problem...
'''

### 5.2 ###
# Write a program which takes as input an array of digits encoding a nonnegative
# decimal integer D and updates the array to represent the integer D+1.
###########

def plusOne(A):
	A[-1] += 1
	for i in reversed(range(1, len(A))):
		if A[i] != 10:
			break
		A[i] = 0
		A[i-1] += 1
	if A[0] == 10:
		A[0] = 1
		A.append(0)
	return A 
'''
-initially I thought to convert the digits in the array to an integer,
	add 1, then convert back. This ends up being easier and is the
	same answer in the book
-time complexity O(n)
'''

### 5.3 ###
# Write a program that takes two arrays representing integers, and returns
# and returns an integer representing their product
###########

def multiply(num1, num2):
    total = 0
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    for i in reversed(range(1, len(num1))):
        for j in reversed(range(1, len(num2))):
            total += (num1[i] * num2[j] * (10 ** (len(num1) - i - 1))
                      * (10 ** (len(num2) - j - 1)))
    product = [int(x) for x in str(total)]

    return product
'''
expected:    [-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7]
result:      [5, 7, 9, 4, 7, 2, 2, 1, 6, 0, 9, 7, 6, 4, 1, 2, 9, 2, 7]
first 8 digits match but something goes wrong, gotta figure this out
'''

def multiply(num1, num2):

    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # Remove the leading zeroes.
    result = result[next((
        i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]

### 5.4 ###
# Write a program which takes an array of n integers, where A[i]
# denotes the maximum you can advance from index i, and returns
# whether itis possible to advance to the last index starting
# from the beginning of the array
###########
