#include <iostream>
using namespace std;

int knapsack(int count, int capacity, int profit_array[], int weight_array[], bool use_array[])
{
	int i, index, max_profit, profit;
	int *knapsack_array;

	// Initialize integer array for tracking current knapsack
	knapsack_array = new int[count];
	for(i = 0; i < count; i++)
	{
		knapsack_array[i] = 0;
	}

	// Set all variables to start state
	index = 0;
	max_profit = 0;
	profit = 0;

	// Backtrack until all solutions finish
	while(index >= 0)
	{
		// If this branch exceeds item count, backtrack 
		if(index == count)
		{
			index--;
			continue;
		}

		// If all possibilites are already tried on that item, backtrack
		if(knapsack_array[index] == 2)
		{
			knapsack_array[index] = 0;
			profit -= profit_array[index];
			capacity += weight_array[index];
			index--;
			continue;
		}

		// Suppose if item is set to be used
		if(knapsack_array[index] == 1)
		{
			// If usage exceeds capacity limit, backtrack back
			if(weight_array[index] > capacity)
			{
				knapsack_array[index] = 0;
				index--;
				continue;
			}

			// If not, continue the assumption
			profit += profit_array[index];
			capacity -= weight_array[index];
		}

		// Set this probability "processed" and proceed to next item
		knapsack_array[index]++;
		index++;

		// If the current profit is greater than max profit up to now
		if(profit > max_profit)
		{
			// Update max profit
			max_profit = profit;

			// Update use array
			for(i = 0; i < count; i++)
			{
				if(knapsack_array[i] == 2)
				{
					use_array[i] = true;
				}
				else
				{
					use_array[i] = false;
				}
			}
		}
	}

	// Delete knapsack array heap that is used
	delete knapsack_array;

	// Return the maximum possible profit
	return max_profit;
}

int main()
{
	int i;
	int result;
    int count = 4;
    int capacity = 6;
    int profit_array[4] = {40, 30, 50, 10};
    int weight_array[4] = {2, 5, 10, 5};
    bool use_array[4] = {false, false, false, false};

    // Solve the knapsack problem
    result = knapsack(count, capacity, profit_array, weight_array, use_array);

    // Print the used items
    for(i = 0; i < count; i++)
    {
    	cout << (int) use_array[i] << endl;
    }

    // Print the result of solution
    cout << result;

    return 0;
}