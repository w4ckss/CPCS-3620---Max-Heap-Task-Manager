# This is the Code for the Computer Science 3620 Winter 2026 Semester Final Project
#  
# This project is a task scheduling system using a max heap data sturcture
# The tasks are read from an xlsx file with assigned name, importance, deadline, and estimated time
# and uses statistical weighted scoring model where all values are normalized and the weights of the 
# varibales are 40% for importance, 40% for deadline, and 20% for estimated time totalling 100%.

import pandas as pd

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

                index = parent
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

            if left_child < size and self.heap[left_child][0] > self.heap[largest][0]:      # if valid + if left > right 
                largest = left_child                    # assign left as largest

            if right_child < size and self.heap[largest][0] < self.heap[right_child][0]:     # if valid + right > left
                largest = right_child                   # assign left as larges

            if largest != index:                        # if largest is not the current one
                temp = self.heap[index]               # swap the current index with the largest if not equal
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
        if len(self.heap) != 0:
            print(f"\nThe first taks that you should do is: {self.heap[0]}")
        else:
            return

    def print_all(self):
        for i in range(len(self.heap) - 1):
            print(f"\nPriority Level: {self.heap[i][0]}, Task Name: {self.heap[i][1]}")

###############################s#################################################

data = pd.read_excel("Project.xlsx")     # read excel file
numrows = data.shape[0]
heap = max_heap() 

# Calculations for the impoirtance level that will be used to compare which task should
# be prioritized first
for i in range(numrows):
    importance = float(data.loc[i, "Importance"])
    deadline = float(data.loc[i, "Deadline"])
    time = float(data.loc[i, "Estimated Time"])
    name = (data.loc[i, "Task Name"])

    # NORMAlIZATION: Putting all data in the same unit for accurate comparison

    importance = (importance/10)
    deadline = (1/deadline)
    time = (time/360)

    # MATH FOR PRIORITY LEVEL: Assining data to the right weight

    priority = 0.4*deadline + 0.4*importance + 0.2*time

    # insert the priority value and the name of the task
    heap.insert(priority, name)

heap.print_all()
flag = True
while flag:
    heap.print_first()
    while flag:
        answer = input("Are you ready to move to the next task? (Y/N)")
        if (answer == 'Y' or answer == 'y'):
            heap.remove_root()
            if len(heap.heap) == 0:
                flag = False
            break
        else:
            print("Complete the task first")

print("\nCONGRATULATIONS YOU FINISHED ALL YOU TASKS!!!")