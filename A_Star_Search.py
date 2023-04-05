from queue import PriorityQueue

adjacency_list = {
    'S': [('A', 1), ('B', 4),],
    'A': [('B', 2), ('C', 5), ('D', 12)],
    'B': [('C', 2)],
    'C': [('D', 3)],
    'D': [('C', 4)],
}

H = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'D': 0,
}


class Node:
    def __init__(self, nodeName, parent, g, h):
        self.nodeName = nodeName
        self.parent = parent
        self.g = g
        self.f = g+h

    def __lt__(self, a):
        return self.f < a.f


myQueue = PriorityQueue()
myQueue.put(Node('S', None, 0, H['S']))

destNode = None

while not myQueue.empty():
    NOb = myQueue.get()
    if NOb.nodeName == 'D':
        destNode = NOb
        break
    else:
        for adjNode in adjacency_list[NOb.nodeName]:
            cg = NOb.g+adjNode[1]
            myQueue.put(Node(adjNode[0], NOb, cg, H[adjNode[0]]))

# Path Generation

resultPath = []
cost = destNode.g
while destNode is not None:
    resultPath.append(destNode.nodeName)
    destNode = destNode.parent
resultPath.reverse()
# print(resultPath)
for i in resultPath:
    l = len(resultPath)
    if i == resultPath[l-1]:
        print(i)
        break
    print(f"{i} -> ", end='')
print(f"Total Cost --> {cost}")
