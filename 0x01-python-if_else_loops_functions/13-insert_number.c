#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: A pointer to a pointer to the head of the list
 * @number: The number to be inserted
 *
 * Return: Address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;
	listint_t *prev = NULL;

	if (new_node == NULL)
	{
		return (NULL);
	}

	/* Assign the given number to the new node's value */
	new_node->n = number;

	/* Traverse the list to find the correct position for insertion */
	while (current != NULL && current->n < number)
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
	{ /* Insert the new node between prev and current */
		prev->next = new_node;
		new_node->next = current;
	}

	return (new_node); /* Return the address of the new node */
}
