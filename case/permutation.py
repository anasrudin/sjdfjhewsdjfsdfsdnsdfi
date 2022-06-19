# backtracking

def toString(List):
	return ''.join(List)


def permute(listString, idJ, stringLen):
	if idJ==stringLen:
		print(toString(a))
	else:
		for i in range (idJ, stringLen):
			listString[i], listString[idJ] = listString[idJ], listString[i]
			permute(listString, idJ+1, stringLen)
			listString[idJ], listString[i] = listString[i], listString[idJ]

string = "ABCD"
n = len(string)
a = list(string)
permute(a, 0, n)
