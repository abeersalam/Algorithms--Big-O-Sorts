//Brian Mitzel      893038547
//Sorasit Wanichpan 897260477
//Abeer Salam       899423594
//CPSC 335
//Version 3
//Project 3, in-place selection sort 
//
//This C++ program reads the first n lines of a text file and uses an in-place selection sort algorithm to
//sort the lines alphabetically. It also records the time that the in-place selection sort algorithm takes
//to execute.
//
//Note: Make sure the machine running the code is not running on battery (or power saving mode) and that
//      the program is running on release mode (in Visual Studios). If run in debug mode, it will generate
//      debugging files and impact overall performance (affects overall runtime). In addition, make sure you
//      compile the project with the C++ 11 standards; otherwise, chrono will not work. For Visual Studio,
//		this requires version 2012 or later.
//
//To compile in Linux: g++ std=c++11 in_place_selection.cpp -o ips.exe 
//To run: ./ips.exe <filename> <# number of words to be sorted>

#include <iostream>
#include <cstdlib>
#include <chrono>
#include <fstream>
#include <string>

using namespace std;

void in_place_selection_sortA(string[], int);
//Purpose: Performs in-place selection sort on an array of strings
//Precondition: The size of the array is passed as a nonnegative integer along with the array itself
//Postcondition: The array of strings is sorted in alphabetical order

int main(int argc, char* argv[])
{
	if (argc != 3)
	{
		cout << "error: you must supply exactly two arguments\n\n"
			 << "usage: python3 ip_selection_sort.py <input file> <n value>" << endl;
		exit(1);
	}

	//Capture the command line arguments
	ifstream fileToBeRead;
	fileToBeRead.open(argv[1]);
	int n_Val = atoi(argv[2]);

	//Introduction
	cout << "----------" << endl;
	cout << "C++ in-place selection sort:" << endl;
	cout << "requested n = " << n_Val << endl;

	//Read in file and print first 10 unsorted words
	cout << "first 10 unsorted words: ";
	string* words = new string[n_Val];
	for (int i = 0; i < n_Val; i++)
	{
		fileToBeRead >> words[i]; //Reads until end of line
		if (i < 10) //Prints out the first 10 words (Unsorted)
		{
			cout << "[" << words[i] << "] ";
		}
	}
	cout << "\nloaded " << n_Val << " lines from '" << argv[1] << "'" << endl;

	//Runs the timer and algorithm
	cout << "running in-place selection sort..." << endl;
	auto start = chrono::high_resolution_clock::now();
	in_place_selection_sortA(words, n_Val);
	auto end = chrono::high_resolution_clock::now();
	int microseconds = chrono::duration_cast<chrono::microseconds>(end - start).count();
	double seconds = microseconds / 1E6;
	
	//Outputs the first 10 sorted words and the elapsed time
	cout << "first 10 sorted words: ";
	for (int i = 0; i < 10; i++)
	{
		cout << "[" << words[i] + "] ";
	}
	cout << "\nelapsed time: " << seconds << " seconds" << endl;
	cout << "\n----------" << endl;

	delete[] words;
	
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