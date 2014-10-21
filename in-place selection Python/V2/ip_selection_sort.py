#Brian Mitzel      893038547
#Sorasit Wanichpan 897260477
#Abeer Salam       899423594
#CPSC 335
#Project 3
#Version 2
#Note: Python = less code/longer time vs C++'s more code/less time.
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

    print('----------')
    print('Python in-place selection sort:')
    print('requested n = ' + str(n_value))

    content = open(input_file).read() #Read file contents
    tokens = content.split('\n')  #tokenize each of the word
    print('first 10 words: ' + str(tokens[0:10])) #Prints out the first 10
    
    to_be_sorted = tokens[0:n_value] #Determine the total # of words to be sorted
    
    #Run the algorithm/start the timer
    print('running in-place selection sort...')
    start = time.perf_counter()
    result = in_place_selection_sort(to_be_sorted)
    end = time.perf_counter()

    #Results
    print('Elapsed time: ' + str(end - start))
    print('first 10 sorted words: ' + str(result[0:10]))
    print('----------')

if __name__ == "__main__":
    main()