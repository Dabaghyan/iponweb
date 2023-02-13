# # Task 1
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, key):
#         if self.root is None:
#             self.root = Node(key)
#         else:
#             self._insert(key, self.root)
#
#     def _insert(self, key, node):
#         if key < node.val:
#             if node.left is None:
#                 node.left = Node(key)
#             else:
#                 self._insert(key, node.left)
#         else:
#             if node.right is None:
#                 node.right = Node(key)
#             else:
#                 self._insert(key, node.right)
#
#     def search(self, key):
#         if self.root is None:
#             return False
#         else:
#             return self._search(key, self.root)
#
#     def _search(self, key, node):
#         if node is None:
#             return False
#         if key == node.val:
#             return True
#         elif key < node.val:
#             return self._search(key, node.left)
#         else:
#             return self._search(key, node.right)
#
#     def delete(self, key):
#         if self.root is None:
#             return
#         else:
#             self._delete(key, self.root)
#
#     def _delete(self, key, node):
#         if node is None:
#             return
#         if key < node.val:
#             node.left = self._delete(key, node.left)
#         elif key > node.val:
#             node.right = self._delete(key, node.right)
#         else:
#             if node.left is None and node.right is None:
#                 node = None
#             elif node.left is None:
#                 node = node.right
#             elif node.right is None:
#                 node = node.left
#             else:
#                 min_node = self._find_min(node.right)
#                 node.val = min_node.val
#                 node.right = self._delete(min_node.val, node.right)
#         return node
#
#     def _find_min(self, node):
#         current = node
#         while current.left is not None:
#             current = current.left
#         return current

# TASK 2
# Create a class that implements a red black tree and can perform basic operations such as insertion, deletion,
# and searching.


# Task 3, merge sort

#
# def merge_sort(l):
#     if len(l) <= 1:
#         return l
#
#     mid = len(l) // 2
#     left = l[:mid]
#     right = l[mid:]
#
#     left = merge_sort(left)
#     right = merge_sort(right)
#
#     return merge(left, right)
#
# def merge(left, right):
#     result = []
#     left_index = 0
#     right_index = 0
#
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] < right[right_index]:
#             result.append(left[left_index])
#             left_index += 1
#         else:
#             result.append(right[right_index])
#             right_index += 1
#
#     result += left[left_index:]
#     result += right[right_index:]
#
#     return result
#
# a = [3, 5, 6, 7, 3, 4, 2, 4, 0, 0, 1]
# print(merge_sort(a))



# Task 4: Write a function that implements an insertion sort algorithm.


# def insertion_sort(l: list):
#     for i in range(1, len(l)):
#         key = l[i]
#         j = i - 1
#         while j >= 0 and l[j] > key:
#             l[j+1] = l[j]
#             j = j -1
#         l[j+1] = key
#     return l
#
# a = [3, 5, 6, 7, 3, 4, 2, 4]
#
# print(insertion_sort(a))



# TASK 5
# Write a function that implements a sorting algorithm in linear time.

# def counting_sort(l):
#     max_val = max(l)
#     min_val = min(l)
#     k = max_val - min_val + 1
#     count = [0] * k
#     for i in l:
#         count[i - min_val] += 1
#     total = 0
#     for i in range(len(count)):
#         count[i], total = total, count[i] + total
#     output = [0] * len(l)
#     for i in l:
#         output[count[i - min_val]] = i
#         count[i - min_val] += 1
#
#     return output
#
#
# a = [3, 5, 6, 7, 3, 4, 2, 4]
# print(counting_sort(a))
