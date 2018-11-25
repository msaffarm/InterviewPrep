def is_lead_node(root):

	if not root.left and not root.right:
		return True
	return False


def decodeHuff(root,s):

	idx = 0
	decoded = ""
	while idx < len(s):
		current_node = root
		while True:
			if is_lead_node(current_node):
				decoded += current_node.data
				break
			code = s[idx]
			if code==1:
				current_node = current_node.right
			else:
				current_node = current_node.left
			idx += 1

	return decoded