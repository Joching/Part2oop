# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

    
# class Linkedlist:
#     def __init__(self):
#         self.head = None

#     def addnode(self, data):
#         self.head = h
#         new_node = Node(data)
#         cur = self.head
#         while cur.next != None:
#             cur = cur.next
#         cur.next = new_node
 
#     def length(self):
#         cur = self.head 
#         total = 0
#         while cur.next != None:
#             total += 1
#             cur = cur.next
#         return total

#     def display(self):
#         elems = []
#         cur = self.head
#         while cur.next != None:
#             elems.append(cur.data)
#             cur = cur.next
#         print (elems)

# my_list = Linkedlist()
# my_list.display()
# my_list.addnode(1)
# my_list.addnode(2)
# my_list.addnode(3)
# my_list.display()






class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
class Linkedlist:
    def __init__(self):
        self.head = Node(None)

    def add_tail(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def add_head(self, data):
        new_node = Node(data)
        self.head.next = new_node 

    def is_empty(self):
        if self.head.next == None:
            print('True')
        else:
            print('False')
 
    def size(self):
        cur = self.head 
        total = 0
        _quit = 0
        while cur.next != None:
            total += 1
            cur = cur.next
            if cur.next == self.head.next:
                print (total)
                _quit = 1
                break
        if _quit == 0:
            print(total)

    def __str__(self):
        elems = []
        cur = self.head
        _exit = 0
        while cur.next != None and _exit == 0:
            cur = cur.next
            elems.append(cur.data)
            if cur.next == self.head.next:
                print (str(elems))
                _exit = 1
                break
        if _exit == 0:
            print (str(elems))
            

    def remove_first(self, search):
        cur = self.head
        _stop = 0
        
        while cur.next != None and _stop == 0:
            if cur.data == search:
                print('Search Found!')
                _stop = 1
            else:
                cur = cur.next


    def _return(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print (cur.data)
            if cur.next == self.head.next:
                break
            
            

    def has_cycle(self):
        cur = self.head
        _quit = 0
        while cur.next != None:
            cur = cur.next
            if cur.next == self.head.next:
                print('Cycle: True!')
                _quit = 1
                break
        if _quit == 0:
            print('Cycle: False!')

    def create_cycle(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = self.head.next
            






                        

my_list = Linkedlist()
my_list.__str__()
my_list.add_head('Head')
my_list.add_tail(1)
my_list.add_tail(2)
my_list.add_tail(3)
my_list.create_cycle()
my_list.__str__()
my_list.is_empty()
my_list.size()
my_list._return()
my_list.remove_first(2)#fix to actually remove
my_list.has_cycle()

    # class Iter:

    #     def _print(self):
    #         cur = self.head
    #         while cur.next != None:
    #             cur = cur.next
    #             print (cur.data)
        
    #     def _find(self, search):
            # cur = self.head
            # while cur.next != None:
            #     if cur.data == search:
            #         print('foudn!')
            #     else:
            #         cur = cur.next
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = Node()

#     def addnode(self, data):
#         new_node = Node(data)
#         cur = self.head
#         while.cur.next != None:
#             cur = cur.next
#         cur.next = new_node

#     def length(self):
#         cur = self.head
#         total = 0
#         while cur.next != None:
#             total += 1
#             cur = cur.next
#         return total

#node.data