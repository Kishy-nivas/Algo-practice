INF = 999 
class Graph:
  def __init__(self,vertices,g):
    self.size =vertices 
    self.graph = g
  
  def find_min(self,key,color):
    min_val =INF
   
    for i in range(self.size):
      if min_val > key[i] and color[i] == "white":
        min_ind = i 
        min_val = key[i]
    print(min_ind)
    return min_ind
  
  def generate_prims(self,s):
    key = [INF] * self.size 
    parent = [-1] * self.size 
    color = ["white"] * self.size 
    color_values = 0 
    key[s] = 0 
    for _ in range(self.size):
      
      u = self.find_min(key,color)
      
      for v in range(self.size):
        if color[v] == "white" and key[v] > self.graph[u][v] and self.graph[u][v]>0:
          key[v] = self.graph[u][v]
          parent[v] = u 
      
      color[u] = "black"
    
    for i in range(self.size):
      print(i,parent[i], graph[i][parent[i]])
   
graph = [ [0, 2, 0, 6, 0],
             [2, 0, 3, 8, 5],
             [0, 3, 0, 0, 7],
             [6, 8, 0, 0, 9],
             [0, 5, 7, 9, 0],
           ]
g  = Graph(5,graph)

g.generate_prims(0) 
        
      