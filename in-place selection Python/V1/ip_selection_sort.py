#Brian Mitzel      893038547
#Sorasit Wanichpan 897260477
#Abeer Salam       899423594
#CPSC 335
#Project 3 First Draft
#python3 ip_selection_sort.py <input file> <n value>

import sys
import time

#In place selection sort that was given in class
#Will edit later

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

    print('In-place selection sort:')
    print('n-value is: ' + str(n_value))
    start = time.perf_counter()
    content = open(input_file).read()
    tokens = content.split('\n')
    print(tokens[0:10])
    to_be_sorted = tokens[0:n_value]
    result = in_place_selection_sort(to_be_sorted)
    end = time.perf_counter()

    #Results
    print('Elapsed time: ' + str(end - start))
    print('Sorted Sequence: ' + str(result[0:]))

if __name__ == "__main__":
    main()