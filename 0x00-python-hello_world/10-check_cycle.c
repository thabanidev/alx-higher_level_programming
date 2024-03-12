#include "lists.h"

/**
 * check_cycle: Checks if a singly-linked list has a cycle
 * @list: list to check
 *
 * Return: 1 if YES or 0 if NO
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (!list)
		return 0;

	slow = list;
	fast = list->next;

	while (fast && fast->next)
	{
		if (fast == slow)
			return 1;
		fast = fast->next->next;
		slow = slow->next;
	}

	return 0;
}
