#include "lists.h"

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
		if (list == posi)
			return (1);

		do {
			posi = posi->next;
		} while (posi != NULL && posi != head);
	}
	if (posi != NULL)
		return (1);
	return (0);
}
