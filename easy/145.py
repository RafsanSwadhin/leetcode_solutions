# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         def traverse(root):
#             nonlocal res
#             if root:
                
#                 traverse(root.left)       
#                 traverse(root.right)
#                 res.append(root.val)
#         traverse(root)
#         return res