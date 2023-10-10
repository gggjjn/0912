class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def update(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next

# 创建一个链表
my_list = LinkedList()

# 添加元素
my_list.append(1)
my_list.append(2)
my_list.append(3)

# 显示链表
my_list.display() 

# 更新元素
my_list.update(2, 4)

# 显示链表
my_list.display()  

# 查找元素
print(my_list.search(4)) 

# 删除元素
my_list.delete(1)

# 显示链表
my_list.display() 