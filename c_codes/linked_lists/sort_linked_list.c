#include <stdio.h>

void free(void* p);
void* malloc(size_t size);

typedef struct node
{
	int key;
	struct node* next;
} node;


node * createLinkedList(int buffer[], int len)
{
	node *p, *head = NULL;

	if(len <= 0)
	{
		return NULL;
	}

	for(len--; len >= 0; len--)
	{
		p = (node *) malloc(sizeof(node));
		p->next = head;
		p->key = buffer[len];
		head = p;
	}

	return head;
}


void printLinkedList(node * head)
{
	if(head)
	{
		while(head)
		{
			printf("%d ", head->key);
			head = head->next;
		}
	}
	else
	{
		printf("NULL");
	}
	printf("\n");
}


void freeLinkedList(node * head)
{
	node *tmp, *p;
	if(head)
	{
		p = head;
		while(p)
		{
			tmp = p->next;
			free(p);
			p = tmp;
		}
	}
}


void bubbleSort(node * head)
{
	int tmp, is_sorted;
	node *first, *second;

	if(!head)
	{
		return;
	}

	do
	{
		is_sorted = 1;
		for(first = head, second = head->next; second; first = first->next, second = second->next)
		{
			if(first->key > second->key)
			{
				tmp = first->key;
				first->key = second->key;
				second->key = tmp;
				is_sorted = 0;
			}
		}
	} while(!is_sorted);
}


node * merge(node * head1, node * head2)
{
	node *head_new, *p;

	head_new = (node *) malloc(sizeof(node));
	head_new->next = NULL;

	p = head_new;
	while(head1 || head2)
	{
		p->next = (node *) malloc(sizeof(node));
		p = p->next;
		p->next = NULL;
	
		if(head1 && head2)
		{
			if(head1->key < head2->key)
			{
				p->key = head1->key;
				head1 = head1->next;
			}
			else
			{
				p->key = head2->key;
				head2 = head2->next;
			}
		}
		else if(head1)
		{
			p->key = head1->key;
			head1 = head1->next;
		}
		else if(head2)
		{
			p->key = head2->key;
			head2 = head2->next;			
		}
	}

	p = head_new;
	head_new = head_new->next;
	free(p);
	return head_new;
}


node * mergeSortHelper(node * head, int len)
{
	int i, small, big, len1, len2;
	struct node *p, *head2;

	if(len == 1)
	{
		p = (node *) malloc(sizeof(node));
		p->key = head->key;
		p->next = NULL;
		return p;
	}

	if(len == 2)
	{
		if(head->key < head->next->key)
		{
			small = head->key;
			big = head->next->key;
		}
		else
		{
			big = head->key;
			small = head->next->key;			
		}

		p = (node *) malloc(sizeof(node));
		p->key = small;
		p->next = (node *) malloc(sizeof(node));
		p->next->key = big;
		p->next->next = NULL;
		return p;
	}

	len1 = len / 2;
	len2 = len - len1;
	head2 = head;
	for(i = 0; i < len1; i++)
	{
		head2 = head2->next;
	}

	return merge(mergeSortHelper(head, len1), mergeSortHelper(head2, len2));
}

node * mergeSort(node * head)
{
	node * p;
	int len = 0;
	if(!head)
	{
		return NULL;
	}

	for(p = head; p; p = p->next)
	{
		len++;
	}

	return mergeSortHelper(head, len);
}


int main(void)
{
	int i;
	int buffer[14] = {2, 3, 5, 4, 7, 9, 2, 6, 6, 5, 3, 1, 1, 0};
	node *linked_list, *new_linked_list;

	for (i = 0; i <= 14; i++)
	{
		linked_list = createLinkedList(buffer, i);
		printf("Bubble Sort:\n");
		printLinkedList(linked_list);
		bubbleSort(linked_list);
		printLinkedList(linked_list);
		freeLinkedList(linked_list);
	}

	printf("\n-----------\n\n");

	for (i = 0; i <= 14; i++)
	{
		linked_list = createLinkedList(buffer, i);
		printf("Merge Sort:\n");
		printLinkedList(linked_list);
		new_linked_list = mergeSort(linked_list);
		printLinkedList(new_linked_list);
		freeLinkedList(linked_list);
		freeLinkedList(new_linked_list);
	}

	return 0;
}