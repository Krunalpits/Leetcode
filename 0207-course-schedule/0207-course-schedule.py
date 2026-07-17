class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        if there is cycle its impossible 
        so find if unweighted graph is cyclic or acyclic.

        keep ana djacency list/hashmap => courses : prereqs list
        one visited set to store courses thqt have been viisted. 

        when you visit a course, check its prereqs from hashmap. visit prereq. add prereq also to visited.

        if we visit a course thats already in the visisted set befoen that means cycle detected.
        
        """
        hashmap={}
        #populate premap to store all course and their prereqs
        hashmap={i:[] for i in range(numCourses)}
        for c,pre in prerequisites:
            hashmap[c].append(pre)
        visited=set()
        def dfs(course):
            if course in visited:
                return False
            if hashmap[course]==[]:
                return True
            visited.add(course)
            #explore prereqs of visited node
            for prereq in hashmap[course]:
                result=dfs(prereq)
                 #if no cycle for prereq->true->can finish allcourses
                if not result:
                    return False #cycle detected for prereq
            visited.remove(course)
            hashmap[course]=[]
            return True

        for course,pre in prerequisites:
            if not dfs(course):
                return False
        return True   

