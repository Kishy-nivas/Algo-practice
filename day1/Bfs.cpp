#include <iostream>
#include <vector> 
#include <queue> 
using namespace std;

class Bfs{
  vector<int> *v; 
  int size; 
  
  public:
  Bfs(int V){
    v= new vector<int>[V];
    this->size = V;
  }
  
  void addEdge(int from ,int to){
    v[from].push_back(to);
  }
  
  void bfs(int s){
    bool *visited = new bool[this->size];
    for(int i = 0 ;i <size ; i++)
      visited[i] = false;
    
    queue<int> q;
    vector<int> ::iterator i;
   
    q.push(s);
    while(!q.empty()){
      int curr_vertice = q.front();
      q.pop();
      visited[curr_vertice] = true;
      cout<< curr_vertice<<"\n";
      
      for(i = v[curr_vertice].begin();i!= v[curr_vertice].end(); i++)
      {
        if(!visited[*i]){
          visited[*i] = true;
          q.push(*i);
        }
          
        
      }
      
    }
      
}
    
};

int main() {
  int V;
  cin>>V;
	Bfs b(V);
	b.addEdge(0,1);
	b.addEdge(0,2);
	b.addEdge(1,2);
	b.addEdge(2,0);
	b.addEdge(2,3);
	b.addEdge(3,3);
	b.bfs(2);
	return 0;
}
