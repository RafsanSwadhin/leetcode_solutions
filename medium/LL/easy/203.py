# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         dummy = ListNode(0,head)
#         prev, curr = dummy, head
#         while curr :
#             nxt = curr.next
#             if curr.val == val:
#                 prev.next = nxt
#             else:
#                 prev = curr
#             curr = nxt
#         return dummy.next



# In the code snippet you provided, `dummy = ListNode(0, head)` creates a dummy node. Let me explain its components step by step:

# ### 1. **Purpose of the Dummy Node**
# The dummy node is a common technique in linked list problems. It simplifies the handling of edge cases, such as when the head of the linked list itself needs to be removed. By introducing a dummy node, you can avoid writing separate logic for these cases.

# - **Key Idea**: The dummy node acts as a placeholder before the actual head of the linked list. This allows you to perform operations without worrying about losing the reference to the head.

# ---

# ### 2. **Breaking Down `ListNode(0, head)`**
# #### **a. `ListNode`**
# `ListNode` is the class that defines the structure of a linked list node. Typically, it looks like this:
# ```python
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# ```
# Each node has:
# - `val`: the value stored in the node.
# - `next`: a pointer/reference to the next node in the list.

# #### **b. `0` (the value of the dummy node)**
# - The value `0` is arbitrary. It could be any value because the dummy node's value doesn't matter. It will not affect the final result as you only care about nodes starting from `dummy.next`.

# #### **c. `head` (the next node)**
# - The `head` is passed as the `next` parameter of the dummy node, meaning the dummy node will point to the original head of the linked list.
# - This effectively creates a new linked list starting with the dummy node, followed by the original list:
#   ```
#   Dummy -> Head -> Node2 -> Node3 -> ...
#   ```

# ---

# ### 3. **Why Use a Dummy Node?**
# #### **Example Without a Dummy Node**
# Suppose you want to remove the head of the list. Without a dummy node, you'd need to handle this case explicitly:
# ```python
# if head and head.val == val:
#     head = head.next
# ```
# By using a dummy node, the code becomes cleaner. You can treat all nodes uniformly, including the original head.

# ---

# ### 4. **How the Dummy Node Fits in This Code**
# - **`prev, curr = dummy, head`**:
#   - `prev` starts at the dummy node, and `curr` starts at the actual head of the list.
# - As the loop iterates:
#   - If the current node (`curr`) matches the value `val`, `prev.next` skips over it.
#   - If it doesn’t match, `prev` moves forward.
# - Finally, `dummy.next` is returned, which is the new head of the modified list.

# ---

# ### Example Walkthrough
# #### Input Linked List:
# `1 -> 2 -> 6 -> 3 -> 4 -> 6`  
# #### Operation:
# Remove all nodes with value `6`.

# 1. **Initial State**:
#    ```
#    Dummy -> 1 -> 2 -> 6 -> 3 -> 4 -> 6
#    prev: Dummy
#    curr: 1
#    ```

# 2. **First Iteration**:
#    - `curr.val` = `1`, not `6`.
#    - Move `prev` to `1`, `curr` to `2`.

# 3. **Second Iteration**:
#    - `curr.val` = `2`, not `6`.
#    - Move `prev` to `2`, `curr` to `6`.

# 4. **Third Iteration**:
#    - `curr.val` = `6`.
#    - Skip this node: `prev.next = curr.next`.
#    - Now, `Dummy -> 1 -> 2 -> 3 -> 4 -> 6`.

# 5. **Continue...**

# Final Result:
# ```
# Dummy -> 1 -> 2 -> 3 -> 4
# Return dummy.next (i.e., 1 -> 2 -> 3 -> 4)
# ```