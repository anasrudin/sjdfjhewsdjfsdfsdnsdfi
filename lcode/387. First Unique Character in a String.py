import collections
def first(s):
    count = collections.Counter(s)
    print(count)


a= 'leetcode'
b= 'loveleetcode'
c= 'aabb'
print(first(a))
