import heapq
from Graph import *

def make_graph():
	g = Graph(type="undirected")
	for i in range(6):
		g.add_vertex(i)
	g.add_edge(0,1,5)
	g.add_edge(0,2,3)	
	g.add_edge(1,3,3)
	g.add_edge(2,3,4)
	g.add_edge(2,4,9)
	g.add_edge(3,4,6)
	g.add_edge(3,5,7)
	g.add_edge(4,5,4)
	return g


def find_shortest_path(start,goal,nodes_prev):
	path = ""
	cur_node = goal
	while cur_node!=start:
		path += str(cur_node.get_id())
		cur_node = nodes_prev[cur_node]
	path += str(cur_node.get_id())
	print(path[::-1])


# shortest path in non-negative graph with O(E + VlogV)
def Djisktra(g,start):
	visited = set()
	nodes_dist = {}
	nodes_dist[start] = 0
	nodes_prev = {}
	nodes_prev[start] = None
	nodes = []
	nodes.append((0,start))
	heapq.heapify(nodes) # min heap
	while nodes:
		cur_node = heapq.heappop(nodes)[1]
		if cur_node in visited:
			continue
		for n in cur_node.get_connections():
			dist = nodes_dist[cur_node] + cur_node.get_weight(n)
			if n not in nodes_dist or dist < nodes_dist[n]:
				nodes_dist[n] = dist
				heapq.heappush(nodes,(dist,n))
				nodes_prev[n] = cur_node

		visited.add(cur_node)

	print([(x.get_id(),y) for x,y in nodes_dist.items()])
	return nodes_prev


def main():
	g = make_graph()
	start = g.get_vertex(0)
	goal = g.get_vertex(5)
	print(start)
	nodes_prev = Djisktra(g,start)
	find_shortest_path(start,goal,nodes_prev)



if __name__ == '__main__':
	main()