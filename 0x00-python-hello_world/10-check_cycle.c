#include "lists.h"

/**
 * check_cycle - this function checks cycle
 * @list: pointer to the list
 * Return: 0 if there is no cycle 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	struct ListNode *slow = head, *fast = head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
