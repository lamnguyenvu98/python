arr = [2, 18, 24, 3, 5, 7, 9, 6, 12]

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

curr = None

for i, elem in enumerate(arr):
    if not curr:
        head = curr = Node(val=elem)
    else:
        prev = curr
        while prev.next:
            prev = prev.next
        prev.next = Node(val=elem)

# print linked list
og_list = list()
curr = head
while curr.next:
    og_list.append(curr.val)
    curr = curr.next
og_list.append(curr.val)

# reversed linked list
prev, curr = None, head
while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp

print("\n\n")
rev_list = list()
curr = prev
while curr.next:
    rev_list.append(curr.val)
    curr = curr.next
rev_list.append(curr.val)
print("original: ", og_list)
print("reversed: ", rev_list)


