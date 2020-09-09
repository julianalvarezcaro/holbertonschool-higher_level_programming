#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: double pointer to the start of the list
 *
 * Return: 1 if a palindrome. 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int numbers[2048];
	int start, pos = 0;
	listint_t *node;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	node = *head;
	while (node)
	{
		numbers[pos] = node->n;
		node = node->next;
		pos++;
	}
	pos--;
	for (start = 0; start < pos; start++, pos--)
	{
		if (numbers[start] == numbers[pos])
		{
			continue;
		}
		else
			return (0);
	}
	return (1);
}
