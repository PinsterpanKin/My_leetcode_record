#Using BFS to serialize and deserialize a binary tree, super efficient and easy to understand
class AmazingCodec:
    from collections import deque

    def serialize(self, root):
        if not root:
            return ""
        out, q = [], deque([root])
        while q:
            node = q.popleft()
            if node:
                out.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                out.append("#")
        return " ".join(out)

    def deserialize(self, data):
        if not data:
            return None
        tokens = data.split()
        root = TreeNode(int(tokens[0]))
        q, i = deque([root]), 1
        while q:
            node = q.popleft()
            if tokens[i] != "#":
                node.left = TreeNode(int(tokens[i]))
                q.append(node.left)
            i += 1
            if tokens[i] != "#":
                node.right = TreeNode(int(tokens[i]))
                q.append(node.right)
            i += 1
        return root

#Using DFS to serialize and deserialize a binary tree
class MyCodec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(node, string):
            if not node:
                string += '# '
            else:
                string += str(node.val) + ' '
                string = rserialize(node.left, string)
                string = rserialize(node.right, string)
            return string
        
        return rserialize(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            if l:
                val = l.pop()
                if val == '#':
                    return None
                node = TreeNode(int(val))
                node.left = rdeserialize(l)
                node.right = rdeserialize(l)
                return node

        data_list = data.split()
        data_list.reverse()
        root = rdeserialize(data_list)
        return root