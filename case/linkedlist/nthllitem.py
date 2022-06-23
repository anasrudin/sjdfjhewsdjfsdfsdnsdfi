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

	def getNthIter(self, index):
		current  = self.head
		count = 0

		while (current):
			if (count == index):
				return current.data
			count += 1
			current = current.next

		assert(false)
		return(0)

	def getNthRec(self, llist, position):
		llist.getNthRecNode(self.head, position, llist)

	def getNthRecNode(self, head, position, llist):
		count = 0
		if(head):
			if count == position:
				print(head.data) 
			else:
				llist.getNthRecNode(head.next, position -1, llist)
		else:
			print("index is not exist")




LL = LinkedList()
LL.push(1)
LL.push(4)
LL.push(1)
LL.push(12)
LL.push(1)

n = 2
# print ("element in index 3 iteratively is :", LL.getNthIter(n))

# print ("element in index 3 recursively is :", LL.getNthRec(LL, n))

print("Element at Index 3 is", end=" ")
LL.getNthRec(LL, 3)