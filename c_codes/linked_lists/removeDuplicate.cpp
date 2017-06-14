#include <iostream>
#include <unordered_set>
#include <cstdlib>

using namespace std;

struct ListNode
{
	int key;
	struct ListNode *next;
};

void removeDuplicate(struct ListNode *head)
{
	struct ListNode *old;
	unordered_set<int> occurrence;

	if(!head)
	{
		return ;
	}

	occurrence.insert(head->key);
	while(head->next) 
	{
		if(occurrence.find(head->next->key) != occurrence.end())
		{
			old = head->next;
			head->next = head->next->next;
			delete old;
		}
		else
		{
			occurrence.insert(head->next->key);
			head = head->next;
		}
	}

	occurrence.clear();
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
	struct ListNode *head;

	seed = time(NULL);
	srand(seed);

	for(i = 0; i < 20; i++)
	{
		head = createLinkedList(i);

		cout << "-- Linked List --" << endl;
		printLinkedList(head);
		cout << endl;
		removeDuplicate(head);
		printLinkedList(head);
		cout << endl;

		freeLinkedList(head);
	}

	return 0;
}