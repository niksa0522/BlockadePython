from os import close
from queue import Queue

def BFS(table,startCoord,endCoords):
    if startCoord in endCoords:
        return True
    queue_nodes = Queue(table.red*table.kol)
    visited = set()
    visited.add(startCoord)
    queue_nodes.put(startCoord)
    found_dest=[False,False]
    while (not all(found_dest)) and (not queue_nodes.empty()):
        node = queue_nodes.get()
        valid_dest =table.ReturnValidMovesForPawn(node,endCoords)
        valid_dest.sort(key=lambda x: Heuristic(x,endCoords))
        for x in valid_dest:
            if x not in visited:
                if x in endCoords:
                    found_dest[endCoords.index(x)] = True
                    if all(found_dest):
                        return True
                visited.add(x)
                queue_nodes.put(x)
    return False

def Heuristic(startCoord,endCoords):
    heur=[]
    for x in endCoords:
        h1 = abs(startCoord[0] - x[0]) + abs(startCoord[1]-x[1])
        heur.append(h1)
    if(heur[0]>heur[1]):
        return heur[1]
    else:
        return heur[0] 


def GetDistanceBetween(startCoord,endCoord):
    return abs(startCoord[0] - endCoord[0]) + abs(startCoord[1]-endCoord[1])

def AStar(table,startCoord,endCoords):
    found_dest=[False,False]
    open_set=set()
    closed_set=set()
    g={}
    prev_nodes={}
    g[startCoord] = 0
    prev_nodes[startCoord]=None
    open_set.add(startCoord)

    while len(open_set) > 0 and (not all(found_dest)):
        node = None
        for next_node in open_set:
            if node is None or g[next_node] + Heuristic(next_node,endCoords) < g[node] + Heuristic(node,endCoords):
                node = next_node
        if node in endCoords:
                    found_dest[endCoords.index(node)] = True
                    if all(found_dest):
                        return True
        for x in table.ReturnValidMovesForPawn(node,endCoords):
            if x not in open_set and x not in closed_set:
                open_set.add(x)
                prev_nodes[x]=node
                g[x]=g[node]+GetDistanceBetween(node,x)
            else:
                if g[x] > g[node] + GetDistanceBetween(node,x):
                    g[x] = g[node] + GetDistanceBetween(node,x)
                    prev_nodes[x]=node
                    if x in closed_set:
                        closed_set.remove(x)
                        open_set.add(x)
        open_set.remove(node)
        closed_set.add(node)
    return False

def BFS_WithPath(table,startCoord,endCoords):
    if startCoord in endCoords:
        path =list()
        path.append(startCoord)
        return path
    queue_nodes = Queue(table.red*table.kol)
    visited = set()
    prev_nodes=dict()
    prev_nodes[startCoord]=None
    visited.add(startCoord)
    queue_nodes.put(startCoord)
    found_dest=False
    end=None
    while (not found_dest) and (not queue_nodes.empty()):
        node = queue_nodes.get()
        valid_dest =table.ReturnValidMovesForPawn(node,endCoords)
        valid_dest.sort(key=lambda x: Heuristic(x,endCoords))
        for x in valid_dest:
            if x not in visited:
                prev_nodes[x] = node
                if x in endCoords:
                    found_dest = True
                    end=x
                    break
                visited.add(x)
                queue_nodes.put(x)
    path = list()
    if found_dest:
        path.append(end)
        prev = prev_nodes[end]
        while prev is not None:
            path.append(prev)
            prev=prev_nodes[prev]
    return path