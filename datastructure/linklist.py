class Node:
    def __init__(self, data):
        self.data = data
        self.node = None

class SLinkedList:
   def __init__(self):
      self.headval = None

def push(node, data ):
    node.node = Node(data)
    return node.node

  
# put 1, 2, 3, 4, 5


head = SLinkedList()
head.headval = Node(1)

new_node = push(head.headval, 2)
push(new_node, 3)





