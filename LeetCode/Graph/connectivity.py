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


# strongly conncted graph! 
# for undirected graph just do a BFS/DFS from any vertex



def main():
	d = defaultdict(lambda:None)
	print(d[1])


if __name__ == '__main__':
	main()