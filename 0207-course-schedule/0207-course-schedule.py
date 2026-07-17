class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        for courses, prereq in prerequisites:
            graph[courses].append(prereq)

        state = [0] * numCourses

        def dfs(course):
            if state [course] == 1:
                return False
            if state [course] == 2:
                return True 

            state [course] = 1

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
