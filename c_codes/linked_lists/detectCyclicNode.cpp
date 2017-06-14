#include <iostream>
#include <cstdlib>

using namespace std;

#define TEST_SUITE_COUNT 10

struct ListNode
{
	int key;
	struct ListNode *next;
};

struct ListNode* detectCyclicNode(struct ListNode *head)
{
	struct ListNode *slow_ptr, *fast_ptr;

	slow_ptr = head;
	fast_ptr = head;
	while(fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
		if(slow_ptr == fast_ptr)
		{
			break;
		}
	}

	if(!fast_ptr || !fast_ptr->next)
	{
		return NULL;
	}

	fast_ptr = head;
	while(slow_ptr != fast_ptr)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next;
	}

	return fast_ptr;
}

/**
 * The function that creates a cyclic linked list
 * 		cycle_start_index < 0 -> generates non-cyclic list
 */
struct ListNode* createCyclicLinkedList(int size, int cycle_start_index)
{
	int i;
	struct ListNode *head;
	struct ListNode *tail;
	struct ListNode *cycle_start = NULL;

	// If size is not positive, quickly return NULL
	if(size <= 0)
	{
		return NULL;
	}

	// Create a starting node
	head = tail = new struct ListNode;
	head->key = rand() % 10;
	head->next = NULL;

	// If cycle start index is 0, set head node as cycle start
	if(!cycle_start_index)
	{
		cycle_start = head;
	}

	// Create remaining elements and append them into tail
	for(i = 1; i < size; i++)
	{
		tail->next = new struct ListNode;
		tail = tail->next;

		tail->key = rand() % 10;
		tail->next = NULL;

		// If index is cycle start index, set current node for cycle start node
		if(i == cycle_start_index)
		{
			cycle_start = tail;
		}
	}

	// If setting cycle start is succesful, append its pointer to the end
	if(cycle_start)
	{
		tail->next = cycle_start;
	}

	return head;
}

void printCyclicLinkedList(struct ListNode *head, int size)
{
	int i;

	if(!head)
	{
		cout << "NULL ";
	}

	for(i = 0; i < size; i++)
	{
		cout << head->key << ' ';
		head = head->next;
	}

	if(head)
	{
		cout << "\t Cycle: " << head->key;
	}
}

void printCyclicNode(struct ListNode *head)
{
	if(head)
	{
		cout << head->key << ' ';
	}
	else
	{
		cout << "NULL";	
	}
}

void freeLinkedList(struct ListNode *head, int size)
{
	int i;
	struct ListNode *old;
	
	for(i = 0; i < size; i++)
	{
		old = head;
		head = head->next;
		delete old;		
	}
}

int main(int argc, char *argv[])
{
	int i, j, upper_bound;
	struct ListNode *head, *cyclic;

	int list_size[TEST_SUITE_COUNT] = 
	{
		0, 1, 2, 3, 4, 5, 10, 11, 42, 43
	};

	for(i = 0; i < TEST_SUITE_COUNT; i++)
	{
		for(j = -1; j <= list_size[i]; j++)
		{
			head = createCyclicLinkedList(list_size[i], j);

			cout << "-------------------------" << endl;
			cout << "Original List (" << list_size[i] << ", " << j << ')' << endl;
			printCyclicLinkedList(head, list_size[i]);
			cout << endl;

			cyclic = detectCyclicNode(head);
			cout << "Detection: ";
			printCyclicNode(cyclic);
			cout << endl;

			freeLinkedList(head, list_size[i]);
		}
	}
	return 0;
}