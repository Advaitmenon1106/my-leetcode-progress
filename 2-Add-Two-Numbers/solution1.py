# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    current_node = l1
    number1_as_str = ''
    while current_node != None:
        number1_as_str+=str(current_node.val)
        current_node = current_node.next
    
    number1_as_str = number1_as_str[::-1]
    n1 = int(number1_as_str)

    current_node = l2
    number2_as_str = ''

    while current_node != None:
        number2_as_str+=str(current_node.val)
        current_node = current_node.next
    
    number2_as_str = number2_as_str[::-1]
    n2 = int(number2_as_str)
    sum_nos = list(str(n1+n2))
    print(l1)

    sum_nos_rev = sum_nos[::-1]

    nodelist = [ListNode() for i in range(len(sum_nos_rev))]

    for i, node in enumerate(nodelist):
        if i == len(nodelist)-1:
            node.next = None
        else:
            node.next = nodelist[i+1]
        node.val = sum_nos_rev[i]
    
    return nodelist[0]