#include "lists.h"

/**
  * check_cycle - checks if a linked list has a cycle
  *
  * @list: linked list
  *
  * Return: 0 if no cycle. 1 if cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *curr = list;

	while (curr)
	{
		if (curr->next == list)
		{
			return (1);
		}
		curr = curr->next;
	}
	return (0);
}
