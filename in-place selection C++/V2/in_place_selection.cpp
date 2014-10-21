//Brian Mitzel      893038547
//Sorasit Wanichpan 897260477
//Abeer Salam       899423594
//CPSC 335
//Version 2
//Project 3, in-place selection sort 
//Note: Make sure the machine running the code is not running on battery (or power saving mode) and that
//      the program is running on release mode (on Visual Studios). If ran on debug mode, it will generate
//      debugging files and impact overall performance (Affects overall runtime). In addition, make sure you
//      compile the project with the C++ 11 standards otherwise chrono will not work (irrelevant for VS users)
//To compile in Linux: g++ std=c++11 in_place_selection.cpp -o ips.exe 
//To run: ./ips.exe <filename> <# number of words to be sorted>

#include <iostream>
#include <cstdlib>
#include <chrono>
#include <fstream>
#include <string>

using namespace std;

void in_place_selection_sortA(string[], int);
//Purpose: Performs in place selection sort for a filled list (vector).
//Precondition: Vector has to be filled with strings and an int has to be a non-negative number
//Postcondition: Returns a sorted vector back to the main

int main(int argc, char* argv[])
{
	string inputFileName;
	ifstream fileToBeRead;
	string* words = NULL;

	//Variables to hold the Nth value and counter for file read in 
	int n_Val = 0;
	int count = 0;
	
	cout << "----------" << endl;
	
	//Intialize variables based upon arguments
	if (argc != 3)
	{
	  cout << "This program requires 2 arguments!\nThe correct usage is: ./ips.exe <filename> <Nth value>" << endl;	
	  exit(0);
	}
	
	//Setting variables
	n_Val = atoi(argv[2]);
	words = new string[n_Val];
	fileToBeRead.open(argv[1]);
	
        cout << "C++ in-place selection sort" << endl;
	cout << "requested n = " << n_Val << endl;
	cout << "loaded " << n_Val << " from " << argv[1] << endl;;
	cout << "first 10 words: ";	
	
	//Read in file
	while (count != n_Val) //Reads until end of line
	{
		fileToBeRead >> words[count];
		if (count <= 10) //Prints out the first 10 words (Unsorted)
		{
			cout << "[" << words[count] + "] ";
		}
		count++;
	}
	
	//Runs the  timer and algorithm
	cout << "\nrunning in-place selection algorithm...";
	auto start = chrono::high_resolution_clock::now();
	in_place_selection_sortA(words, n_Val);
	auto end = chrono::high_resolution_clock::now();
	int microseconds = chrono::duration_cast<chrono::microseconds>(end - start).count();
	
	//Outputs the time
	double seconds = microseconds / 1E6;
	cout << "\nelapsed time: " << seconds << " seconds" << endl;

	//Outputs the first 10 sorted results
	cout << "first 10 sorted words: ";
	for (int i = 0; i < 10; i++)
	{
		cout << "[" << words[i] + "] ";
	}
	
	cout << "\n----------" << endl;
	
	return 0;
}

//In-place selection sort, implemented in C++
void in_place_selection_sortA(string token[], int n)
{
	int least;
	for (int i = 0; i < (n - 1); i++)
	{
		least = i;
		for (int j = (i + 1); j < n; j++)
		{
			if (token[j] < token[least])
			{
				least = j;
			}
		}
		swap(token[i], token[least]);
	}
}