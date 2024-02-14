"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""

from typing import Optional,List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: 
            return None
        def merge_two_lists(l1, l2):
            dummy = ListNode()
            curr = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next
        
        # divide and conquer
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    merged_lists.append(merge_two_lists(lists[i], lists[i + 1]))
                else:
                    merged_lists.append(lists[i])
            lists = merged_lists
        
        return lists[0]

if __name__ == "__main__":
    listnode1_1 = ListNode(1)
    listnode1_4 = ListNode(4)
    listnode1_5 = ListNode(5)
    listnode2_1 = ListNode(1)
    listnode2_3 = ListNode(3)
    listnode2_4 = ListNode(4)
    listnode3_2 = ListNode(2)
    listnode3_6 = ListNode(6)

    listnode1_1.next = listnode1_4
    listnode1_4.next = listnode1_5
    listnode2_1.next = listnode2_3
    listnode2_3.next = listnode2_4
    listnode3_2.next = listnode3_6

    listOfNodes = list([listnode1_1,listnode2_1, listnode3_2])
    mergeNodes = Solution().mergeKLists(listOfNodes)
    res = []
    while mergeNodes:
        res.append(mergeNodes.val)
        mergeNodes = mergeNodes.next
    print(res)