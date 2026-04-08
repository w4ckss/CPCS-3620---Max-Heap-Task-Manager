#Project 

import pandas as pd

#Functions
#read file
#add node --
#remove node --
#print node
#data normalization
#calculation

#Max Heap Class:

class max_heap:
    def __init__(self):   #constructor
        self.heap = []    #list for heap

    def heapify_up(self, index):             # arranging upwards
        while index > 0:                     # as long as index is not root node
            parent = (index - 1) // 2        # parent node

            if self.heap[index][0] > self.heap[parent][0]:    # if the current is child is bigger than the parent
                temp = self.heap[index]
                self.heap[index] = self.heap[parent]    #swap places
                self.heap[parent] = temp
            else:
                break                                   # if everything is good break

    def insert(self, key, value):                            # adding a task
        self.heap.append((key, value))                       # add to the end of the heap list (tuple)
        self.heapify_up(len(self.heap) - 1)        # heapify up

    def heapify_down(self, index):                      # heapify down
        size = len(self.heap)                           # size of the heap
 
        while True:                                     # run for everything
            largest = index                             # make the node the root
            left_child = (2 * index) + 1                # formula for left child
            right_child = (2 * index) + 2               # formula for right child

            if left_child < size and self.heap[left_child][0] > self.heap[right_child][0]:      # if valid + if left > right 
                largest = left_child                    # assign left as largest

            if right_child < size and self.heap[left_child][0] < self.heap[right_child][0]:     # if valid + right > left
                largest = right_child                   # assign left as larges

            if largest != index:                        # if largest is not the current one
                temp = self.heap[largest]               # swap the current index with the largest if not equal
                self.heap[index] = self.heap[largest]
                self.heap[largest] = temp

                index = largest                         # make the current index the largest
            else:
                break                                   # if node is bigger than both children then done
        
    def remove_root(self):                              # removing node
        if len(self.heap) == 0:                         # check if there is a heap to start with
            return None
        
        if len(self.heap) == 1:                         # If there is only one then return that 
            return self.heap.pop()
        
        root = self.heap[0]                             # make the root node the first element

        self.heap[0] = self.heap[-1]                    # make the first element the last
        self.heap.pop()                                 # remove the duplicated element

        self.heapify_down(0)                            # heapify down the new node to the right place

        return root
    
    def print_first(self):
        print(f"The first taks that you should do is: {self.heap[0]}")

    def print_all(self):
        for i in range(len(self.heap) - 1):
            print(f"Priority Level: {self.heap[i][0]}, Task Name: {self.heap[i][1]}")

###############################s#################################################

data = pd.read_excel("Project.xlsx")     # read excel file
print(data.head())


row = data.iloc[1]   # to get the information of a row (start at index = 1)
print(row) 
print(data.loc[1, "Importance"])   # to acess the column from the row
numrows = data.shape[0]
print(numrows)

heap = max_heap()

for i in range(numrows):
    importance = float(data.loc[i, "Importance"])
    deadline = float(data.loc[i, "Deadline"])
    time = float(data.loc[i, "Estimated Time"])
    name = (data.loc[i, "Task Name"])

    # NORMAlIZATION

    importance = (importance/10)
    deadline = (1/deadline)
    time = (time/360)

    # MATH FOR PRIORITY LEVEL

    priority = 0.4*deadline + 0.4*importance + 0.2*time

    heap.insert(priority, name)

heap.print_first()
heap.print_all()