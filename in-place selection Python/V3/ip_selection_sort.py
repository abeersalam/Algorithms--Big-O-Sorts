#Brian Mitzel      893038547
#Sorasit Wanichpan 897260477
#Abeer Salam       899423594
#CPSC 335
#Project 3
#Version 3
#
#This script reads the first n lines of a text file
#and uses an in-place selection sort algorithm to sort the
#lines alphabetically. It also records the time that the
#in-place selection sort algorithm takes to execute.
#
#Note: Python = less code/longer time vs C++'s more code/less time.
#
#run: python3 ip_selection_sort.py <input file> <n value>

import sys
import time

#In place selection sort that was given in class
def in_place_selection_sort(L):
    for k in range(len(L)-1):
        least = k
        for i in range(k+1, len(L)):
            if L[i] < L[least]:
                least = i

        #swap elements
        L[k], L[least] = L[least], L[k]
    return L

def main():
    if len(sys.argv) !=3:
        print('error: you must supply exactly two arguments\n\n' +
              'usage: python3 ip_selection_sort.py <input file> <n value>' )
        sys.exit(1)

    #Capture the command line arguments
    input_file = sys.argv[1]
    n_value = int(sys.argv[2])

    #Introduction
    print('----------')
    print('Python in-place selection sort:')
    print('requested n = ' + str(n_value))
    to_sort = [line.rstrip('\n') for line in open(input_file)][0:n_value]

    print('loaded ' + str(n_value) + ' lines from \'' + input_file + '\'')
    print('first 10 unsorted words: ' + str(to_sort[0:10])) #Prints out the first 10
    
    #Run the algorithm/start the timer
    print('running in-place selection sort...')
    start = time.perf_counter()
    result = in_place_selection_sort(to_sort)
    end = time.perf_counter()

    #Results
    print('first 10 sorted words: ' + str(result[0:10]))
    print('elapsed time: ' + str(end - start) + ' seconds')
    print('----------')

if __name__ == "__main__":
    main()
