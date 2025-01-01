from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move the right pointer n steps ahead
        for _ in range(n):
            right = right.next

        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Remove the nth node
        left.next = left.next.next

        # Return the head of the modified list
        return dummy.next


'''


Your code attempts to remove the nth node from the end of the linked list, but it has some logical issues. Here's a step-by-step explanation and the corrected implementation:

---

### **Issues in Your Code**
1. **Incorrect Position Tracking**:
   - You are decrementing `currentPosition` with `currentPosition -= 1` but starting it at `-1`. This won't correctly align with the logic for finding the nth node from the end.

2. **Iterating from Head Instead of Using Two Pointers**:
   - Using two pointers is the typical and efficient way to solve this problem because it avoids the need to traverse the list twice.

3. **Not Returning the Modified List**:
   - The function should return the new head of the list after removing the node.

---

### **Two-Pointer Approach**

#### **Algorithm**:
1. Create a dummy node to handle edge cases (e.g., removing the head).
2. Use two pointers (`left` and `right`). Start both at the dummy node.
3. Move the `right` pointer `n + 1` steps ahead to maintain a gap of `n` between `left` and `right`.
4. Move both pointers one step at a time until `right` reaches the end of the list.
5. Remove the node by updating the `next` pointer of the `left` pointer.
6. Return the list starting from `dummy.next`.

---

### **Corrected Code**:
```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move the right pointer n steps ahead
        for _ in range(n):
            right = right.next

        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Remove the nth node
        left.next = left.next.next

        # Return the head of the modified list
        return dummy.next
```

---

### **Example Walkthrough**

#### Input: `head = [1, 2, 3, 4, 5]`, `n = 2`

1. **Initialization**:
   ```
   dummy -> 1 -> 2 -> 3 -> 4 -> 5
   left = dummy
   right = head
   ```

2. **Move `right` n steps ahead**:
   ```
   After 2 steps:
   right = 3
   ```

3. **Move `left` and `right` until `right` is None**:
   ```
   left = 3
   right = None
   ```

4. **Remove the nth node**:
   ```
   left.next = left.next.next (remove 4)
   ```

5. **Result**:
   ```
   dummy -> 1 -> 2 -> 3 -> 5
   ```

---

### **Output**

#### Example 1:
```python
head = [1, 2, 3, 4, 5]
n = 2
Output: [1, 2, 3, 5]
```

#### Example 2:
```python
head = [1]
n = 1
Output: []
```

#### Example 3:
```python
head = [1, 2]
n = 1
Output: [1]
```

---

### **Complexity Analysis**
- **Time Complexity**: \(O(L)\), where \(L\) is the length of the linked list (single traversal).
- **Space Complexity**: \(O(1)\), as no additional space is used apart from pointers.


'''