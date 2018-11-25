from collections import deque

class Solution(object):

	def findMinHeightTrees(self,n,edges):
		if n==1:
			return list(range(n))
		adjList = {}
		for e in edges:
			adjList.setdefault(e[0],[]).append(e[1])
			adjList.setdefault(e[1],[]).append(e[0])
		dist = {}
		for node in range(n):
			queue = deque()
			queue.append((node,0))
			visited = set()
			while queue:
				cur_node,depth = queue.popleft()
				if cur_node in visited:
					continue
				if depth:
					dist.setdefault(node,[]).append(depth)

				for neigh in adjList[cur_node]:
					queue.append((neigh,depth+1))
				visited.add(cur_node)
		
		MHTR = []
		max_height = {x:max(dist[x]) for x in range(n)}
		min_height = min(x[1] for x in max_height.items())
		for i in range(n):
			if max_height[i]==min_height:
				MHTR.append(i)
		return MHTR


	def findMinHeightTreesRemove(self,n,edges):
		if n==1:
			return list(range(n))
		adjList = {}
		for e in edges:
			adjList.setdefault(e[0],[]).append(e[1])
			adjList.setdefault(e[1],[]).append(e[0])
		node_degree = {x:len(adjList[x]) for x in range(n)}
		deleted_nodes = set()
		while True:
			if len(deleted_nodes)==n-1 or len(deleted_nodes)==n-2:
				return [x for x in range(n) if x not in deleted_nodes]
			leaves = [x[0] for x in node_degree.items() if (x[1]==1 or x[1]==0)
			and x[0] not in deleted_nodes]
			# remove leaves iteratively until one or two nodes are remained
			for l in leaves:
				neighbors = adjList[l]
				for x in neighbors:
					node_degree[x] -= 1
				deleted_nodes.add(l)






def main():
	s = Solution()
	edges = [[0,1],[0,2],[2,3],[0,4],[2,5],[5,6],[3,7],[6,8],[8,9],[9,10]]
	n =11
	print(s.findMinHeightTreesRemove(n,edges))
	# print([i for i in range(n)])


if __name__ == '__main__':
	main()