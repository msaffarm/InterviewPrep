from collections import defaultdict, deque


class Graph(object):
	def __init__(self,vertices=list()):
		self.vertices = vertices
		self.edges = defaultdict(list)

	def add_vertex(self,v):
		self.vertices.append(v)

	def add_edge(self,s,t):
		self.edges[s].append(t)

	def add_edges(self,edge_list):
		for pair in edge_list:
			s,t = pair
			self.edges[s].append(t)

	def add_weighted_edge(self,s,t,w):
		self.edges[s].append((t,w))

	def add_weighted_edges(self,edge_list):
		for triple in edge_list:
			s,t,w = triple
			self.edges[s].append((t,w))


def dfs(g,node,visited,sol):
	visited.add(node)
	for neigh in g.edges[node]:
		if neigh not in visited:
			dfs(g,neigh,visited,sol)
	sol.append(node)


# Topological sorting (only for DAGs)
def topological_sort(g):
	visited = set()
	sol = deque()
	for node in g.vertices:
		if node not in visited:
			dfs(g,node,visited,sol)
	return [x for x in reversed(sol)]


# find shortest path in DAG in O(V + E) using topological sorting
def find_shortest_path(g):
	pass


def main():
	g = Graph(list(range(6)))
	g.add_edges([(2,3),(3,1),(4,0),(4,1),(5,0),(5,2)])
	g.add_weighted_edges([])
	d = defaultdict(lambda:10.0)



if __name__ == '__main__':
	main()