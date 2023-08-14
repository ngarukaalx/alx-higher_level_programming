#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * createNode - parameter
 * @n: parameter
 *
 * Return: newnode
 */

listint_t* createNode(int n)
{
	listint_t* newNode = (listint_t*)malloc(sizeof(listint_t));
	if (newNode != NULL)
	{
		newNode->n = n;
		newNode->next = NULL;
	}
	return newNode;
}
