class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def reverse(self):
		prev = None
		current = self.head
		while(current is not None):
			next = current.next
			current.next = prev
			prev=current
			current = next
		self.head = prev
		
	def push(self, newData):
		newNode = Node(newData)
		newNode.next = self.head
		self.head = newNode

	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next

LL = LinkedList()
LL.push(20)
LL.push(4)
LL.push(15)
LL.push(85)

print ("Given Linked List")
LL.printList()
LL.reverse()
print("Reversed Linked list")
LL.printList()
