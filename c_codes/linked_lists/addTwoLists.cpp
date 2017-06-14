#include <iostream>
#include <cstdlib>

using namespace std;

#define TEST_COUNT 52
#define ARRAY_SIZE 10

struct ListNode
{
	int key;
	struct ListNode *next;
};

struct ListNode* addTwoLists(struct ListNode* list1, struct ListNode* list2)
{
	int carry = 0;
	struct ListNode *result_head, *result_tail;

	// Allocate a dummy node 
	result_head = result_tail = new struct ListNode;
	result_tail->next = NULL;

	// Traverse both lists until at least one list turned out to be NULL
	while(list1 && list2)
	{
		result_tail->next = new struct ListNode;
		result_tail = result_tail->next;

		carry += list1->key + list2->key;
		result_tail->key = carry % 10;
		result_tail->next = NULL;
		
		carry /= 10;
		list1 = list1->next;
		list2 = list2->next;
	}

	/**
		- If list1 is NOT NULL, continue with list1.
		- If list1 is NULL, continue with list2.
		- If both of them turned out to be NULL, it will not any cause problem
			because of the next NULL check below
	*/ 
	if(!list1)
	{
		list1 = list2;
	}

	// Traverse remaining elements in any of lists.
	while(list1)
	{
		result_tail->next = new struct ListNode;
		result_tail = result_tail->next;

		carry += list1->key;
		result_tail->key = carry % 10;
		result_tail->next = NULL;

		carry /= 10;
		list1 = list1->next;
	}

	// If there is a still a carry digit, append it to the end
	if(carry)
	{
		result_tail->next = new struct ListNode;
		result_tail = result_tail->next;

		result_tail->key = carry;
		result_tail->next = NULL;	
	}

	// Delete the dummy node
	result_tail = result_head->next;
	delete result_head;

	// Return the result list without dummy
	return result_tail;
}

struct ListNode* createLinkedList(int arr[], int size)
{
	int i;
	struct ListNode *new_node, *head = NULL;

	for(i = size - 1; i >= 0; i--)
	{
		new_node = new struct ListNode;
		new_node->key = arr[i];
		new_node->next = head;

		head=new_node;
	}

	return head;
}

void freeLinkedList(struct ListNode *head)
{
	struct ListNode *old;
	while(head)
	{
		old = head;
		head = head->next;
		delete old;
	}
}

void printLinkedList(struct ListNode *head)
{
	if(!head)
	{
		cout << "NULL ";
		return;
	}

	while(head)
	{
		cout << head->key << ' '; 
		head = head->next;
	}
}

void testSolution()
{
	struct ListNode *head_a, *head_b, *head_result;
	int i;
	
	int list1_length[TEST_COUNT] = 
	{
		0, 1, 1, 1, 2, 3, 6, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
		1, 2, 3, 6, 1, 1, 1, 1, 1, 1, 2, 1, 3, 1, 2, 2, 3, 2, 3, 2,
		5, 5, 5, 3, 2, 3, 6, 1, 1, 6, 8, 3, 6, 3
	};
	
	int list2_length[TEST_COUNT] = 
	{
		0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 3, 6, 1, 1, 2, 3, 6,
		1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 3, 2, 2, 2, 3, 2, 3,
		2, 3, 3, 5, 5, 5, 1, 6, 6, 1, 1, 8, 2, 6
	};
	
	int list1[TEST_COUNT][ARRAY_SIZE] = 
	{
		{},
		{0},
		{1},
		{8},
		{4, 1},
		{1, 3, 2},
		{1, 2, 3, 7, 8, 9},
		{},
		{},
		{},
		{},
		{},
		{},
		{0},
		{0},
		{0},
		{0},
		{0},
		{8},
		{3, 4},
		{4, 1, 3},
		{1, 2, 3, 7, 8, 9},
		{1},
		{1},
		{3},
		{9},
		{9},
		{8},
		{6, 1},
		{5},
		{9, 0, 1},
		{5},
		{3, 2},
		{8, 1},
		{9, 0, 1},
		{2, 9},
		{4, 3, 1},
		{6, 7},
		{1, 0, 9, 9, 1},
		{9, 0, 0, 9, 1},
		{7, 8, 3, 9, 1},
		{6, 8, 8},
		{9, 9},
		{1, 9, 9},
		{9, 9, 9, 9, 9, 1},
		{1},
		{6},
		{9, 9, 9, 9, 9, 1},
		{9, 9, 9, 9, 9, 9, 9, 9},
		{3, 2, 1},
		{9, 9, 9, 9, 9, 9},
		{3, 0, 2}
	};
	
	int list2[TEST_COUNT][ARRAY_SIZE] =
	{
		{},
		{},
		{},
		{},
		{},
		{},
		{},
		{0},
		{1},
		{8},
		{4, 1},
		{1, 3, 2},
		{1, 2, 3, 7, 8, 9},
		{0},
		{8},
		{3, 4},
		{4, 1, 3},
		{1, 2, 3, 7, 8, 9},
		{0},
		{0},
		{0},
		{0},
		{3},
		{9},
		{8},
		{9},
		{1},
		{3},
		{5},
		{6, 1},
		{5},
		{9, 0, 1},
		{8, 1},
		{3, 2},
		{2, 9},
		{9, 0, 1},
		{6, 7},
		{4, 3, 1},
		{9, 9},
		{1, 9, 9},
		{6, 8, 8},
		{7, 8, 3, 9, 1},
		{1, 0, 9, 9, 1},
		{9, 0, 0, 9, 1},
		{1},
		{9, 9, 9, 9, 9, 1},		
		{9, 9, 9, 9, 9, 1},
		{6},
		{1},
		{7, 7, 8, 9, 9, 9, 9, 9},
		{2, 1},
		{9, 9, 9, 9, 9, 9}
	};

	for(i = 0; i < TEST_COUNT; i++)
	{	
		cout << "--------------------------" << endl;
		head_a = createLinkedList(list1[i], list1_length[i]);
		head_b = createLinkedList(list2[i], list2_length[i]);

		cout << "List A: ";
		printLinkedList(head_a);
		cout << endl;
		cout << "List B: ";
		printLinkedList(head_b);
		cout << endl;
		cout << "(A + B): ";
		head_result = addTwoLists(head_a, head_b);
		printLinkedList(head_result);
		cout << endl;

		freeLinkedList(head_a);
		freeLinkedList(head_b);
		freeLinkedList(head_result);
	}
}

int main(int argc, char *argv[])
{
	testSolution();
	return 0;
}