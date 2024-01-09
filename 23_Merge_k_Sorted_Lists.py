# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        united_lists = []
        head = n = ListNode(0)
        
        #running through all linkes lists
        for i in range(len(lists)):
            while lists[i]!= None:
                #appending and uniting all linked lists values
                united_lists.append(lists[i].val)
                #creating the 'next' lable for each node
                lists[i]=lists[i].next

        #sorting the united lists
        united_lists.sort()
        for i in range(len(united_lists)):
            #placing the next node value
            n.next=ListNode(united_lists[i])
            #pointing to the next node
            n=n.next
        
        #returning the head of the new sorted merged linked list
        return head.next