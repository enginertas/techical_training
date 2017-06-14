#include <iostream>

using namespace std;

#define STACK_SIZE 5
#define DEFAULT_NEG_VALUE -12345;

class MyStack
{
	private:
		int indexes[3];
		int stack[STACK_SIZE * 3];

	public:
		MyStack();
		bool isEmpty(int stack_nr);
		void push(int stack_nr, int elem);
		int peek(int stack_nr);
		int pop(int stack_nr);
};

MyStack::MyStack()
{
	indexes[0] = 0;
	indexes[1] = STACK_SIZE;
	indexes[2] = STACK_SIZE * 2;
}

bool MyStack::isEmpty(int stack_nr)
{
	// Stack number validity check
	if(stack_nr < 1 || stack_nr > 3)
	{
		return true;
	}

	// nth stack = (n-1)th index
	stack_nr--;

	return indexes[stack_nr] == (stack_nr * STACK_SIZE);
}

void MyStack::push(int stack_nr, int elem)
{
	// Stack number validity check
	if(stack_nr < 1 || stack_nr > 3)
	{
		return ;
	}

	// nth stack = (n-1)th index
	stack_nr--;

	// Check if stack is filled
	if(indexes[stack_nr] == (STACK_SIZE * (stack_nr + 1)))
	{
		return ;
	}

	// Push element to current index and increment the index
	stack[indexes[stack_nr]] = elem;
	indexes[stack_nr]++;
}

int MyStack::pop(int stack_nr)
{
	// Stack number validity check
	if(stack_nr < 1 || stack_nr > 3)
	{
		return DEFAULT_NEG_VALUE;
	}

	// If stack is empty, do not pop
	if(isEmpty(stack_nr))
	{
		return DEFAULT_NEG_VALUE;
	}

	// nth stack = (n-1)th index
	stack_nr--;

	// Decrement the current index and return the element on new index
	indexes[stack_nr]--;
	return stack[indexes[stack_nr]];
}

int MyStack::peek(int stack_nr)
{
	// Stack number validity check
	if(stack_nr < 1 || stack_nr > 3)
	{
		return DEFAULT_NEG_VALUE;
	}

	// If stack is empty, reject the function call
	if(isEmpty(stack_nr))
	{
		return DEFAULT_NEG_VALUE;
	}

	// nth stack = (n-1)th index
	stack_nr--;

	return stack[indexes[stack_nr] - 1];
}

int main(int argc, char *argv[])
{
	int i;
	MyStack a;

	// Invalid stack number test
	cout << "---------- Stack Nr = -1 ----------" << endl;
	cout << "isEmpty: " << a.isEmpty(-1) << endl;
	cout << "peek: " << a.peek(-1) << endl;
	cout << "pop: " << a.pop(-1) << endl;
	cout << "push 6, 8" << endl;
	a.push(-1, 6);
	a.push(-1, 8);
	cout << "isEmpty: " << a.isEmpty(-1) << endl;
	cout << "peek: " << a.peek(-1) << endl;
	cout << "pop: " << a.pop(-1) << endl;

	cout << "---------- Stack Nr = 0 ----------" << endl;
	cout << "isEmpty: " << a.isEmpty(0) << endl;
	cout << "peek: " << a.peek(0) << endl;
	cout << "pop: " << a.pop(0) << endl;
	cout << "push 6, 8" << endl;
	a.push(0, 6);
	a.push(0, 8);
	cout << "isEmpty: " << a.isEmpty(0) << endl;
	cout << "peek: " << a.peek(0) << endl;
	cout << "pop: " << a.pop(0) << endl;

	cout << "---------- Stack Nr = 4 ----------" << endl;
	cout << "isEmpty: " << a.isEmpty(4) << endl;
	cout << "peek: " << a.peek(4) << endl;
	cout << "pop: " << a.pop(4) << endl;
	cout << "push 6, 8" << endl;
	a.push(4, 6);
	a.push(4, 8);
	cout << "isEmpty: " << a.isEmpty(4) << endl;
	cout << "peek: " << a.peek(4) << endl;
	cout << "pop: " << a.pop(4) << endl;

	// isEmpty, peek and pop check when stack is empty
	cout << "---------- All stacks are empty ----------" << endl;
	cout << "isEmpty 1: " << a.isEmpty(1) << endl;
	cout << "isEmpty 2: " << a.isEmpty(2) << endl;
	cout << "isEmpty 3: " << a.isEmpty(3) << endl;
	cout << "pop 1: " << a.pop(1) << endl;
	cout << "pop 2: " << a.pop(2) << endl;
	cout << "pop 3: " << a.pop(3) << endl;
	cout << "peek 1: " << a.peek(1) << endl;
	cout << "peek 2: " << a.peek(2) << endl;
	cout << "peek 3: " << a.peek(3) << endl;

	// multiple isEmpty, peek and pop checks after single push
	cout << "---------- After pushing one element ----------" << endl;
	cout << "push 4 to stack 1" << endl;
	a.push(1, 4);
	cout << "isEmpty 1: " << a.isEmpty(1) << endl;
	cout << "peek 1: " << a.peek(1) << endl;
	cout << "pop 1: " << a.pop(1) << endl;
	cout << "isEmpty 1: " << a.isEmpty(1) << endl;
	cout << "peek 1: " << a.peek(1) << endl;
	cout << "pop 1: " << a.pop(1) << endl;

	cout << "push 43 to stack 2" << endl;
	a.push(2, 43);
	cout << "isEmpty 2: " << a.isEmpty(2) << endl;
	cout << "peek 2: " << a.peek(2) << endl;
	cout << "pop 2: " << a.pop(2) << endl;
	cout << "isEmpty 2: " << a.isEmpty(2) << endl;
	cout << "peek 2: " << a.peek(2) << endl;
	cout << "pop 2: " << a.pop(2) << endl;
	
	cout << "push 334 to stack 3" << endl;
	a.push(3, 334);
	cout << "isEmpty 3: " << a.isEmpty(3) << endl;
	cout << "peek 3: " << a.peek(3) << endl;
	cout << "pop 3: " << a.pop(3) << endl;
	cout << "isEmpty 3: " << a.isEmpty(3) << endl;
	cout << "peek 3: " << a.peek(3) << endl;
	cout << "pop 3: " << a.pop(3) << endl;	

	// multiple push tests
	cout << "---------- After pushing three elements ----------" << endl;
	cout << "push 4 to stack 1" << endl;
	a.push(1, 4);
	cout << "push 8 to stack 1" << endl;
	a.push(1, 8);
	cout << "push 10 to stack 1" << endl;
	a.push(1, 10);
	cout << "isEmpty 1: " << a.isEmpty(1) << endl;
	cout << "peek 1: " << a.peek(1) << endl;
	cout << "pop 1: " << a.pop(1) << endl;
	cout << "isEmpty 1: " << a.isEmpty(1) << endl;
	cout << "peek 1: " << a.peek(1) << endl;
	cout << "pop 1: " << a.pop(1) << endl;
	cout << "isEmpty 1: " << a.isEmpty(1) << endl;
	cout << "peek 1: " << a.peek(1) << endl;
	cout << "pop 1: " << a.pop(1) << endl;
	cout << "isEmpty 1: " << a.isEmpty(1) << endl;
	cout << "peek 1: " << a.peek(1) << endl;
	cout << "pop 1: " << a.pop(1) << endl;

	cout << "push 43 to stack 2" << endl;
	a.push(2, 43);
	cout << "push 44 to stack 2" << endl;
	a.push(2, 44);
	cout << "push 45 to stack 2" << endl;
	a.push(2, 45);
	cout << "isEmpty 2: " << a.isEmpty(2) << endl;
	cout << "peek 2: " << a.peek(2) << endl;
	cout << "pop 2: " << a.pop(2) << endl;
	cout << "isEmpty 2: " << a.isEmpty(2) << endl;
	cout << "peek 2: " << a.peek(2) << endl;
	cout << "pop 2: " << a.pop(2) << endl;
	cout << "isEmpty 2: " << a.isEmpty(2) << endl;
	cout << "peek 2: " << a.peek(2) << endl;
	cout << "pop 2: " << a.pop(2) << endl;
	cout << "isEmpty 2: " << a.isEmpty(2) << endl;
	cout << "peek 2: " << a.peek(2) << endl;
	cout << "pop 2: " << a.pop(2) << endl;

	cout << "push 334 to stack 3" << endl;
	a.push(3, 334);
	cout << "push 335 to stack 3" << endl;
	a.push(3, 335);
	cout << "push 336 to stack 3" << endl;
	a.push(3, 336);
	cout << "isEmpty 3: " << a.isEmpty(3) << endl;
	cout << "peek 3: " << a.peek(3) << endl;
	cout << "pop 3: " << a.pop(3) << endl;
	cout << "isEmpty 3: " << a.isEmpty(3) << endl;
	cout << "peek 3: " << a.peek(3) << endl;
	cout << "pop 3: " << a.pop(3) << endl;	
	cout << "isEmpty 3: " << a.isEmpty(3) << endl;
	cout << "peek 3: " << a.peek(3) << endl;
	cout << "pop 3: " << a.pop(3) << endl;	
	cout << "isEmpty 3: " << a.isEmpty(3) << endl;
	cout << "peek 3: " << a.peek(3) << endl;
	cout << "pop 3: " << a.pop(3) << endl;

	// push more than stack sizes
	cout << "---------- After pushing elements more than stack size (size 5) ----------" << endl;
	cout << "push 1 to stack 1" << endl;
	a.push(1, 1);
	cout << "push 2 to stack 1" << endl;
	a.push(1, 2);
	cout << "push 3 to stack 1" << endl;
	a.push(1, 3);
	cout << "push 4 to stack 1" << endl;
	a.push(1, 4);
	cout << "push 5 to stack 1" << endl;
	a.push(1, 5);
	cout << "push 6 to stack 1" << endl;
	a.push(1, 6);
	cout << "push 7 to stack 1" << endl;
	a.push(1, 7);
	cout << "isEmpty 1: " << a.isEmpty(1) << endl;
	cout << "peek 1: " << a.peek(1) << endl;
	cout << "pop 1: " << a.pop(1) << endl;
	cout << "isEmpty 1: " << a.isEmpty(1) << endl;
	cout << "peek 1: " << a.peek(1) << endl;
	cout << "pop 1: " << a.pop(1) << endl;
	cout << "isEmpty 1: " << a.isEmpty(1) << endl;
	cout << "peek 1: " << a.peek(1) << endl;
	cout << "pop 1: " << a.pop(1) << endl;
	cout << "isEmpty 1: " << a.isEmpty(1) << endl;
	cout << "peek 1: " << a.peek(1) << endl;
	cout << "pop 1: " << a.pop(1) << endl;
	cout << "isEmpty 1: " << a.isEmpty(1) << endl;
	cout << "peek 1: " << a.peek(1) << endl;
	cout << "pop 1: " << a.pop(1) << endl;
	cout << "isEmpty 1: " << a.isEmpty(1) << endl;
	cout << "peek 1: " << a.peek(1) << endl;
	cout << "pop 1: " << a.pop(1) << endl;

	cout << "push 41 to stack 2" << endl;
	a.push(2, 41);
	cout << "push 42 to stack 2" << endl;
	a.push(2, 42);
	cout << "push 43 to stack 2" << endl;
	a.push(2, 43);
	cout << "push 44 to stack 2" << endl;
	a.push(2, 44);
	cout << "push 45 to stack 2" << endl;
	a.push(2, 45);
	cout << "push 46 to stack 2" << endl;
	a.push(2, 46);
	cout << "push 47 to stack 2" << endl;
	a.push(2, 47);
	cout << "isEmpty 2: " << a.isEmpty(2) << endl;
	cout << "peek 2: " << a.peek(2) << endl;
	cout << "pop 2: " << a.pop(2) << endl;
	cout << "isEmpty 2: " << a.isEmpty(2) << endl;
	cout << "peek 2: " << a.peek(2) << endl;
	cout << "pop 2: " << a.pop(2) << endl;
	cout << "isEmpty 2: " << a.isEmpty(2) << endl;
	cout << "peek 2: " << a.peek(2) << endl;
	cout << "pop 2: " << a.pop(2) << endl;
	cout << "isEmpty 2: " << a.isEmpty(2) << endl;
	cout << "peek 2: " << a.peek(2) << endl;
	cout << "pop 2: " << a.pop(2) << endl;
	cout << "isEmpty 2: " << a.isEmpty(2) << endl;
	cout << "peek 2: " << a.peek(2) << endl;
	cout << "pop 2: " << a.pop(2) << endl;
	cout << "isEmpty 2: " << a.isEmpty(2) << endl;
	cout << "peek 2: " << a.peek(2) << endl;
	cout << "pop 2: " << a.pop(2) << endl;

	cout << "push 331 to stack 3" << endl;
	a.push(3, 331);
	cout << "push 332 to stack 3" << endl;
	a.push(3, 332);
	cout << "push 333 to stack 3" << endl;
	a.push(3, 333);
	cout << "push 334 to stack 3" << endl;
	a.push(3, 334);
	cout << "push 335 to stack 3" << endl;
	a.push(3, 335);
	cout << "push 336 to stack 3" << endl;
	a.push(3, 336);
	cout << "push 337 to stack 3" << endl;
	a.push(3, 337);

	cout << "isEmpty 3: " << a.isEmpty(3) << endl;
	cout << "peek 3: " << a.peek(3) << endl;
	cout << "pop 3: " << a.pop(3) << endl;
	cout << "isEmpty 3: " << a.isEmpty(3) << endl;
	cout << "peek 3: " << a.peek(3) << endl;
	cout << "pop 3: " << a.pop(3) << endl;	
	cout << "isEmpty 3: " << a.isEmpty(3) << endl;
	cout << "peek 3: " << a.peek(3) << endl;
	cout << "pop 3: " << a.pop(3) << endl;	
	cout << "isEmpty 3: " << a.isEmpty(3) << endl;
	cout << "peek 3: " << a.peek(3) << endl;
	cout << "pop 3: " << a.pop(3) << endl;
	cout << "isEmpty 3: " << a.isEmpty(3) << endl;
	cout << "peek 3: " << a.peek(3) << endl;
	cout << "pop 3: " << a.pop(3) << endl;	
	cout << "isEmpty 3: " << a.isEmpty(3) << endl;
	cout << "peek 3: " << a.peek(3) << endl;
	cout << "pop 3: " << a.pop(3) << endl;

	return 0;
}