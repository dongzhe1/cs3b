#################################################
# CS03B - Winter 2026
# Assignment 3 - Question 4
# Student Name: Zhe Dong
# SID: 20703849
#################################################


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getLengthOfLinkedList(head):
    l = 0
    while not (head is None):
        l += 1
        head = head.next

    return l


def getIntersectionNode(headA, headB):
    if headA is None or headB is None:
        return None

    pA, pB = headA, headB
    lA, lB = getLengthOfLinkedList(pA), getLengthOfLinkedList(pB)
    if lA > lB:
        for i in range(0, lA - lB):
            headA = headA.next
    else:
        for i in range(0, lB - lA):
            headB = headB.next

    while headA != headB:
        headA = headA.next
        headB = headB.next

    return headA


def run():
    print(f"Input: listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]")
    intersect1 = ListNode(8)
    intersect1.next = ListNode(4)
    intersect1.next.next = ListNode(5)

    headA1 = ListNode(4)
    headA1.next = ListNode(1)
    headA1.next.next = intersect1

    headB1 = ListNode(5)
    headB1.next = ListNode(6)
    headB1.next.next = ListNode(1)
    headB1.next.next.next = intersect1

    intersection1 = getIntersectionNode(headA1, headB1)
    print(f"Output: {'null' if intersection1 is None else intersection1.val}")

    print(f"Input: listA = [1,9,1,2,4], listB = [3,2,4]")
    intersect2 = ListNode(2)
    intersect2.next = ListNode(4)

    headA2 = ListNode(1)
    headA2.next = ListNode(9)
    headA2.next.next = ListNode(1)
    headA2.next.next.next = intersect2

    headB2 = ListNode(3)
    headB2.next = intersect2

    intersection2 = getIntersectionNode(headA2, headB2)
    print(f"Output: {'null' if intersection2 is None else intersection2.val}")

    print(f"Input: listA = [2,6,4], listB = [1,5]")
    headA3 = ListNode(2)
    headA3.next = ListNode(6)
    headA3.next.next = ListNode(4)

    headB3 = ListNode(1)
    headB3.next = ListNode(5)

    intersection3 = getIntersectionNode(headA3, headB3)
    print(f"Output: {'null' if intersection3 is None else intersection3.val}")

if __name__ == "__main__":
    run()