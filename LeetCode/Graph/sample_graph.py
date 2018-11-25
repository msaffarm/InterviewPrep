from collections import defatultdict

class Graph(object):
	def __init__(self):
		self.vertices = set()
		self.edges = defatultdict(set)

	def add_vertex(self,v):
		self.vertices.add(v)

	def add_edge(self,s,t):
		self.edges[s].add(t)

	def add_edges(self,edge_list):
		for pair in edge_list:
			s,t = pair
			self.edge_list[s].add(t)
		




def main():
	pass


if __name__ == '__main__':
	main()