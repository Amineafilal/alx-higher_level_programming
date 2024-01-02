#include "lists.h"
/**
 * insert_node - Inserts a value into a sorted singly-linked list
 * @head: A pointer to the head of the linked list
 * @number: The value to insert
 * Return: NULL in case of failure, a pointer to the new node otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (current_node == NULL || current_node->n >= number)
	{
		new_node->next = current_node;
		*head = new_node;
		return (new_node);
	}

	while (current_node && current_node->next && current_node->next->n < number)
		current_node = current_node->next;

	new_node->next = current_node->next;
	current_node->next = new_node;
	return (new_node);
}
