import pylab as graph #@UnresolvedImport
import LinkedList

'''
Evaluates the specified Linked List cycle detection algorithm by creating lists with cycles from size 2 up to the
specified size and returning a (python) list specifying the number of iterations it took to find the cycle.
'''
def evaluateCycleDetection(sizeOfList, cycleDetectionAlgorithm, locationOfCycle):
    numberOfIterations = [] #y-axis
    
    for i in range (2, sizeOfList):
        list = LinkedList.createLinkedList(i, True, int(i * locationOfCycle))
        containsCycle, iterationsForList = cycleDetectionAlgorithm(list)
        
        assert containsCycle # all of the generated lists should contain cycles.
        
        numberOfIterations.append(iterationsForList)

    return numberOfIterations

def generateGraph(titleOfGraph, functionsToEvaluate, sizeOfLists, locationOfCycle):
    assert locationOfCycle < 1 #this will be multiplied by the current list size to get the position of the cycle
    
    xAxis = range(2, sizeOfLists) #x-axis

    for function, description in functionsToEvaluate:
        numberOfIterations = evaluateCycleDetection(sizeOfLists, function, locationOfCycle)
        
        graph.plot(xAxis, numberOfIterations, 'o-', label=description, linewidth=2) #http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.plot
    
    graph.xlabel('Size of List')
    graph.ylabel('Number of Iterations')
    graph.plt.legend(fancybox=True, loc=2) #2 = position 'upper left'
    
    graph.title(titleOfGraph)
    graph.grid(True)
    
    graph.show()

'''
Creates a linked list of size 1000 (with a cycle in it) and checks whether the algorithm detects this.
'''
if __name__ == '__main__':
    functionsToEvaluate = [
                           (LinkedList.checkForCyclesHashSet,'Hashset Algorithm'),
                           (LinkedList.checkForCyclesRabbitAndHare, 'Tortoise and Hare Algorithm'), 
                           (LinkedList.checkForCyclesLargerLoops, 'Larger Loops Algorithm')]
    
    generateGraph('Cycle Detection (cycle occurs near start of list)', functionsToEvaluate, 1000, 0.1)
    generateGraph('Cycle Detection (cycle occurs at midpoint list)', functionsToEvaluate, 1000, 0.5)
    generateGraph('Cycle Detection (cycle occurs towards end of list)', functionsToEvaluate, 1000, 0.9)
