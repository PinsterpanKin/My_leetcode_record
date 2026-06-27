#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Helper function for backtracking
void backtrack(int n, int open, int close, char* current, int index, char** result, int* returnSize) {
    // Base Case: If the current string reaches the maximum required length
    if (open == n && close == n) {
        current[index] = '\0'; // Null-terminate the string
        result[*returnSize] = strdup(current); // Duplicate and store it
        (*returnSize)++;
        return;
    }

    // Rule 1: Add an open parenthesis if we haven't reached the limit 'n'
    if (open < n) {
        current[index] = '(';
        backtrack(n, open + 1, close, current, index + 1, result, returnSize);
    }

    // Rule 2: Add a close parenthesis only if it won't violate well-formedness
    if (close < open) {
        current[index] = ')';
        backtrack(n, open, close + 1, current, index + 1, result, returnSize);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** generateParenthesis(int n, int* returnSize) {
    // Max combinations for n=8 is 1430 (Catalan number C_8). 
    // Allocating 2000 pointers is safe and sufficient for LeetCode constraints.
    int maxCombinations = 2000; 
    char** result = (char**)malloc(maxCombinations * sizeof(char*));
    *returnSize = 0;

    // Buffer to hold the current combination string dynamically
    char* current = (char*)malloc((2 * n + 1) * sizeof(char));

    // Start backtracking from index 0, with 0 open and 0 close parentheses
    backtrack(n, 0, 0, current, 0, result, returnSize);

    // Free the temporary buffer
    free(current);

    return result;
}