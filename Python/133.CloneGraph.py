from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}

        def traverse(curr: 'Node') -> 'Node':
            if curr in visited:
                return visited[curr]
            
            copy = Node(curr.val)
            visited[curr] = copy
            
            for neighbor in curr.neighbors:
                copy.neighbors.append(traverse(neighbor))
                
            return copy

        return traverse(node)