def graphColoring(graph, k, V):
    color = [-1]*V;
    
    def isPossible(node,col):
        for i in range(V):
            if color[i] == col and graph[node][i] == 1:
                return False
        return True
    
    def colorGraph(node):
        if node == V:
            return True
        
        for col in range(k):
            if isPossible(node,col):
                color[node] = col
                if colorGraph(node + 1):
                    return True
                color[node] = -1
        return False
    
    return colorGraph(0)