#include <iostream>
#include <functional> 
#include <climits>
#include <algorithm> 
#include <queue>
using namespace std;

typedef pair<int,int> ipair;
int INF = INT_MAX;
class Graph{
  int size; 
  vector<ipair> *adj;
  
  public:
  Graph(int si){
    size = si ;
    adj = new vector<ipair>[size];
    
  }
  
  void addEdge(int u, int v,int w){
    adj[u].push_back(make_pair(v,w));
  }
  
  void Dijkstra(int s){
    priority_queue<ipair,vector<ipair>, greater<ipair>> pq;  //use as min-heap
    vector<int> dist(size,INF);
    vector<int> parent(size,-1);
    
    pq.push(make_pair(0,s)); //weight goes first, to sort 
    dist[s] = 0;
    
    while(!pq.empty()){
      int u = pq.top().second;
      pq.pop();
      
      vector<ipair>::iterator it;
      for(it = adj[u].begin();it!=adj[u].end();it++){
        int v= (*it).first;
        int weight = (*it).second;
        
        if (dist[v] > dist[u] + weight){       //relaxation 
          dist[v] = dist[u] + weight;
          pq.push(make_pair(dist[v],v));
          parent[v] = u; 
          
        }
        
      }
    }
    for(int i =0 ; i<this->size ; i++){
      cout<<i<<"\t"<<parent[i]<<"\n";
    }
    
    
  }
  
  
  
};


int main() {
  Graph g(9);
   g.addEdge(0, 1, 4);
    g.addEdge(0, 7, 8);
    g.addEdge(1, 2, 8);
    g.addEdge(1, 7, 11);
    g.addEdge(1, 0, 4);
    g.addEdge(2, 8, 2);
    g.addEdge(2, 5, 4);
    g.addEdge(2, 3, 7);
    g.addEdge(2, 1, 8);
    g.addEdge(3, 5, 14);
    g.addEdge(3, 4, 9);
    g.addEdge(3, 2, 7);
    g.addEdge(4, 3, 9);
    g.addEdge(4, 5, 10);
    g.addEdge(5, 6, 2);
    g.addEdge(5, 2, 4);
    g.addEdge(5, 4, 10);
    g.addEdge(5, 3, 14);
    g.addEdge(6, 8, 6);
    g.addEdge(6, 7, 1);
    g.addEdge(6,5,2);
    g.addEdge(7, 8, 7);
    g.addEdge(7, 1, 11);
    g.addEdge(7, 0, 8);
    g.addEdge(7, 6, 1);
    g.addEdge(8, 7, 7);
    g.addEdge(8, 2, 2);
    g.addEdge(8, 6, 6);

    g.Dijkstra(0);
  
}