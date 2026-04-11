//easy
char* longestCommonPrefix(char** strs, int strsSize) {
    int first_length=strlen(strs[0]);
    int i=0,j=0,k=0;
    int isDifferent=0;
    char* first=strs[0];
    char* Result=(char*)malloc(first_length+1);
    while(i<first_length){
        char compare= first[i];
        for(j=1;j<strsSize;j++){
            char* target=strs[j];
            if(compare!=target[i]||target[i]=='\0'){
                isDifferent=1;
                break;
            }
        }
        if(isDifferent) break;
        i++;
    }
    char* empty=(char*)malloc(1);
    empty[0]='\0';
    if(i==0) return empty;
    for(k=0;k<i;k++){
        Result[k]=first[k];
    }
    Result[i]='\0';
    return Result;
}