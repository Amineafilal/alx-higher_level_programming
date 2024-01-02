#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * Return: Always 0.
*/
int check_cycle(listint_t *list) 
{
	listint_t *slow = list;
	listint_t *fast = list;
	while (fast != NULL && fast->next != NULL) {
		slow = slow->next;         
		fast = fast->next->next;
		if (slow == fast) 
		{
			return (1);
		}
	}
	return (0);
}
/**
 * main - entry point
 * Return: Always 0.
*/
int main() 
{
	listint_t *head = NULL;
	head = (listint_t*)malloc(sizeof(listint_t));
	head->data = 1;
	head->next = (listint_t*)malloc(sizeof(listint_t));
	head->next->data = 2;
	head->next->next = (listint_t*)malloc(sizeof(listint_t));
	head->next->next->data = 3;
	head->next->next->next = head->next;  /* Creating a cycle */
	int result = check_cycle(head);
	if (result)
		printf("The linked list has a cycle.\n");
	else
		printf("The linked list does not have a cycle.\n");
	free(head->next->next);
	free(head->next);
	free(head);
	return (0);
}
