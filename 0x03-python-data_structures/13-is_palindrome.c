#include "lists.h"
/**
 * is_palindrome - function that checks ²singly linked list is a palindrome.
 * @head: pointer to the head of the list
 * Return: 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	listint_t *prev;
	listint_t *second_h;
	int is_pali = 1;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	slow = *head;
	fast = *head;
	prev = *head;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	second_h = reverse_list(slow);
	while (second_h != NULL)
	{
		if ((*head)->n != second_h->n)
		{
			is_pali = 0;
			break;
		}
		*head = (*head)->next;
		second_h = second_h->next;
	}
	prev->next = reverse_list(second_h);
	return (is_pali);
}
/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current;
	listint_t *next;
	
	current = head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}
