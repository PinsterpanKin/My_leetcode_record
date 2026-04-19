//Take care! In C programming, the inside of the function is not allowed for another function definition, so we need to put the backtrack function outside of the letterCombinations function. 
//And we also need to declare the list array as a global variable, otherwise it will cause an error when we call the backtrack function.
#include <stdlib.h>
char* list[]={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
//the body of backtrack function
void backtrack(char* digits, int index, char* path, char** result, int* count){
    if(index==strlen(digits)){
        result[*count]=(char*)malloc(sizeof(char)*(strlen(digits)+1));
        strcpy(result[*count],path);
        (*count)++;
        return;
    }
    char* letters = list[digits[index]-'0'];
    for(int i=0; i<strlen(letters); i++){
        path[index]=letters[i];
        path[index+1]='\0';
        backtrack(digits, index+1, path, result, count);
    }
}

char** letterCombinations(char* digits, int* returnSize) {
    if(digits==NULL||strlen(digits)==0){//for none
        *returnSize=0;
        return NULL;
    }
    //initialization
    int n=strlen(digits);
    *returnSize=1;
    for(int i=0;i<n;i++){
        if(digits[i]=='7' || digits[i]=='9'){
            *returnSize*=4;
        }
        else{
            *returnSize*=3;
        }
    }
    //first layer pointer of result
    char** result=(char**)malloc(sizeof(char*)*(*returnSize));
    char* path=(char*)malloc(sizeof(char)*(n+1));
    int count=0;
    //apply backtrack function and enter the recursion
    backtrack(digits,0,path,result,&count);
    //when all completed,return result
    free(path);
    return result;
}