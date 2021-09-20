#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - will insert a value into a sorted list
 * @head: head of the list
 * @number: number to insert into list
 *
 * Return: the newly created node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *posi = NULL, *hold = NULL;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number, newnode->next = NULL;
	if (head != NULL)
		posi = *head;

	if (posi != NULL)
		while (newnode->n > posi->n && posi != NULL)
			hold = posi, posi = posi->next;
	if (hold == NULL)
	{
		if (head != NULL)
			newnode->next = *head;
		*head = newnode;
	}
	else
		hold->next = newnode, newnode->next = posi;

	return (newnode);
}
