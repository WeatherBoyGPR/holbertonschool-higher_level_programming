#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - will check for a cycle in a singly linked list
 * @list: a node in the list to check
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *head = NULL, *posi = NULL;

	head = list, posi = list;
	if (list != NULL)
	{
		while (posi != NULL && posi != NULL && posi->next != NULL)
		{
			head = head->next;
			posi = posi->next->next;
			if (head == posi)
				return (1);
		}
	}

	return (0);
}
