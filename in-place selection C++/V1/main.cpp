//Brian Mitzel      893038547
//Sorasit Wanichpan 897260477
//Abeer Salam       899423594
//CPSC 335
//Project 3 First Draft

#include <iostream>
#include <utility>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void in_place_selection_sort(vector<string>&, int);

int main()
{
	string inputFileName;
	string line;
	ifstream fileToBeRead;
	vector<string> contents;
	int nVal = 0;

	cout << "Input Value for N: ";
	cin >> nVal;

	//Reads file and tokenize values
	fileToBeRead.open("beowulf.txt");
	while (!fileToBeRead.eof()) //Reads until end of line
	{
		getline(fileToBeRead, line); //Gets each word
		contents.push_back(line); //Each word is stored in a vector
	}

	//UnSorted
	for (int i = 0; i < nVal; i++)
	{
		cout << contents[i] << endl;

	}

	cout << endl << endl;

	//Sorted
	in_place_selection_sort(contents, nVal);
	
	for (int i = 0; i < nVal; i++)
	{
		cout << contents[i] << endl;

	}

	return 0;
}

//C++ Style
void in_place_selection_sort(vector<string> &token, int n)
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
