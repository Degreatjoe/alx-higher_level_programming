#include <stdio.h>
#include "lists.h" // Include the header file where dlistint_t is defined

size_t print_dlistint(const dlistint_t *h) {
    size_t count = 0; // Initialize a counter for the number of nodes

    // Iterate through the list
    while (h != NULL) {
        printf("%d\n", h->n); // Print the value of the current node
        h = h->next; // Move to the next node
        count++; // Increment the counter
    }

    return count; // Return the number of nodes
}
