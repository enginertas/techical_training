#include <iostream>
#include <cstdlib>

using namespace std;

struct ListNode
{
	int key;
	struct ListNode *next;
};

void reverseList(struct ListNode *&head_ref)
{
	struct ListNode *next_node;
	struct ListNode *tail = NULL;
	struct ListNode *current = head_ref;

	while(current)
	{
		next_node = current->next;
		current->next = tail;

		tail = current;
		current = next_node;
	}

	head_ref = tail;
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

int main(int argc, char *argv[])
{
	int i, seed;
	struct ListNode* head;

	seed = time(NULL);
	srand(seed);

	for(i = 0; i < 10; i++)
	{
		cout << "---------------------------------" << endl;
		head = createLinkedList(i);

		cout << "Original List: ";
		printLinkedList(head);
		cout << endl;

		cout << "Reversed List: ";
		reverseList(head);
		printLinkedList(head);
		cout << endl;

		freeLinkedList(head);
	}

	
	return 0;
}