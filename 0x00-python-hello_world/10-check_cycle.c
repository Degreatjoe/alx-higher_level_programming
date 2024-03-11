#include "lists.h"
/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: Pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;


	if (list == NULL || list->next == NULL)
	{
		return (0); /* No cycle if list is empty or has only one node */
	}

	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		{
			return (1); /* Cycle detected */
		}
		slow = slow->next;
		fast = fast->next->next;
	}

	return (0); /* No cycle found */
}
