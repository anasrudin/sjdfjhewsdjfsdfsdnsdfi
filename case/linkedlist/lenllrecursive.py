class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, newData):
		newNode = Node(newData)
		newNode.next = self.head
		self.head = newNode

	def lenRec(self, node):
		if (not node):
			return 0
		else:
			return 1 + self.lenRec(node.next)

	def lenll(self):
		return self.lenRec(self.head)


LL = LinkedList()
LL.push(1)
LL.push(3)
LL.push(1)
LL.push(2)
LL.push(1)

print("count of node is :", LL.lenll())