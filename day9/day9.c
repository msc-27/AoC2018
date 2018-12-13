/* Not familiar with any Python (or other) libraries suitable for a
 * linked list so rolled sleeves up and implemented a linked list
 * directly in C. Part 1 was doable with a simple list in Python.
*/
#include <stdio.h>
#include <stdlib.h>
#define LAST 7201900
#define PLAYERS 458
struct node {
	struct node *prev;
	struct node *next;
	int val;
};

int main(void) {
	int player = 0;
	long long scores[PLAYERS] = {0};
	struct node* current = malloc(sizeof *current);
	current->prev = current;
	current->next = current;
	current->val = 0;
	for (int marb = 1; marb <= LAST; marb++) {
		if((marb % 23) != 0) {
			current = current->next;
			struct node* newnode = malloc(sizeof *newnode);
			newnode->val = marb;
			newnode->prev = current;
			newnode->next = current->next;
			current->next->prev = newnode;
			current->next = newnode;
			current = newnode;
		} else {
			scores[player] += marb;
			current = current->prev;
			current = current->prev;
			current = current->prev;
			current = current->prev;
			current = current->prev;
			current = current->prev;
			current = current->prev;
			scores[player] += current->val;
			current->next->prev = current->prev;
			current->prev->next = current->next;
			current = current->next;
		/* Didn't bother freeing memory for removed node */
		}
		player++;
		player %= PLAYERS;
	}
	long long winscore = 0;
	for (int i = 0; i < PLAYERS; i++) if (scores[i] > winscore) winscore = scores[i];
	printf("%lld\n", winscore);
}
