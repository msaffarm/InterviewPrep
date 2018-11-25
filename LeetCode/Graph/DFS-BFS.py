from Graph import *
from collections import deque


def bfs(g,start,path=""):
	q = deque()
	q.append(start)
	visited = set()
	while q:
		curr_node = q.popleft()
		if curr_node in visited:
			continue
		neighbors = curr_node.get_connections()
		for n in neighbors:
			q.append(n)
		print([x.get_id() for x in q])
		# do sth with curr node
		visited.add(curr_node)
	print(path)


def bfs_paths(g,start,goal,paths=[]):
	q = deque()
	q.append(start)
	visited = set()
	while q:
		pass


def dfs(g,start):
	s = deque()
	s.append(start)
	visited = set()
	while s:
		curr_node = s.pop()
		if curr_node in visited:
			continue
		neighbors = curr_node.get_connections()
		for n in neighbors:
			s.append(n)
		print([x.get_id() for x in s])
		visited.add(curr_node)


def recur_dfs(g,start,visited=None):
	if not visited:
		visited = set()
	if start in visited:
		return
	print(start)
	visited.add(start)
	for n in start.get_connections():
		recur_dfs(g,n,visited)


def make_graph():
	g = Graph(type="undirected")
	for i in range(5):
		g.add_vertex(i)
	g.add_edge(0,1,5)
	g.add_edge(0,2,3)	
	g.add_edge(1,3,5)
	g.add_edge(2,3,5)
	g.add_edge(2,4,5)
	return g


def Djikstra(g,start,end):
	pass



def main():
	g = make_graph()
	s = g.get_vertex(4)
	# bfs(g,s)
	# dfs(g,s)
	recur_dfs(g,s)



if __name__ == '__main__':
	main()