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

/**
 * insert_node - fuction name
 * @**head: parameter
 * @number: parameter
 *
 * Return: adress of node created
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insert;

	listint_t *new_node = createNode(number);
	
	if (new_node == NULL)
	{
		return (NULL);
	}

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	insert = *head;

	while (insert->next != NULL && insert->next->n < number)
	{
		insert = insert->next;
	}
	new_node->next = insert->next;
	insert->next = new_node;
	return new_node;
}
