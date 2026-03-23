struct ListNode* middleNode(struct ListNode* head) {
    
    struct ListNode* weak = head;
    struct ListNode* strong = head;

    while (strong && strong->next) {
        weak = weak->next;          
        strong = strong->next->next;    
    }

    return weak;
}
