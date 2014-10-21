#Brian Mitzel      893038547
#Sorasit Wanichpan 897260477
#Abeer Salam       899423594
#CPSC 335
#Project 3 First Draft
#python3 mergesort.py <input file> <n value> 

import sys
import time
#Merge Sort implementation derived off of one found on Wikipedia

def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) / 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))
	
def main():
	if len(sys.argv) !=3:
        print('error: you must supply exactly two arguments\n\n' +
              'usage: python3 mergesort.py <input file> <n value>' )
        sys.exit(1)
	
	#Capture the command line arguments
	input_file = sys.argv[1]
	n_value = int(sys.argv[2])
	
	print('Merge sort:')
	print('n-value is: ' + str(n_value))
	start = time.perf_counter()
	content = open(input_file).read()
	tokens = content.split('\n')
	print(tokens[0:10])
	to_be_sorted = tokens[0:n_value]
	result = merge_sort(to_be_sorted)
	end = time.perf_counter()
	
	#Results
	print('Elapsed time: ' + str(end - start))
	print('Sorted Sequence: ' + str(result[0:]))

if __name__ == "__main__":
	main()