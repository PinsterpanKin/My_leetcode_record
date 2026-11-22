from collections import deque

class Solution:
    def alienOrder(self, words: list[str]) -> str:
        # 1. Every letter is a node
        adj = {c: set() for w in words for c in w}
        indeg = {c: 0 for c in adj}

        # 2. Build edges from adjacent pairs
        for w1, w2 in zip(words, words[1:]):
            found = False
            for a, b in zip(w1, w2):
                if a != b:
                    if b not in adj[a]:          # avoid duplicate edges
                        adj[a].add(b)
                        indeg[b] += 1
                    found = True
                    break
              # no difference found in the overlapping part
            if found and len(w1) > len(w2):
                    return ""                    # prefix case: invalid

        # 3. Topological sort
        q = deque(c for c in indeg if indeg[c] == 0)
        out = []
        while q:
            c = q.popleft()
            out.append(c)
            for nxt in adj[c]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)

        # 4. If some letters were never placed, there was a cycle
        return "".join(out) if len(out) == len(adj) else ""