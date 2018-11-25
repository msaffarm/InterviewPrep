from collections import deque,defaultdict


def bfs(adj_list,start):
	queue = deque()
	visited_nodes = set()
	queue.append((start,0))
	while queue:
		cur_node,depth = queue.popleft()
		if cur_node in visited_nodes:
			continue
		for n in adj_list[cur_node]:
			queue.append((n,depth+1))
		visited_nodes.add(cur_node)
	return cur_node,depth


def findMaxPath(E):
	adj_list = {}
	for e in E:
		n1,n2 = e
		adj_list.setdefault(n1,[]).append(n2)
		adj_list.setdefault(n2,[]).append(n1)
	end_node,_ = bfs(adj_list,E[0][0])
	print(end_node)
	_,depth = bfs(adj_list,end_node)
	return depth


def solution(A, E):
    # write your code in Python 3.6
    node2label = {}
    for i,v in enumerate(A):
    	node2label[i+1] = v
    label2node = {v:k for k,v in node2label.items()}
    edges = set()
    i=0
    while i < len(E):
    	edges.add((E[i],E[i+1]))
    	i += 2
    label_edge = {}
    for e in edges:
    	n1,n2 = e
    	if node2label[n1]==node2label[n2]:
    		label_edge.setdefault(node2label[n1],[]).append(e)
    print(label_edge)
    for k,E in label_edge.items():
    	print(findMaxPath(E))


def main():
	A = [1,1,1,2,2,3,3,3,3,3,3,3]
	E = [1,2,1,3,2,4,2,5,3,6,3,7,6,8,6,9,8,10,8,11,10,12]
	solution(A,E)



if __name__ == '__main__':
	main()