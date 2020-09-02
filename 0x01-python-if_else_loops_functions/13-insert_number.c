#include "lists.h"

/**
 * insert_node - inserts a node in a linked list
 *
 * @head: double pointer to the list
 * @number: int that the new node will have
 *
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *curr, *next;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	if (*head == NULL)
		addthenode(node, *head);

	curr = *head;
	next = curr->next;

	node->n = number;
	while (next)
	{
		if (next->n >= number)
		{
			addthenode(node, curr);
			return (node);
		}
		curr = next;
		next = next->next;
	}
	addthenode(node, curr);
	return (node);
}

/**
 * addthenode - adds a node to a liked list
 *
 * @node: node to be added
 * @curr: node after which node must be added
 *
 * Return: void
 */
void addthenode(listint_t *node, listint_t *curr)
{
	node->next = curr->next;
	curr->next = node;
}
