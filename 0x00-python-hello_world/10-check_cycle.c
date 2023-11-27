#include "list.h"
#include <stdio.h>
#include <stdlib.h>

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: a pointer to the first node of the list
*
* Description: This function takes a pointer to the first node
*
* Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}

	return (0);
}
