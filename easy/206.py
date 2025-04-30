# problem:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr :
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


### 👩‍💻 Code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 🧠 This is the structure for a node in a **singly linked list**.

# - `val` is the data inside the node (like 1, 2, 3).
# - `next` is a pointer to the **next node** in the list.

# So a linked list like `[1, 2, 3]` is represented as:
# ```
# 1 → 2 → 3 → None
# ```

# ---

# ### 🔁 Now the real function:
# ```python
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# ```

# This is a method inside a class `Solution`.  
# It takes `head` (the first node of the linked list) and returns the **head of the reversed list**.

# ---

# ### 1️⃣ Initial setup:
# ```python
#         curr = head
#         prev = None
# ```

# - `curr` is the pointer to the **current node** we're working with.
# - `prev` will store the **previous node** (initially `None`, because the new tail will point to `None`).

# ---

# ### 🔄 Loop through the list and reverse:
# ```python
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
# ```

# Let’s break it into baby steps 💫:

# 1. `temp = curr.next`  
#    👉 Save the next node so we don’t lose the rest of the list.

# 2. `curr.next = prev`  
#    👉 Flip the current node’s pointer. It now points **backward**.

# 3. `prev = curr`  
#    👉 Move the `prev` pointer forward (to the current node).

# 4. `curr = temp`  
#    👉 Move `curr` to the next node (which we saved earlier).

# 🔁 Repeat until `curr` becomes `None` (end of list).

# ---

# ### ✅ Finally:
# ```python
#         return prev
# ```

# Now `prev` points to the **new head** of the reversed linked list.  
# Return it as the result.

# ---

# ### 🧠 Example:

# Input:  
# `head → 1 → 2 → 3 → 4 → 5 → None`

# After reversing:
# `prev → 5 → 4 → 3 → 2 → 1 → None`

# So the function returns node `5`, which is the new **head** of the reversed list.





# ### 😕 Why returning `prev` doesn't just return `5`?

# You're thinking:
# > "I’m returning `prev`, which is the last node (value `5`), so shouldn’t it just return `5`?"

# And you’re **partially right** — `prev` **does** point to the node with value `5`...  
# **BUT** that node also now has `.next` pointing to `4`, and `4.next` points to `3`, and so on...

# So even though you only return the **first node of the reversed list**, it holds the **entire reversed chain** like this:

# ```
# prev → 5 → 4 → 3 → 2 → 1 → None
# ```

# So when you return `prev`, you're actually returning the **head of the whole reversed list**, not just the number `5`.

# ---

# ### 🔄 Visual Representation:

# Before reversing:
# ```
# head → 1 → 2 → 3 → 4 → 5 → None
# ```

# After reversing:
# ```
# prev → 5 → 4 → 3 → 2 → 1 → None
# ```

# So if your function returns `prev`, and you **traverse the list**, you will get:
# ```
# [5, 4, 3, 2, 1]
# ```

# ---

# ### 🧪 But If You Do This:
# print(prev.val)  # 👉 It will just print: 5

# Because you're only printing the value of that node.

# But if you **traverse it**, like this:
# result = []
# while prev:
#     result.append(prev.val)
#     prev = prev.next

# You’ll get:
# [5, 4, 3, 2, 1]

# ### 🔚 Summary:

# - `prev` points to the full **reversed linked list**.
# - You just need to **traverse** from `prev` to get all the values.