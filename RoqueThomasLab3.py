
#IMPORTS



#CONSTRUCTOR
class Node(object):
    # Constructor
    def __init__(self, data, next=None):  
        self.data = data
        self.next = next 

class List(object):   
    # Constructor
    def __init__(self,head = None,tail = None):    
        self.head = head
        self.tail = tail

    def Append(self,x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next

    def AppendList(self,python_list):
        for d in python_list:
            self.Append(d)

        
    #PRINT CONTENTS OF THE LIST
    def Print(self):
        t = self.head
        while t is not None:
            print(t.data,end=' ')
            t = t.next
        print()

    #INSERTS AN INTEGER i TO THE LIST - SHOULD REMAIN ORDERED
    def Insert(self, i):
        if self is None:
            self.head = Node(i)
            self.tail = self.head
        iter = self.head

        Ncert = Node(i)

        while iter is not None:
            if iter.data > i:
                Ncert.next=iter
                self.head = Ncert
                return
            elif iter.next is None:
                iter.next = Ncert
                return
            
            elif iter.next.data < i:
                iter = iter.next
            
            elif iter.next.data >= i:
                Ncert.next = iter.next
                iter.next = Ncert
                return
             
              

    #REMOVES INTEGER I FROM THE LIST
    def Delete(self,i):
        if self is None:
            return
        iter = self.head
        
        while iter is not None:
            if iter.data==i:
                iter = iter.next
                self.head = iter
                return
            if iter.next is None:
                return
            elif iter.next.data == i:
                iter.next = iter.next.next
                return
            iter = iter.next
            

    #RETURNS INDEX OF I TO LIST
    def IndexOf(self, i):
        if self is None:
            return -1
        iter = self.head
        count = 0
        while iter is not None:
            if iter.data == i:
                return count
            count +=1
            iter = iter.next
        return -1

    #REMOVES ALL ELEMENTS FROM THE LIST
    def Clear(self):
        if self is None:
            return
        self.head = None
        self.tail = None

    #RETURN MIN AND MAX
    def min(self):
        if self is None:
            return 
        return self.head.data
    def max(self):
        if self is None:
            return 
        return self.tail.data

    #TRUE IF LIST HAS DUPLICANT ELEMENTS
    def HasDubplicate(self):
        if self is None:
            return False
        iter = self.head
        while iter is not None:
            if iter.next is None:
                return False
            elif iter.data == iter.next.data:
                return True
            iter = iter.next

    #RETURNS THE K-TH SMALLEST ELEMENT IN THE LIST
    def Select(self,k):
        if self is None:
            return
        iter = self.head
        while iter is not None:
            if k==0:
                return iter.data
            iter = iter.next
            k-=1
        return -1
def initList(List):
        for i in range(0,10):
            List.Append(i)
def initList2(List):
    for i in range(11,13):
        List.Append(i)
#INSERTS ALL ELEMENTS OF M INTO THE LIST - COULD NOT GET TO WORK IN CLASS
def Merge(iter,miter):
    if iter is None: 
        return miter 
    if miter is None: 
        return iter
    
    if iter.data <= miter.data: 
        temp = iter 
        temp.next = Merge(iter.next, miter) 
    else: 
        temp = miter 
        temp.next = Merge(iter, miter.next) 
    return temp 

#RUNNER AREA
print('PRINT THE LIST:')
L1 = List()
initList(L1)
L1.Print()
print('Insert an Int:')
L1 = List()
initList(L1)
L1.Insert(0)
L1.Print()

print('Delete the an Int:')
L1 = List()
initList(L1)
L1.Delete(0)
L1.Print()

print('Merges 2 lists:')
L1 = List()
initList(L1)
L2 = List()
initList2(L2)
L3 = List()
L3.head = Merge(L1.head,L2.head)
L3.Print()

print('Index of 5:')
L1 = List()
initList(L1)
print(L1.IndexOf(5))


print('Min and Max (respectavily):')
L1 = List()
initList(L1)
print(L1.min())
print(L1.max())


print('Has Dubplicit')
L1 = List()
initList(L1)
L1.Insert(3)
L1.Print()
print(bool(L1.HasDubplicate))

print('kth Smallest:')
L1 = List()
initList(L1)
print(L1.Select(2))

