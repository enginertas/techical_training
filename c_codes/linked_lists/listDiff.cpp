#include <iostream>
#include <unordered_map>

using namespace std;

#define TEST_COUNT 15
#define ARRAY_SIZE 20

struct ListNode
{
	int key;
	struct ListNode *next;
};

struct ListNode* listDiff(struct ListNode *head1, struct ListNode *head2)
{
	ListNode *result_head, *result_tail;
	unordered_map<int, int> element_map;

	// Allocate a dummy node
	result_head = result_tail = new struct ListNode;
	result_head->next = NULL;

	// Transfer integer occurrence counts into an unordered map
	while(head2)
	{
		if(element_map.find(head2->key) == element_map.end())
		{
			element_map[head2->key] = 1;
		}
		else
		{
			element_map[head2->key]++;
		}
		head2 = head2->next;
	}

	// Loop among first array, and create a node for each difference
	while(head1)
	{
		if(element_map.find(head1->key) == element_map.end())
		{
			result_tail->next = new struct ListNode;
			result_tail = result_tail->next;

			result_tail->next = NULL;
			result_tail->key = head1->key;
		}
		else
		{
			element_map[head1->key]--;
			if(!element_map[head1->key])
			{
				element_map.erase(head1->key);
			}
		}
		head1 = head1->next;
	}

	// Clear dummy node and map
	result_tail = result_head->next;	
	delete result_head;
	element_map.clear();

	// Return the constructed list
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
	int list1_length[TEST_COUNT] = {0, 1, 2, 10, 0, 0, 0, 1, 2, 3, 4, 5, 6, 6, 7};
	int list2_length[TEST_COUNT] = {0, 0, 0, 0, 1, 2, 10, 1, 2, 3, 4, 4, 5, 3, 6};
	int list1[TEST_COUNT][ARRAY_SIZE] = 
	{
		{},
		{1},
		{1, 2},
		{1, 1, 2, 2, 3, 3, 6, 6, 8, 9},
		{},
		{},
		{},
		{1},
		{1, 2},
		{1, 2, 3},
		{1, 1, 2, 2},
		{1, 1, 2, 2, 2},
		{1, 2, 2, 2, 1, 1},
		{3, 4, 4, 3, 2, 1},
		{4, 1, 3, 89, 2, 1, 3}
	};
	int list2[TEST_COUNT][ARRAY_SIZE] =
	{
		{},
		{},
		{},
		{},
		{1},
		{1, 2},
		{1, 1, 2, 2, 3, 3, 6, 6, 8, 9},
		{1},
		{1, 2},
		{1, 2, 3},
		{1, 1, 2, 2},
		{1, 1, 2, 2},
		{1, 2, 2, 1, 2},
		{3, 4, 1},
		{1, 7, 8, 8, 323, 3}
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
		cout << "(A - B): ";
		head_result = listDiff(head_a, head_b);
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