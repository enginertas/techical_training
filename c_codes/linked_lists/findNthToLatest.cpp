#include <iostream>
#include <cstdlib>

using namespace std;

struct ListNode
{
	int key;
	struct ListNode *next;
};

struct ListNode* findNthToLatest(struct ListNode *head, int n)
{
	int i;
	struct ListNode* nptr;

	if(!head || n < 1)
	{
		return NULL;
	}

	nptr = head;
	for(i = 0; i < n && head; i++)
	{
		head = head->next;
	}

	if(i != n)
	{
		return NULL;
	}

	while(head)
	{
		nptr = nptr->next;
		head = head->next;
	}

	return nptr;
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
	struct ListNode *head, *nptr;

	seed = time(NULL);
	srand(seed);

	for(i = 0; i < 20; i++)
	{
		head = createLinkedList(i);

		cout << "-- Linked List --" << endl;
		printLinkedList(head);
		cout << endl;

		nptr = findNthToLatest(head, 0);
		if(nptr)
		{
			cout << nptr->key << endl;			
		}

		freeLinkedList(head);
	}

	return 0;
}