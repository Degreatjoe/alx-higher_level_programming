#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int elements[1000];
	int count = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (current != NULL)
	{
		elements[count] = current->n;
		current = current->next;
		count++;
	}

	for (i = 0; i < count / 2; i++)
	{
		if (elements[i] != elements[count - i - 1])
			return (0);
	}
	return (1);
}
