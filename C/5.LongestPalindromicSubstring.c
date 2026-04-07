/*Originally I condiered applying two pointers starting from both ends of the sting
      but it failed on ensuring the substring to be largest.
  So I decided to use center expansion method, which is more intuitive and easier to implement.
*/
int expand(char* s, int left, int right, int n) {
    while (left >= 0 && right < n && s[left] == s[right]) {
        left--;
        right++;
    }
    return right - left - 1;
}

/**
 * time complexity: O(n^2) || space complexity: O(1)
 */
char* longestPalindrome(char* s) {
    int length = strlen(s);
    if (length <= 1) return s;

    int result_head = 0;
    int max = 0;

    for (int i = 0; i < length; i++) {
        // if the center is a single character, the length of palindrome is odd
        int len1 = expand(s, i, i, length);
        // if the center is between two characters, the length of palindrome is even
        int len2 = expand(s, i, i + 1, length);

        int temp = len1 > len2 ? len1 : len2;

        if (temp > max) {
            max = temp;
            result_head = i - (temp - 1) / 2;
        }
    }
    //make sure that the return value is valid !!!
    char* result = (char*)malloc(sizeof(char) * (max + 1));
    
    // strncpy is high efficient
    strncpy(result, s + result_head, max);
    result[max] = '\0'; // remember to add null *terminator*

    return result;
}