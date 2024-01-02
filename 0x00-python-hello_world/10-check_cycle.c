#include "lists.h"
/**
 *  check_cycle - checks i linked list has a cycle
 *   @list: pointer to the head of the list
 *    Return: 0
 */
int check_cycle(listint_t *head)
{
	listint_t *slow_ptr, *fast_ptr;

	slow_ptr = head;
	fast_ptr = head;
	while (head && slow_ptr && fast_ptr && fast_ptr->next)
	{
		head = head->next;
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
		if (slow_ptr == fast_ptr)
		{
			head = head;
			slow_ptr = slow_ptr;
			while (1)
			{
				fast_ptr = slow_ptr;
				while (fast_ptr->next != head && fast_ptr->next != slow_ptr)
				{
					fast_ptr = fast_ptr->next;
				}
				if (fast_ptr->next == head)
					break;
				head = head->next;
			}
			return (1);
		}
	}
	return (0);
}
