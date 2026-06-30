// Helper function for backtracking
void backtrack(int n, int open, int close, char* current, int index, char** result, int* returnSize) {
    if (open == n && close == n) {
        current[index] = '\0';
        result[*returnSize] = strdup(current);
        (*returnSize)++;
        return;
    }

    if (open < n) {
        current[index] = '(';
        backtrack(n, open + 1, close, current, index + 1, result, returnSize);
    }

    if (close < open) {
        current[index] = ')';
        backtrack(n, open, close + 1, current, index + 1, result, returnSize);
    }
}

char** generateParenthesis(int n, int* returnSize) {
    // Max combinations for n=8 is 1430 (Catalan number C_8). 
    char** result = (char**)malloc(1500 * sizeof(char*));
    *returnSize = 0;
    char* current = (char*)malloc((2 * n + 1) * sizeof(char));
    // Start backtracking from index 0, with 0 open and 0 close parentheses
    backtrack(n, 0, 0, current, 0, result, returnSize);

    free(current);
    return result;
}