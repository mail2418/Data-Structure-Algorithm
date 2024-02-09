"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = None
        current_node = head
        while current_node != None:
            next_node = current_node.next
            current_node.next = new_node
            new_node = current_node
            current_node = next_node
        return new_node
    """
    State awal ==> 1 -> 2 -> 3 -> 4 -> 5 -> None
    None -> 1 -> 2 -> 3 -> 4 -> 5 -> None
    None <- 1   2-> 3 -> 4 -> 5 -> None
    None <- 1 <- 2  3 -> 4 -> 5 -> None
    None <- 1 <- 2 <- 3  4 -> 5 -> None
    None <- 1 <- 2 <- 3 <- 4  5 -> None
    None <- 1 <- 2 <- 3 <- 4 <- 5 -/-> None
    """
        

if __name__ == "__main__":
    listnode1 = ListNode(1)
    listnode2 = ListNode(2)
    listnode3 = ListNode(3)
    listnode4 = ListNode(4)
    listnode5 = ListNode(5)
    listnode1.next = listnode2
    listnode2.next = listnode3
    listnode3.next = listnode4
    listnode4.next = listnode5

    new_node = Solution().reverseList(listnode1)
    res = []
    while new_node :
        res.append(new_node.val)
        new_node = new_node.next
    print(res)
