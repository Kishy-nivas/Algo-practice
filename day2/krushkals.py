
class Graph:
  
  def __init__(self,vertices):
    self.graph = []
    self.v= vertices
    
  
  def addEdge(self,u,v,w):
    self.graph.append([u,v,w])
  
  
  
  def find_parent(self,parent,i):
    if parent[i] == -1:
      return i 
    else:
      return self.find_parent(parent,parent[i]) # trace back the parent 
    
  def union(self,rank,parent,i,j):
    if rank[i]< rank[j]:
      parent[i] = j
    elif rank[i] > rank[j]:
      parent[j] = i  
    else: 
      rank[i]+=1 
      parent[j]=i 
  
  

  
  def generate_mst(self):
    
    graph_index =0 # index value to  graph 
    
    sorted_graph = sorted(self.graph,key = lambda item: item[2]) # arrange in soreted order 
    
    rank= [0]*self.v 
    parent = [-1] * self.v 
    mst = []
    
    mst_size =0 
    while mst_size<self.v-1:
      
      u,v,w= sorted_graph[graph_index]
      graph_index+=1 
      
      u_set = self.find_parent(parent, u)
      v_set = self.find_parent(parent,v)
      
      if u_set != v_set: # cycle check
        mst.append([u,v,w])
        self.union(rank,parent,u_set,v_set)
        mst_size += 1 
    
    print(mst)

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.generate_mst() 

        
        
    
    
  
    
  