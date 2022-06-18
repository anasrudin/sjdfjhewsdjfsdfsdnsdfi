# Knapsack Problem 
# for array

class ItemValue:
	def __init__(self, item, value, ind):
		self.item = item 
		self.value  = value 
		self.ind = ind 
		self.cost = value // item 

	def __lt__(self, other):
		return self.cost < other.cost



# Greedy Approach
class FractionalKnapsack:
	#time complexity n log n 
	@staticmethod
	def getMaxValue(item, value, capacity):
		iVal = []
		for i in range(len(item)):
			iVal.append(ItemValue(item[i], value[i], i))

		#sorting item by value
		iVal.sort(reverse=True)

		totalValue = 0
		for i in iVal:
			curItem = int(i.item)
			curValue = int(i.value)
			if capacity - curItem >=0:
				capacity -= curItem
				totalValue += curValue
			else:
				fraction = capacity /curItem
				totalValue += curValue * fraction
				capacity = int(capacity - (curItem * fraction))
				break
		return totalValue










item = [10, 40, 20, 30]
value = [60, 40, 100, 120]
capacity = 50

maxValue = FractionalKnapsack.getMaxValue(item, value, capacity)
print ("Maximum value in Knapsack =", maxValue)