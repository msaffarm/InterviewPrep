class Vertex(object):

	def __init__(self,id):
		self._id = id
		self._neighbors = {}

	def add_neighbor(self,n,weight=0):
		self._neighbors[n] = weight

	def __str__(self):
		return "vertex id= " + str(self._id) + ", neighbors= " + str([x.get_id() for 
			x in self._neighbors])

	def get_connections(self):
		return list(self._neighbors.keys())

	def get_id(self):
		return self._id

	def get_weight(self,n):
		if n not in self._neighbors:
			raise Exception("No neighbor found!")
		return self._neighbors[n]


class Graph(object):

	def __init__(self,type="directed"):
		self._vertices = {}
		self._type = type

	def add_vertex(self,key):
		new_vertex = Vertex(key)
		self._vertices[key] = new_vertex

	def add_edge(self,from_v,to_v,weight=0):
		if self._type=="directed":
			self._vertices[from_v].add_neighbor(self._vertices[to_v],weight=weight)
		elif self._type=="undirected":
			self._vertices[from_v].add_neighbor(self._vertices[to_v],weight=weight)
			self._vertices[to_v].add_neighbor(self._vertices[from_v],weight=weight)

	def __contains__(self,v):
		return v in self._vertices

	def get_vertices(self):
		return list(self._vertices.keys())

	def get_vertex(self,v):
		return self._vertices[v]



def main():

	g = Graph(type="undirected")
	for i in range(3):
		g.add_vertex(i)
	print(g.get_vertices())
	g.add_edge(0,1,10)
	g.add_edge(2,1,3)	
	g.add_edge(0,2,5)

	print(g.get_vertex(1))


if __name__ == '__main__':
	main()


