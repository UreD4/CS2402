"""
Thomas Roque
Lab 2
CS2302 Data Structures
MW 10:30
Professor: Olac Fuentes
TA: Anindita Nath
"""
import random
import time


def select_bubble(L, end, k):
    size = len(L)
    for i in range(size):  
        for j in range(0, size-i-1): #This iterates through the list
            if L[j] > L[j+1]: #this is checking if the element is greater than the next one
                L[j],L[j+1]=L[j+1],L[j]#python switching
    return L[k]


def partition(L, start, end):
    i = (start-1)
    pi=L[end] #pivot is selected to be the last element
    
    for j in range(start, end):
        if L[j] <= pi: #check if element at j is less than or equal to pivot
            i = i+1 #increment i
            L[i],L[j] = L[j],L[i] #swap elements in python 
    L[i+1],L[end] = L[end],L[i+1] #move pivot to correct position in the list
    
    return (i+1) #return pivot index


def select_quick(L, low, high, k):
    #base case
    if start < end: 
        pi = partition(L, low, high)#creating partition or pivot 
        select_quick(L, low, pi-1, k)#left
        select_quick(L, pi+1, high, k)#right
    
    return L[k] # return the element at pos k




def select_modified_quick(L, low, high, k):
    #same as before but adds an if statement to determine where to sort
    pi = partition(L, low, high)
    if k == pi:
        L[pi]
    if k < pi:
        return select_modified_quick(L, low, pi-1, k)
    else:
        return select_quick(L, pi+1, high, k)

class Stack:
    def __init__(self, L, low, high):
        self.L = L
        self.low = low
        self.high = high


###################################################################################
### PART 2 #######################################################################
##################################################################################
    
def selectQuickStack(L, low, high, k):
    stack = [Stack(L, low, high)]
    while(len(stack) > 0):
        #h gets last element
        h = stack.pop(-1)
        if h.low < h.high:
            #pi gets value of pivot
            pi = partition(h.L, h.low, h.high)
            
            #append left and right sublists
            stack.append(Stack(h.L, h.low, pi - 1))
            stack.append(Stack(h.L, pi + 1, h.high))
    return L[k]





def select_quick_while(L, start, end, k):
    pi = partition(L, start, end)
    #goes until pivot
    while(pi != k):
        if k < pi:
            pi = partition(L, start, pi -1)
        elif k > pi:
            pi = partition(L, pi + 1, end)
            
    return L[pi]




#####main
    
print('Size of List is currently 10\nPlease choose a number between 0-9')
k=int(input("Enter kth element: "))

#create a list witht the size entered by user with random elements
testList = []
for i in range(10):
    testList.append(random.randint(0, 1000))
    
L1 = testList
L2 = testList
L3 = testList
L4 = testList
L5 = testList

#check if user enters invalid input(s)
if k>=0:


    start = time.perf_counter()
    print('\nselect_bubble kth element is: ', select_bubble(L1, len(L1)-1, k))
    end = time.perf_counter()
    print('Time taken: ' + str(end-start) + '\n')
    
    start = time.perf_counter()
    print('\nselect_quick kth element is: ', select_quick(L2, 0, len(L1)-1, k))
    end = time.perf_counter()
    print('Time taken: ' + str(end-start) + '\n')
    
    start = time.perf_counter()
    print('\nselect_modified_quick kth element is: ', select_modified_quick(L3, 0, len(L1)-1, k))
    end = time.perf_counter()
    print('Time taken: ' + str(end-start) + ' seconds\n')
    
    start = time.perf_counter()
    print('\nselect_quick_nr kth element is: ', selectQuickStack(L4, 0, len(L1)-1, k))
    end = time.perf_counter()
    print('Time taken: ' + str(end-start) + '\n')
    
    start = time.perf_counter()
    print('\nselect_quick_while kth element is: ', select_quick_while(L5, 0, len(L1)-1, k))
    end = time.perf_counter()
    print('Time taken: ' + str(end-start) + '\n')
else:
    print("kth element is more than list size")
