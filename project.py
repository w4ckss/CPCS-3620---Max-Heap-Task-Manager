#Project 

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
            parent = (index - 1) // 3        # parent node

            if self.heap[index] > self.heap[parent]:    # if the current is child is bigger than the parent
                temp = self.heap[index] 
                self.heap[index] = self.heap[parent]    #swap places
                self.heap[parent] = temp
            else:
                break                                   # if everything is good break

    def insert(self, value):                            # adding a task
        self.heap.append(value)                         # add to the end of the heap list
        self.heap.heapify_up(len(self.heap) - 1)        # heapify up

    def heapify_down(self, index):                      # heapify down
        size = len(self.heap)                           # size of the heap
 
        while True:                                     # run for everything
            largest = index                             # make the node the root
            left_child = (2 * index) + 1                # formula for left child
            right_child = (2 * index) + 2               # formula for right child

            if left_child < size and self.heap[left_child] > self.heap[right_child]:      # if valid + if left > right 
                largest = left_child                    # assign left as largest

            if right_child < size and self.heap[left_child] < self.heap[right_child]:     # if valid + right > left
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
    
################################################################################

def open_file(): 