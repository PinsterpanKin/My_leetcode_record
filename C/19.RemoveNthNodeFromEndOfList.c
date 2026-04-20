//The application of dummy is to handle the edge case when the head node is removed.
 struct ListNode {
  int val;
  struct ListNode *next;
  };

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode *fast, *slow;
    struct ListNode* dummy=(struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->next=head;
    fast=dummy;
    slow=dummy;
    for(int i=0; i<n+1; i++){
        fast=fast->next;
    }
    while(fast){
        slow=slow->next;
        fast=fast->next;
    }
    slow->next=slow->next->next;
    return dummy->next;
}