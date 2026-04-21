class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


def traverse(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next


def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    print(slow.data)
    return slow.data


node1 = Node("a")
node2 = Node("b")
node3 = Node("c")
node4 = Node("d")
node5 = Node("e")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverse(node1)
middle_node(node1)
