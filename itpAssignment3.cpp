#include <iostream>
using namespace std;

class definitions
{
public:
	int number;
	int Numbers[10];
		void fillTheArray()
		{
			int i = 0;
			while (i < 10)
			{
				cout << "Please enter an integer for 10 times" << endl;
				cin >> number;
				Numbers[i] = number;
				i++;
			}
		}
		void unSortedDisplayer()
		{
			cout << "The integers you entered: " << endl;
			for (int i = 0; i < 10; i++)
			{
				cout << Numbers[i] << endl;
			}
		}
		void swap(int* ptr1, int* ptr2)
		{
			int temp = *ptr1;
			*ptr1 = *ptr2;
			*ptr2 = temp;
		}
		void sorter()
		{
			int* ptr = Numbers;
			int i, j, temp;
			for (i = 0; i < 9; i++)
			{
				for (j = 0; j < 9; j++)
				{
					if (*(ptr + j) > *(ptr + 1 + j))
					{
						swap(ptr + j, ptr + 1 + j);
					}
				}
			}
		}
		void sortedDisplayer()
		{
			cout << "The integers you entered by descending order: " << endl;
			for (int i = 0; i < 10; i++)
			{
				cout << Numbers[i] << endl;
			}
		}
};

	int main()
	{
		definitions defs;

		defs.fillTheArray();
		defs.unSortedDisplayer();
		defs.sorter();
		defs.sortedDisplayer();
	}