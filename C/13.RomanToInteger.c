//easy
#include<string.h>
static int rec(char input){
    switch(input){
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
    }
    return 0;
}

int romanToInt(char* s) {
    int length=strlen(s);
    int sum=0;
    for(int i=0;i<length;i++){
        int this_value=rec(s[i]);
        int next_value= (i+1 < length)? rec(s[i+1]) : 0;
        sum=sum+((this_value>=next_value)? rec(s[i]) : -rec(s[i]));
    }
    return sum;
}