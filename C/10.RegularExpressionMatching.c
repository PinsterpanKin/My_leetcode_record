//Very hard for me, I originally used linear pointer approach 
//but just couldn't write proper solution to deal with the rest elements of p
#include <stdio.h>
bool isMatch(char* s, char* p) {
    int l1 = strlen(s), l2 = strlen(p);
    int i, j = 0, k;
    if (l1 == 0 && l2 == 0) return true;
    if (l1 == 0 || l2 == 0) return false;

    // match the first character of s with p, and move j to the first character that is not * or the first character that matches s[0]
    while (j < l2) {
        if (s[0] == p[j] || p[j] == '.') {
            j++;
            break;
        }
        if (j > 0 && p[j] == '*') {
            j++;
            continue;
        }
        //if current character in p is not * and does not match s[0], then if the next character in p is not *, return false, else move j to the next character
        if (j == l2 - 1) return false;
        if (s[0] != p[j] && p[j] != '.') {
            if (p[j + 1] != '*') return false;
            else {
                j++;
            }
        }
    }

    // match the rest characters of s with p, if current character in p is *, then move j to the first character that is not * or the first character that matches s[i], if current character in p is not * and does not match s[i], then if the next character in p is not *, return false, else move j to the next character
    for (i = 1; i < l1; i++) {
        if (p[j] == '*') {
            k = j;
            while (p[k] == '*') k--;
            if (s[i] != p[k] && p[k] != '.') {
                i--;
                j++;
                continue;
            } else continue;
        } else {
            if (s[i] != p[j] && p[j] != '.') {
                if (j < l2 - 2) {
                    if (p[j + 1] == '*') {
                        j += 2;
                        i--;
                        continue;
                    }
                }
                return false;
            } else {
                j++;
            }
        }
    }
    // --- to be completed (not yet, give up already...) ---

//genius solution after I gave up the prevous one
bool isMatch(char* s, char* p) {
    int n = strlen(s);
    int m = strlen(p);
    bool dp[n + 1][m + 1];
    memset(dp, false, sizeof(dp));
    dp[0][0] = true;
    for (int j = 2; j <= m; j++) {
        if (p[j - 1] == '*') {
            dp[0][j] = dp[0][j - 2];
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (p[j - 1] == s[i - 1] || p[j - 1] == '.') {
                dp[i][j] = dp[i - 1][j - 1];
            } 
            else if (p[j - 1] == '*') {
                dp[i][j] = dp[i][j - 2];
                if (p[j - 2] == s[i - 1] || p[j - 2] == '.') {
                    dp[i][j] = dp[i][j] || dp[i - 1][j];
                }
            }
        }
    }

    return dp[n][m];
}