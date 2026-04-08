char* convert(char* s, int numRows) {
    int n = strlen(s), k = 0, T = 2 * numRows - 2;
    if (numRows == 1 || numRows >= n) return s;
    char* result = (char*)malloc((n + 1) * sizeof(char));
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < n; j++) {
            if ((j - i) % T == 0 || (j + i) % T == 0) {
                result[k] = s[j];
                k++;
            }
        }
    }
    result[n] = '\0';
    return result;
}