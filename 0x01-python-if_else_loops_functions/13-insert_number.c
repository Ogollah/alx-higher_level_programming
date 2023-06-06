#include "lists.h"

/**
 *insert_node - Inserts a number into a singly linked list.
 *@head: Pointer to a pointer to the head of the list.
 *@number: Number to be inserted.
 *Return: Address of the new node else NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *current = *head;
	listint_t *prev = NULL;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	while (current != NULL && current->n <= number)
	{
		prev = current;
		current = current->next;
	}

	if (prev == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		new_node->next = current;
		prev->next = new_node;
	}
	return (new_node);
}
