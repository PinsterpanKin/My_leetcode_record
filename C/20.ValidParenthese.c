#include<stdlib.h>
#include<string.h>
#include<stdbool.h>
typedef struct node{
    char data;
    struct node* next;
}node;

typedef struct stack{
    node* topone;
}stack;

stack* create(void){
    stack* the_top=(stack*)malloc(sizeof(stack));
    if(!the_top) return NULL;
    the_top->topone=NULL;
    return the_top;
}

void put_in(stack* the_top, char input){
    node* newone=(node*)malloc(sizeof(node));
    newone->data=input;
    newone->next=the_top->topone;
    the_top->topone=newone;
}

char take_out(stack* the_top){
    if (the_top->topone==NULL){
        return '\0';
    }
    node* take_one=the_top->topone;
    char target=take_one->data;
    the_top->topone=the_top->topone->next;
    free(take_one);
    return target;
}

bool isValid(char* s) {
    int length=strlen(s);
    int i=0;
    stack* the_stack=create();
    char container;
    char target;
    if(length%2==1) return false;
    if(s[0]==')'||s[0]==']'||s[0]=='}') return false;
    if(s[length-1]=='('||s[length-1]=='['||s[length-1]=='{') return false;
    for(i=0;i<length;i++){
        container=s[i];
        if(container=='('||container=='['||container=='{'){
            put_in(the_stack, container);
            continue;
        }
        if(container==')'){
            target=take_out(the_stack);
            if(target!='(') return false;
            continue;
        }
        if(container==']'){
            target=take_out(the_stack);
            if(target!='[') return false;
            continue;
        }
        if(container=='}'){
            target=take_out(the_stack);
            if(target!='{') return false;
            continue;
        }
    }
    if(the_stack->topone!=NULL) return false;
    return true;
}