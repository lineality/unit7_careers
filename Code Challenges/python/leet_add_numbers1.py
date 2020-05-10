# 2020.04.27
# https://leetcode.com/problems/add-two-numbers/submissions/
# works

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Part 1: turn the linked lists into listspart

        # get values into list:
        list1 = []
        list1.append(l1.val)
        mask = l1
        while mask.next:
            if mask.next:
                list1.append(mask.next.val)
                if mask.next.next:
                    mask = mask.next
                else:
                    break
        print(list1)

        # get values into list:
        list2 = []
        list2.append(l2.val)
        mask = l2
        while mask.next:
            if mask.next:
                list2.append(mask.next.val)
                if mask.next.next:
                    mask = mask.next
                else:
                    break
        print(list2)

        # part 2: reverse the numbers

        l1 = list1
        l2 = list2

        # convert list 1
        l1 = l1[::-1]  # reverse the order
        strL = ""
        l1 = int("".join(map(str, l1)))  # convert to a single number

        print(l1)

        # convert list 2
        l2 = l2[::-1]  # reverse the order
        strL = ""
        l2 = int("".join(map(str, l2)))  # convert to a single number

        print(l2)

        # add and make a new backwards list
        # add list 1 and list 2
        l3 = l1 + l2  # add the numbers
        l3 = list(str(l3))  # convert to list of digits (string form)
        l3 = list(map(int, l3))  # convert to a list of digits
        l3 = l3[::-1]  # reverse the order

        print(l3)

        # turn back into a linked list

        # swap names
        list3 = l3

        # start the linked list
        l3 = ListNode(list3[0])

        # remove first item
        list3.pop(0)

        mask = l3
        for i in list3:  # now one digit shorter
            mask.next = ListNode(i)  # create node for each item in list
            # print(mask.next.val)
            mask = mask.next

        print(l3.val)
        print(l3.next.val)
        print(l3.next.next.val)

        return l3


xx = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

xx.addTwoNumbers(l1, l2)
