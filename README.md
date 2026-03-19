# The Royal Rail Ledger

## Summary
This project implements several linked list operations for managing a railway cargo system. It includes working with both singly linked lists and doubly linked lists to perform different inspection and repair tasks.

## Approach

### Task 1: Build Singly Linked List
I created a linked list by iterating through the given Python list and linking nodes one by one using a pointer.

### Task 2: Convert to Python List
I traversed the singly linked list from head to end and collected values into a list.

### Task 3: First Repeated Value
I used a set to track seen values. While traversing, the first value already in the set is returned.

### Task 4: Remove Nodes from Doubly Linked List
I traversed the list and removed nodes matching the target value. I carefully handled:
- removing head
- removing tail
- removing middle nodes  
and updated both `prev` and `next` pointers correctly.

### Stretch Task: Palindrome Check
I used two pointers:
- one from the head
- one from the tail  
and compared values moving toward the center.

## Complexity

- Building list: O(n)
- Traversal: O(n)
- Removing nodes: O(n)
- Palindrome check: O(n)

## Edge Cases

- Empty list
- Single node list
- Removing head node
- Removing tail node
- Removing all nodes
- Consecutive duplicate values
- Even and odd palindrome cases

## Assistance & Sources

- Class notes and lectures
- ChatGPT for debugging and understanding linked list logic