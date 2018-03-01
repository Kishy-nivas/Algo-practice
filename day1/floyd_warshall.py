V= 4 
INF = 99999 
dist = [[0 for x in range(V)] for y in range (V)]

def floyd_warshall(graph):
  
  # find the intermediate node k  between i and j, such that the path is optimized 
  for k in range(V): 
    for i in range(V):
      for j in range(V):
        if graph[i][j] > graph[i][k] + graph[k][j]:
          graph[i][j] = graph[i][k] + graph[k][j]
  
  
  print(graph)
        
  
  
  
  


g= [[0,5,INF,10],
             [INF,0,3,INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
        ]
floyd_warshall(g)