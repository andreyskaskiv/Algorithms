1. Поиск в ширину (Breadth-first search, BFS) - O(V+E)
   ```python
   def bfs(graph, start):
       visited = set()
       queue = [start]
   
       while queue:
           vertex = queue.pop(0)
           if vertex not in visited:
               visited.add(vertex)
               queue.extend(graph[vertex] - visited)
   
       return visited
   
   ```
2. Поиск в глубину (Depth-first search, DFS) - O(V+E)
   ```python
   def dfs(graph, start, visited=None):
       if visited is None:
           visited = set()
       visited.add(start)
       for next in graph[start] - visited:
           dfs(graph, next, visited)
       return visited
   
   ```
3. Алгоритм Дейкстры (Dijkstra's algorithm) - O((V+E)logV) при использовании кучи, O(V^2) в худшем случае при
   использовании массива
   ```python
   import heapq
   
   def dijkstra(graph, start):
       distances = {vertex: float('infinity') for vertex in graph}
       distances[start] = 0
       pq = [(0, start)]
   
       while pq:
           current_distance, current_vertex = heapq.heappop(pq)
   
           if current_distance > distances[current_vertex]:
               continue
   
           for neighbor, weight in graph[current_vertex].items():
               distance = current_distance + weight
   
               if distance < distances[neighbor]:
                   distances[neighbor] = distance
                   heapq.heappush(pq, (distance, neighbor))
   
       return distances
   
   ```
4. Алгоритм Флойда-Уоршелла (Floyd–Warshall algorithm) - O(V^3)
   ```python
   def floyd_warshall(graph):
       dist = {v1: {v2: graph[v1][v2] if v2 in graph[v1] else float('infinity')
                    for v2 in graph} for v1 in graph}
       for k in graph:
           for i in graph:
               for j in graph:
                   dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
       return dist
   
   ```
5. Алгоритм Прима (Prim's algorithm) - O(E*log(V)) при использовании кучи
   ```python
   import heapq
   
   def prim(graph, start):
       visited = set()
       edges = [(weight, start, neighbor) for neighbor, weight in graph[start].items()]
       heapq.heapify(edges)
       total_weight = 0
       mst = []
   
       while edges:
           weight, current_vertex, next_vertex = heapq.heappop(edges)
           if next_vertex not in visited:
               visited.add(next_vertex)
               mst.append((current_vertex, next_vertex, weight))
               total_weight += weight
               for neighbor, weight in graph[next_vertex].items():
                   if neighbor not in visited:
                       heapq.heappush(edges, (weight, next_vertex, neighbor))
   
       return mst, total_weight
   
   ```
6. Алгоритм Крускала (Kruskal's algorithm) - O(E*log(E)) при использовании кучи
   ```python
   def kruskal(graph):
       parent = {}
       rank = {}
   
       def find(vertex):
           if parent[vertex] != vertex:
               parent[vertex] = find(parent[vertex])
           return parent[vertex]
   
       def union(vertex1, vertex2):
           root1 = find(vertex1)
           root2 = find(vertex2)
           if root1 != root2:
               if rank[root1] > rank[root2]:
                   parent[root2] = root1
               else:
                   parent[root1] = root2
                   if rank[root1] == rank[root2]:
                       rank[root2] += 1
   
       for vertex in graph:
           parent[vertex] = vertex
           rank[vertex] = 0
   
       edges = [(weight, start, end) for start in graph for end, weight in graph[start].items()]
       edges.sort()
       mst = []
       total_weight = 0
   
       for weight, start, end in edges:
           if find(start) != find(end):
               union(start, end)
               mst.append((start, end, weight))
               total_weight += weight
   
       return mst, total_weight
   
   ```
