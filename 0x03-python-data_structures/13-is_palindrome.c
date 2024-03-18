#include "lists.h"
#include <stdio.h>

void reverse_lists(listint_t **head);
int compare_lists(listint_t *head, listint_t *middle, int length);

/**
 * is_palindrome - A function that checks if a list is a palindrome
 * @head: A pointer to the first node
 * Return: 1 if a palindrome otherwise, 0
 */
int is_palindrome(listint_t **head)
{
	int length;
	int a;
	listint_t *tmp;
	listint_t *middle;

	if (head == NULL || *head == NULL)
		return (1);
	tmp = *head;
	middle = *head;

	for (length = 0; tmp != NULL; length++)
		tmp = tmp->next;
	length = length / 2;

	for (a = 1; a < length; a++)
		middle = middle->next;
	if (length % 2 != 0 && length != 1)
	{
		middle = middle->next;
		length = length - 1;
	}
	reverse_lists(&middle);
	a = compare_lists(*head, middle, length);

	return (a);
}
/**
 * compare_lists - function that compare two lists
 * @head: pointer to th first node
 * @middle: Pointer to the middle node
 * @length: length of the list
 * Return: 1 if are same otherwise 0
 */
int compare_lists(listint_t *head, listint_t *middle, int length)
{
	int a;

	if (head == NULL || middle == NULL)
		return (1);
	for (a = 0; a < length; a++)
	{
		if (head->n != middle->n)
			return (0);
		head = head->next;
		middle = middle->next;
	}
	return (1);
}
/**
 * reverse_lists - A function that reverse the list
 * @head: a pointer to the first node
 *
 * Return: void
 */
void reverse_lists(listint_t **head)
{
	listint_t *recent;
	listint_t *next;
	listint_t *previous;

	if (head == NULL || *head == NULL)
		return;
	previous = NULL;
	recent = *head;
	while (recent != NULL)
	{
		next = recent->next;
		recent->next = previous;
		previous = recent;
		recent = next;
	}
	*head = previous;
}
