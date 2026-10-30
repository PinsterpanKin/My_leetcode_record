class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        from collections import defaultdict, deque

        # Create a graph and a list to track in-degrees
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        # Build the graph and in-degree list
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Initialize a queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed_courses = 0

        while queue:
            course = queue.popleft()
            completed_courses += 1

            # Decrease the in-degree of neighboring courses
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If we completed all courses, return True; otherwise, return False
        return completed_courses == numCourses