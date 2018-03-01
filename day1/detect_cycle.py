from collections import defaultdict 
# naive union-find 

class Graph:
  
  def __init__(self,vertices):
    self.graph = defaultdict(list) # a key with a list will be added,if the key is not found 
    self.size = vertices 
    
    
  def addEdge(self,u,v):
    self.graph[u].append(v)
    
  def find_parent(self,parent,i):
    if parent[i] == -1:
      return i 
    else:
      return self.find_parent(parent,parent[i]) # recursively find the parent 
    
    
  def union(self,parent,i,j):
    x_set = self.find_parent(parent,i)
    y_set = self.find_parent(parent,j)
    parent[x_set] = y_set
    
  
  def is_cyclic(self):
    parent =[-1] * self.size  
    
    for i in self.graph:
      for j in self.graph[i]:
        x_set = self.find_parent(parent,i)
        y_set = self.find_parent(parent,j)
        if x_set == y_set:                          # They belong to the same set , so there is a cycle
          return True 
        self.union(parent,x_set,y_set)
    return False 
    
        
        
        
g = Graph(3)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,1)

if g.is_cyclic:
  print("It contains cycle")
else:
  print("No cycle ")