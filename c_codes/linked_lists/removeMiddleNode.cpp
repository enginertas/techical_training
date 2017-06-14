#include <iostream>
#include <cstdlib>

using namespace std;

struct ListNode
{
	int key;
	struct ListNode *next;
};

bool removeMiddleNode(struct ListNode *node)
{
	struct ListNode *old_node;

	if(!node || !node->next)
	{
		return false;
	}

	old_node = node->next;
	node->key = old_node->key;
	node->next = old_node->next;
	delete old_node;

	return true;
}

struct ListNode* createLinkedList(int size)
{
	int i;
	struct ListNode *new_node, *head = NULL;

	for(i = 0; i < size; i++)
	{
		new_node = new struct ListNode;
		new_node->key = rand() % 10;
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
	while(head)
	{
		cout << head->key << ' '; 
		head = head->next;
	}
}

int main(int argc, char *argv[])
{
	int i, seed;
	struct ListNode *head, *cur_node;

	seed = time(NULL);
	srand(seed);

	head = createLinkedList(15);

	cout << "----------------------------------------" << endl;
	cout << "Original List: " << endl;
	printLinkedList(head);
	cout << endl;

	cout << "----------------------------------------" << endl;
	cout << "After deleting nothing: ";
	cout << removeMiddleNode(NULL) << endl;
	printLinkedList(head);
	cout << endl;

	cout << "----------------------------------------" << endl;
	cout << "After deleting the last element: ";
	cur_node = head;
	for(i = 1; i < 15; i++)
	{
		cur_node = cur_node->next;
	}
	cout << removeMiddleNode(cur_node) << endl;
	printLinkedList(head);
	cout << endl;

	cout << "----------------------------------------" << endl;
	cout << "After deleting the second to the last element: ";
	cur_node = head;
	for(i = 1; i < 14; i++)
	{
		cur_node = cur_node->next;
	}
	cout << removeMiddleNode(cur_node) << endl;	
	printLinkedList(head);
	cout << endl;

	cout << "----------------------------------------" << endl;
	cout << "After deleting the 5th element: ";
	cur_node = head;
	for(i = 1; i < 5; i++)
	{
		cur_node = cur_node->next;
	}
	cout << removeMiddleNode(cur_node) << endl;	
	printLinkedList(head);
	cout << endl;

	cout << "----------------------------------------" << endl;
	cout << "After deleting the first element: ";
	cout << removeMiddleNode(head) << endl;
	printLinkedList(head);
	cout << endl;

	freeLinkedList(head);

	return 0;
}