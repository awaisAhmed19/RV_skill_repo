class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def segregate_even_odd(head):
    if head is None:
        return None

    even_head = None
    even_tail = None
    odd_head = None
    odd_tail = None

    current_node = head

    while current_node:
        if current_node.data % 2 == 0:
            if even_head is None:
                even_head = current_node
                even_tail = current_node
            else:
                even_tail.next = current_node
                even_tail = current_node
        else:
            if odd_head is None:
                odd_head = current_node
                odd_tail = current_node
            else:
                odd_tail.next = current_node
                odd_tail = current_node

        current_node = current_node.next

    if even_head is None:
        return odd_head

    even_tail.next = odd_head

    if odd_tail:
        odd_tail.next = None

    return even_head

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example usage:
arr = [17, 15, 8, 12, 10, 5, 4, 1, 7, 6]
head = create_linked_list(arr)

print("Original Linked List:")
print_linked_list(head)

segregated_head = segregate_even_odd(head)

print("Segregated Linked List:")
print_linked_list(segregated_head)

arr2 = [1,3,5,7]
head2 = create_linked_list(arr2)
print("Original Linked List 2:")
print_linked_list(head2)
segregated_head2 = segregate_even_odd(head2)
print("Segregated Linked List 2:")
print_linked_list(segregated_head2)

arr3 = [2,4,6,8]
head3 = create_linked_list(arr3)
print("Original Linked List 3:")
print_linked_list(head3)
segregated_head3 = segregate_even_odd(head3)
print("Segregated Linked List 3:")
print_linked_list(segregated_head3)
