class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class SinglyLinkedList(object):
  def __init__(self, value):
    super(SinglyLinkedList, self).__init__(value)
    self.head = None
    self.tail = None

  def printAllVals(self):
    runner = list.head
    while (runner.next != null):
      print(runner.value)

   



list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')



print list.printAllVals