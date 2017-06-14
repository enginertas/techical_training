#include <iostream>
#include <stack>
#include <climits>

using namespace std;

#define DEFAULT_NEG_VALUE -10001

class StackWithMin: public stack<int>
{
	private:
		stack<int> min_stack;

	public:
		void push(int elem);
		int pop();
		int top();
		int min();
};

void StackWithMin::push(int elem)
{
	if(elem <= min())
	{
		min_stack.push(elem);
	}

	this->stack<int>::push(elem);
}

int StackWithMin::pop()
{
	int ret_val;

	if(this->empty())
	{
		return DEFAULT_NEG_VALUE;
	}

	ret_val = this->stack<int>::top();
	this->stack<int>::pop();

	if(ret_val == min())
	{
		min_stack.pop();
	}

	return ret_val;
}

int StackWithMin::top()
{
	if(this->empty())
	{
		return DEFAULT_NEG_VALUE;
	}
	else
	{
		return this->stack<int>::top();
	}
}

int StackWithMin::min()
{
	if(min_stack.empty())
	{
		return INT_MAX;
	}
	else
	{
		return min_stack.top();
	}
}


int main(int argc, char *argv[])
{
	StackWithMin a;
	int i;
	int unique_set[4] = {3, 4, 2, 1};
	int complex_set[19] = {2, 2, 3, 3, 2, 2, 3, 3, 1, 1, 2, 1, 2, 1, 0, 0, 1, -3, 5};

	// empty, pop, top, min check when stack is empty
	cout << "---------- The stack is empty ----------" << endl;
	cout << "empty: " << a.empty() << endl;
	cout << "top: " << a.top() << endl;
	cout << "min: " << a.min() << endl;
	cout << "pop: " << a.pop() << endl;

	// Multiple empty, pop, top and min checks, after single push
	cout << "---------- Single push tests ----------" << endl;
	cout << "push 3" << endl;
	a.push(3);
	
	for(i = 0; i < 2; i++)
	{
		cout << "empty: " << a.empty() << endl;
		cout << "top: " << a.top() << endl;
		cout << "min: " << a.min() << endl;
		cout << "pop: " << a.pop() << endl;		
	}

	// Multiple pushes with all unique elements
	cout << "---------- Tests with unique elements ----------" << endl;
	
	for(i = 0; i < 4; i++)
	{
		cout << "push " << unique_set[i] << endl;
		a.push(unique_set[i]);
	}

	for(i = 0; i < 5; i++)
	{
		cout << "empty: " << a.empty() << endl;
		cout << "top: " << a.top() << endl;
		cout << "min: " << a.min() << endl;
		cout << "pop: " << a.pop() << endl;		
	}

	// Multiple pushes with elements some of which are not unique
	cout << "---------- Tests with some unique and non-unique elements ----------" << endl;
	for(i = 0; i < 19; i++)
	{
		cout << "push " << complex_set[i] << endl;
		a.push(complex_set[i]);
	}

	for(i = 0; i < 20; i++)
	{
		cout << "empty: " << a.empty() << endl;
		cout << "top: " << a.top() << endl;
		cout << "min: " << a.min() << endl;
		cout << "pop: " << a.pop() << endl;		
	}

	return 0;
}