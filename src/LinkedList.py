'''
Implements a linked list (rather than using the in-built version).

'''

class List:
    def __init__(self):
        self.firstNode = None
        self.lastNode = self.firstNode
 
    def __PrintData(self,aNode):
        if aNode is not None:
            print aNode.data ,
            self.__PrintData(aNode.next)
 
    def Print(self):
        self.__PrintData(self.firstNode)
 
    def Append(self, data):
        newNode = LinkedListNode(data)
        if self.firstNode is None:
            self.firstNode = newNode
            self.lastNode = newNode
        else:
            self.lastNode.next = newNode
            self.lastNode = newNode
    def AppendNode(self, newNode):
        if self.firstNode is None:
            self.firstNode = newNode
            self.lastNode = newNode
        else:
            self.lastNode.next = newNode
            self.lastNode = newNode
    def getFirst(self):
        return self.firstNode

'''
Singly-linked list node.
'''
class LinkedListNode:
    def __init__(self,value):
        self.data = value
        self.next = None
 

'''
Function to detect whether there is a cycle in a linked list.
Returns True/False depending on whether a cycle was detected and an int representing the number of iterations
required to find the cycle.

Implementation: Iterates once through the list with a fast iterator and a slow iterator. If there is a cycle the 
fast iterator will eventually look at the same element as the slow iterator.
'''
def checkForCyclesRabbitAndHare(list):
    numberOfIterations = 0
    
    firstPass = list.getFirst()
    secondPass = list.getFirst().next
    
    while firstPass is not None and secondPass is not None:
        numberOfIterations = numberOfIterations + 1
        
        if firstPass.data == secondPass.data: 
            return True, numberOfIterations
        firstPass = firstPass.next
        
        if secondPass.next is not None:
            secondPass = secondPass.next.next
        else:
            secondPass = None
    return False, numberOfIterations

'''
Function to detect whether there is a cycle in a linked list.
Returns True/False depending on whether a cycle was detected and an int representing the number of iterations
required to find the cycle.

Implementation (the detection part) of Brent's algorithm, as described in http://en.wikipedia.org/wiki/Floyd's_cycle-finding_algorithm
Further description from http://ostermiller.org/find_loop_singly_linked_list.html

This algorithm is supposedly faster than the Rabbit and Hare algorithm (above) if you want to find where the loop occurs.
'''

def checkForCyclesLargerLoops(list):
    numberOfIterations = 0
    
    currentNode = list.getFirst()
    checkNode = None
    since = 0
    sinceScale = 2;
    
    while currentNode is not None:
        numberOfIterations = numberOfIterations + 1
        
        if checkNode == currentNode:
            return True, numberOfIterations
        if since >= sinceScale:
            checkNode = currentNode;
            since = 0;
            sinceScale = 2*sinceScale;
        
        currentNode = currentNode.next
        since = since + 1
 
    return False, numberOfIterations

'''
Function to detect whether there is a cycle in a linked list.
Returns True/False depending on whether a cycle was detected and an int representing the number of iterations
required to find the cycle.

Basic implementation that has O(n) space complexity. Adds every node pointer seen so far to a set and detects
a cycle if the same pointer is added twice to the set.
'''
def checkForCyclesHashSet(list):
    numberOfIterations = 0
    
    nodesSeen = set() 
    currentNode = list.getFirst()

    while currentNode is not None:
        numberOfIterations = numberOfIterations + 1
         
        if currentNode in nodesSeen:
            return True, numberOfIterations
        nodesSeen.add(currentNode)
        currentNode = currentNode.next

    return False, numberOfIterations


'''
Iterative algorithm for reversing a linked list.
'''
def reverseList(list):
    currentItem = list.getFirst()

    previousItem = None
    
    list.lastNode = list.getFirst() #set the new last node to be the current currentItem node
    
    while currentItem is not None: # iterate through the list reversing each element.
        nextItem = currentItem.next #store the next item in the list in a temp variable
        
        currentItem.next = previousItem #flip the pointer to the previous item in the list.

        previousItem = currentItem 
        currentItem = nextItem
    
    list.firstNode = previousItem #set the new currentItem node to be the old last node.

'''
Factory function for creating a linked list with the specified size (contents are just numbers), whether
there is a cycle in the list, and the point at which that cycle should occur.
'''   
def createLinkedList(size, containsCycle=False, cycleStartPos=0):
    list = List()
     
    if containsCycle:
        assert size > cycleStartPos
        
        for i in range(0, cycleStartPos-1): #create all of the lists nodes up until the node which will be part of the cycle.
            list.AppendNode(LinkedListNode(i))
        
        cycleNode = LinkedListNode(cycleStartPos) #create a reference to the node which the list will cycle back to.
        
        list.AppendNode(cycleNode)
        
        for i in range (cycleStartPos+1, size-1): #add the rest of the nodes, apart from the last one, which is where the cycle begins.
            list.AppendNode(LinkedListNode(i))
        
        list.AppendNode(cycleNode) # add the cycle node again to create a cycle.
    else:
        for i in range(0, size): #create all of the lists nodes up until the node which will be part of the cycle.
            list.AppendNode(LinkedListNode(i))
        
    return list

'''
Creates a linked list of size 1000 (with a cycle in it) and checks whether the algorithm detects this.
'''
if __name__ == '__main__':
    testList = createLinkedList(1000, True, 50)

    isACycle, iterations = checkForCyclesLargerLoops(testList)
    if isACycle is True:
        print "There are cycles in the list (number of iterations: {0})".format(iterations)
    else:
        print "There are no cycles in the list, so it can be printed..."
        testList.Print()
        print "\nReversed List: "
        reverseList(testList)
        testList.Print()

