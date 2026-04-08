//My original solution: unstable, dangerous for proficient level examination (leetcode refused)
#include <limits.h>
int myAtoi(char* s) {
    int n = strlen(s);
    int i, j;
    char result[n + 1];
    for (i = 0; i < n; i++) {
        if (s[i] >= '0' && s[i] <= '9' || s[i] == '-' || s[i] == '+') {
            for (j = i; j <= n; j++) {
                result[j - i] = s[j];
                if (j == i);
                else if (s[j] > '9' || s[j] < '0') {
                    result[j - i] = '\0';
                    return atoi(result);
                }
                if (atoi(result) > INT_MAX / 10 || (atoi(result) == INT_MAX / 10 && (s[j + 1] > '7' && s[j + 1] < '10'))) return INT_MAX;
                if (atoi(result) < INT_MIN / 10 || (atoi(result) == INT_MIN / 10 && (s[j + 1] > '8' && s[j + 1] < '10'))) return INT_MIN;
            }
        } else if ((s[i] > '9' || s[i] < '0') && s[i] != ' ') {
            return 0;
        }
    }
    return atoi(result);
}
//In above code, atoi() is called multiple times, which is inefficient and may cause overflow. 
//Below is a more efficient and safer implementation.

#include <limits.h>

int myAtoi(char *s) {
    int i = 0;
    int sign = 1;
    long result = 0;
    while (s[i] == ' ') {
        i++;
    }
    if (s[i] == '+' || s[i] == '-') {
        if (s[i] == '-') sign = -1;
        i++;
    }
    while (s[i] >= '0' && s[i] <= '9') {
        int digit = s[i] - '0';
        if (result > (INT_MAX - digit) / 10) {
            return sign == 1 ? INT_MAX : INT_MIN;
        }
        result = result * 10 + digit;
        i++;
    }
    return (int)(sign * result);
}