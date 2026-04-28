//Original code: for the second layer of for loop, the step of j should be T instead of 1, which can significantly reduce the time complexity from O(n^2) to O(n).
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
//My new code:
char* convert(char* s, int numRows) {
    int n=strlen(s), k=0, T=2*numRows-2;
    if(numRows==1 || numRows>=n) return s;
    char* result=(char*)malloc((n+1)*sizeof(char));
    for(int row=0;row<numRows;row++){
        for(int j=row;j<n;j+=T){
            result[k]=s[j];
            k++;
            if(row>0 && row<numRows-1 && j+T-2*row < n){
                result[k]=s[j+T-2*row];
                k++;
            }
        }
    }
    result[n]='\0';
    return result;
}