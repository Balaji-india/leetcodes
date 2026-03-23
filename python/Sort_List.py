struct ListNode* merge(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode dummy;
    struct ListNode*temp=&dummy;
    dummy.next=NULL;
    while(l1 && l2){
        if(l1->val<l2->val){
            temp->next=l1;
            l1=l1->next;
        }
        else{
            temp->next=l2;
            l2=l2->next;
        }
        temp=temp->next;
    }
    if(l1){
        temp->next=l1;
    }
    else{
        temp->next=l2;
    }
    return dummy.next;
}
struct ListNode* sortList(struct ListNode* head) {
    if(!head||!head->next){
        return head;
    }
    struct ListNode *slow = head, *fast = head, *prev = NULL;
    while(fast && fast->next){
        prev=slow;
        slow=slow->next;
        fast=fast->next->next;
    }
    prev->next=NULL;
    struct ListNode* left = sortList(head);
    struct ListNode* right = sortList(slow);
    return merge(left,right);
}
    
