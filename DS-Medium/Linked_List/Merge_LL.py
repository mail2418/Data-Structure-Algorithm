"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = head =  ListNode()
        while list1 and list2:
            if list1.val < list2.val :
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return head.next
            
if __name__ == "__main__":
    listnode1_1 = ListNode(1)
    listnode1_2 = ListNode(2)
    listnode1_4 = ListNode(4)
    listnode2_1 = ListNode(1)
    listnode2_3 = ListNode(3)
    listnode2_4 = ListNode(4)

    listnode1_1.next = listnode1_2
    listnode1_2.next = listnode1_4
    listnode2_1.next = listnode2_3
    listnode2_3.next = listnode2_4

    new_list = Solution().mergeTwoLists(listnode1_1,listnode2_1)
    res = []
    while new_list :
        res.append(new_list.val)
        new_list = new_list.next
    print(res)