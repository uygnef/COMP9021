# Written by Eric Martin and Yu Feng for COMP9021

from linked_list import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)
        
        
    def rearrange(self):
        if not self.head:
            return
        First = self.head
        before_temp = First
        temp = before_temp.next_node        
            
        while First.next_node:

            if self.compare(First.value, temp.value):
                
                before_temp.next_node = temp.next_node
                temp.next_node = First.next_node
                First.next_node = temp


                First = temp
                before_temp = temp
                temp = temp.next_node       
            else:
                if temp.next_node == None:
                    First = First.next_node
                    before_temp = First
                    temp = before_temp.next_node
                else:
                    before_temp = temp
                    temp = temp.next_node




                    
          
            

                
                
