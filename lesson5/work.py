import heapq

##
print('Задание номер 1: Алгоритм Дейкстры')
# def dijkstra(graph, start):
#     distances = {vertex: float('infinity') for vertex in graph}
#     distances[start] = 0
#     path = {vertex: [] for vertex in graph}
#     priority_queue = [(0, start)]
    
#     while priority_queue:
#         current_distance, current_vertex = heapq.heappop(priority_queue)
        
#         for neighbor, weight in graph[current_vertex].items():
#             distance = current_distance + weight

#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 path[neighbor] = path[current_vertex] + [current_vertex]
#                 heapq.heappush(priority_queue, (distance, neighbor))
#     return distances, path

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    print(distances)
    distances[start] = 0
    path = {vertex: [] for vertex in graph}
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        for neigbor, weight in graph[current_vertex].items():
            print(neigbor, weight)
            distance = current_distance + weight
            print(distances)
            if distance<distances[neigbor]:
                distances[neigbor] = distance
                path[neigbor] = path[current_vertex] + [current_vertex]
                heapq.heappush(priority_queue, (distance, neigbor))
    return distances, path

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_vertex = 'A'
distances, path = dijkstra(graph, start_vertex)
print('Расстояние: ',distances)
print('Кратчайшие пути: ',path)
print('\n')





##
# print('Задание 2: Сортировка слияния (Merge Sort)')
# def merge(left, right):
#     merged = []
#     left_idx, right_idx = 0, 0
    
#     while left_idx < len(left) and right_idx < len(right):
#         if left[left_idx] < right[right_idx]:
#             merged.append(left[left_idx])
#             left_idx += 1
#         else:
#             merged.append(right[right_idx])
#             right_idx += 1
    
#     merged.extend(left[left_idx:])
#     merged.extend(right[right_idx:])
#     return merged

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr 
    
#     mid = len(arr) // 2
    
#     left_half = arr[:mid]
#     right_half = arr[mid:]
    
#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)
    
#     return merge(left_half, right_half)

# input_array = [38, 27, 43, 3, 9, 82, 10]
# print("Исходный массив:", input_array)
# sorted_array = merge_sort(input_array)
# print("Отсортированный массив:", sorted_array)






# ##
# print('Задание 3: Связанный поиск')
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data): 
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node

#     def delete(self, data): 
#         current = self.head
#         if current and current.data == data:
#             self.head = current.next
#             current = None
#             return
#         prev = None
#         while current and current.data != data:
#             prev = current
#             current = current.next
#         if current is None:
#             return
#         prev.next = current.next
#         current = None

#     def search(self, data): 
#         current = self.head
#         while current:
#             if current.data == data:
#                 return True
#             current = current.next
#         return False

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.display()

# ll.delete(2)
# ll.display()

# result = ll.search(3)
# print("Поиск элемента 3:", result)
# print('\n')








# ##
# print('Задание 4: Бинарное дерево')
# class TreeNode:
#     def __init__(self, key):
#         self.val = key
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, key):
#         if not self.root:
#             self.root = TreeNode(key)
#         else:
#             self._insert(self.root, key)

#     def _insert(self, node, key):
#         if key < node.val:
#             if node.left is None:
#                 node.left = TreeNode(key)
#             else:
#                 self._insert(node.left, key)
#         elif key > node.val:
#             if node.right is None:
#                 node.right = TreeNode(key)
#             else:
#                 self._insert(node.right, key)

#     def delete(self, key):
#         self.root = self._delete(self.root, key)

#     def _delete(self, node, key):
#         if not node:
#             return node
#         if key < node.val:
#             node.left = self._delete(node.left, key)
#         elif key > node.val:
#             node.right = self._delete(node.right, key)
#         else:
#             if not node.left:
#                 return node.right
#             elif not node.right:
#                 return node.left

#             min_val = self._find_min(node.right)
#             node.val = min_val
#             node.right = self._delete(node.right, min_val)

#         return node

#     def _find_min(self, node):
#         while node.left:
#             node = node.left
#         return node.val

#     def search(self, key):
#         return self._search(self.root, key)

#     def _search(self, node, key):
#         if not node or node.val == key:
#             return node
#         if key < node.val:
#             return self._search(node.left, key)
#         return self._search(node.right, key)

#     def inorder_traversal(self, node):
#         if node:
#             self.inorder_traversal(node.left)
#             print(node.val, end=" -> ")
#             self.inorder_traversal(node.right)

#     def display(self):
#         self.inorder_traversal(self.root)
#         print("None")


# tree = BinaryTree()
# tree.insert(5)
# tree.insert(3)
# tree.insert(7)
# tree.insert(2)
# tree.insert(4)
# tree.insert(6)
# tree.insert(8)
# tree.display()

# tree.delete(3)
# tree.display()

# result = tree.search(6)
# print("Результат поиска 6:", result.val)





# ##
# print('Задание 5: Хеш-таблица с методом цепочек')
# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [[] for _ in range(size)]

#     def _hash(self, key):
#         return hash(key) % self.size

#     def insert(self, key, value):
#         index = self._hash(key)
#         found = False
#         for i, entry in enumerate(self.table[index]):
#             if entry[0] == key:
#                 self.table[index][i] = (key, value)
#                 found = True
#                 break
#         if not found:
#             self.table[index].append((key, value))

#     def search(self, key):
#         index = self._hash(key)
#         for entry in self.table[index]:
#             if entry[0] == key:
#                 return entry[1]  
#         return None  

#     def delete(self, key):
#         index = self._hash(key)
#         for i, entry in enumerate(self.table[index]):
#             if entry[0] == key:
#                 del self.table[index][i]  
#                 return

#     def display(self):
#         for i, bucket in enumerate(self.table):
#             print(f'Bucket {i}:', end=" ")
#             for key, value in bucket:
#                 print(f'({key}: {value})', end=" ")
#             print()

# hash_table = HashTable(10)
# hash_table.insert("яблоко", 5)
# hash_table.insert("банан", 8)
# hash_table.insert("мандарин", 12)

# print("Перед удалением:")
# hash_table.display()
# hash_table.delete("банан")
# print("\nПосле удаления:")
# hash_table.display()






# ##
# print('Задание номер 6: quick sort (алгоритм быстрой сортировки)')
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[len(arr) // 2]
#         less = []
#         equal = []
#         greater = []
#         for element in arr:
#             if element < pivot:
#                 less.append(element)
#             elif element == pivot:
#                 equal.append(element)
#             else:
#                 greater.append(element)
#         return quick_sort(less) + equal + quick_sort(greater)

# input_array = [38, 27, 43, 3, 9, 82, 10]
# print("Исходный массив:", input_array)
# sorted_array = quick_sort(input_array)
# print("Отсортированный массив:", sorted_array)