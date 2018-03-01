from collections import defaultdict

class Graph: 
  def __init__(self,vertices):
    self.size = vertices 
    self.graph = defaultdict(list)
    
  def addEdge(self,u,v):
    self.graph[u].append(v)
  
  def topological_sort(self):
    
    queue =[]
    ans = []
    in_coming_node = [0]*self.size   

    for i in range(self.size):            # find incoming nides 
      for adj in self.graph[i]:
        in_coming_node[adj] += 1
    
    #print(in_coming_node)
    for i in range(self.size):              #there must be a incoming node with value zero, since it is acyclic graph 
      if in_coming_node[i] ==0:
        queue.append(i)                          # add it to queue or stack 
    while (queue ):
      val = queue.pop(0)
      ans.append(val)
      for i in self.graph[val]:               # update it's adjancent vertices 
        in_coming_node[i] -= 1              # since it has been removed,decrement it
        if in_coming_node[i] == 0:
            queue.append(i)
      
    print(queue)
    print(ans)
            
    
 
      
        
g= Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
g.topological_sort() 