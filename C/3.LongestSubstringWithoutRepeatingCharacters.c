// my stupid original solution with violence
int lengthOfLongestSubstring_original(char* s) {
    int n=strlen(s);
    if(!n) return 0;
    char target[n+1];
    memset(target, 0, sizeof(target));
    int max=1, count=0, is_repeat=0, i=0, j=0, k=0;
    for(i=0;i<n;i++){
        for(k=i;k<n;k++){
            while(target[j]){
                if(s[k]==target[j]){
                    is_repeat=1;
                    j=0;
                    break;
                }
                j++;
            }
            if(!is_repeat){
                j=0;
                target[count]=s[k];
                count++;
            }
            else{
                is_repeat=0;
                if(count>max) max=count;
                count=0;
                memset(target, 0, sizeof(target));
                break;
            }
        }
    }
    return max;
}
/*Analysis: The above code uses a brute-force approach to find the longest substring 
without repeating characters. 
It iterates through each character in the string and checks for duplicates by maintaining a target array.
If a duplicate is found, it resets the count and target array.
This approach has a time complexity of O(n^2) in the worst case, which can be inefficient for long strings. 
*/
/*A more efficient solution would involve using a sliding window technique with a hash set to track characters in the current window, 
achieving a time complexity of O(n).
*/
int lengthOfLongestSubstring(char* s) {
    int n = strlen(s);
    if (n == 0) return 0;

    int max = 0;
    int left = 0;
    int right = 0;
    int charSet[128] = {0}; // Assuming ASCII character set

    while (right < n) {
        if (charSet[s[right]] == 0) {
            charSet[s[right]] = 1; // Mark the character as seen
            right++;
            max = (right - left > max) ? right - left : max; // Update max length
        } else {
            charSet[s[left]] = 0; // Unmark the character at left pointer
            left++; // Move the left pointer to the right
        }
    }

    return max;
}