# Written by Eric Martin for COMP9021

from linked_list import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)
        
        
    def rearrange(self):
        if not self.head:
            return
        First = self.head
 #       print(First.value)
        before_temp = First
  #      print(before_temp.value)
        temp = before_temp.next_node
  #      print(temp.value)

        while temp.next_node:
            print(temp.next_node.value)
            if self.compare(First.value, temp.value):
                before_temp.next_node = temp.next_node
           #     print('----',before_temp.next_node.value)
                temp.next_node = First.next_node
            #    print(before_temp.next_node.value,temp.next_node.value)
                First.next_node = temp


                First = temp
                before_temp = temp
                temp = temp.next_node
                
            else:
            #    print('else')
                before_temp = temp
                temp = temp.next_node
            
