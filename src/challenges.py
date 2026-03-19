from typing import Optional


# ----------- Singly Linked List -----------

class SinglyNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[SinglyNode] = None


# ----------- Doubly Linked List -----------

class DLLNode:
    def __init__(self, value: int, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[DLLNode] = None
        self.tail: Optional[DLLNode] = None


# ----------- TASK 1 -----------

def build_sll_from_list(values: list[int]) -> SinglyLinkedList:
    sll = SinglyLinkedList()

    if not values:
        return sll

    sll.head = SinglyNode(values[0])
    current = sll.head

    for value in values[1:]:
        current.next = SinglyNode(value)
        current = current.next

    return sll


# ----------- TASK 2 -----------

def sll_to_list(sll: SinglyLinkedList) -> list[int]:
    result = []
    current = sll.head

    while current:
        result.append(current.value)
        current = current.next

    return result


# ----------- TASK 3 -----------

def find_first_repeat_sll(sll: SinglyLinkedList) -> int | None:
    seen = set()
    current = sll.head

    while current:
        if current.value in seen:
            return current.value
        seen.add(current.value)
        current = current.next

    return None


# ----------- TASK 4 -----------

def remove_all_from_dll(dll: DoublyLinkedList, target: int) -> None:
    current = dll.head

    while current:
        next_node = current.next

        if current.value == target:

            # Remove head
            if current.prev is None:
                dll.head = current.next
                if dll.head:
                    dll.head.prev = None

            # Remove tail
            elif current.next is None:
                dll.tail = current.prev
                if dll.tail:
                    dll.tail.next = None

            # Remove middle
            else:
                current.prev.next = current.next
                current.next.prev = current.prev

        current = next_node

    if dll.head is None:
        dll.tail = None


# ----------- STRETCH TASK -----------

def is_train_palindrome(dll: DoublyLinkedList) -> bool:
    left = dll.head
    right = dll.tail

    while left and right and left != right and left.prev != right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.prev

    return True