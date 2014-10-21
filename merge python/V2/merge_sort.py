#Brian Mitzel      893038547
#Sorasit Wanichpan 897260477
#Abeer Salam       899423594
#CPSC 335
#Project 3 Third Draft
#python3 merge_sort.py <input file> <n value> 

import sys
import time

# Merges two sorted lists A and B into one sorted list S
# as shown in the lecture notes
def merge(A, B):
    S = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            x = A[i]
            i += 1
        else:
            x = B[j]
            j += 1
        S.append(x)
    return S + A[i:] + B[j:]

# Sorts a list L using the Merge Sort decrease-by-half algorithm
# as shown in the lecture notes
def merge_sort(L):
    if len(L) <= 1:
        return L
    else:
        middle = int(len(L) / 2)
        left = L[:middle]
        right = L[middle:]
 
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)
    
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
    print('Sorted Sequence: ' + str(result[0:10]))

if __name__ == "__main__":
    main()
