#Brian Mitzel      893038547
#Sorasit Wanichpan 897260477
#Abeer Salam       899423594
#CPSC 335
#Project 3
#Version 4
#
#This script reads the first n lines of a text file
#and uses a merge sort algorithm to sort the lines
#alphabetically. It also records the time that the
#merge sort algorithm takes to execute.
#
#run: python3 merge_sort.py <input file> <n value> 

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
    print('----------')
    print('Python merge sort:')
    print('requested n = ' + str(n_value))
    to_sort = [line.rstrip('\n') for line in open(input_file)][0:n_value]
    print('loaded ' + str(n_value) + ' lines from \'' + input_file + '\'')
    print('first 10 unsorted words: ' + str(to_sort[0:10])) #Prints out the first 10

    #Run the algorithm/start the timer
    print('running merge sort...')
    start = time.perf_counter()
    result = merge_sort(to_sort)
    end = time.perf_counter()
    
    #Results
    print('first 10 sorted words: ' + str(result[0:10]))
    print('elapsed time: ' + str(end - start) + ' seconds')
    print('----------')

if __name__ == "__main__":
    main()
