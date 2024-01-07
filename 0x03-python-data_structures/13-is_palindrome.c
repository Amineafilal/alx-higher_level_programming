#include "lists.h"
/**
 * is_palindrome - function that checks ²singly linked list is a palindrome.
 * @head: input value
 * Return: 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	listint_t *prev;
	listint_t *temp;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	slow = *head;
	fast = *head;
	prev = NULL;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	while (prev != NULL && slow != NULL)
	{
		if (prev->val != slow->val)
		{
			return (0);
		}
		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}
