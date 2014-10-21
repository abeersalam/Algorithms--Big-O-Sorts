#Brian Mitzel      893038547
#Sorasit Wanichpan 897260477
#Abeer Salam       899423594
#CPSC 335
#Project 3 Second Draft
#python3 merge_sort.py <input file> <n value> 

import sys
import time
#Merge Sort implementation derived off of one found on Wikipedia

def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = int(len(m) / 2)
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))
    
def main():
    if len(sys.argv) !=3:
        print('error: you must supply exactly two arguments\n\n' +
              'usage: python3 merge_sort.py <input file> <n value>' )
        sys.exit(1)
    
    #Capture the command line arguments
    input_file = sys.argv[1]
    n_value = int(sys.argv[2])

    #Introduction
    print('Merge sort:')
    print('n-value is: ' + str(n_value))
    to_sort = [line.rstrip('\n') for line in open(input_file)][0:n_value]
    print(to_sort[0:10])

    #Merge Sort
    start = time.perf_counter()
    result = merge_sort(to_sort)
    end = time.perf_counter()
    
    #Results
    print('Elapsed time: ' + str(end - start))
    print('Sorted Sequence: ' + str(result[0:]))

if __name__ == "__main__":
    main()
