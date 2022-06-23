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

	def getCount(self):
		temp = self.head
		count = 0

		while(temp):
			count +=1
			temp = temp.next
		return count


LL = LinkedList()
LL.push(1)
LL.push(3)
LL.push(1)
LL.push(2)
LL.push(1)
print("count of node is :", LL.getCount())