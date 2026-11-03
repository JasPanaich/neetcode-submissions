class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create empty list of prereq for every course
        preMap = { i:[] for i in range(numCourses)}
        # Append course and prereqs to lists
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet to store all courses along current DFS path
        visitSet = set()
        def dfs(crs): # Visit every course
            # Base cases
            if crs in visitSet:
                return False
            if preMap[crs] == []: # Has no prereq
                return True
            
            visitSet.add(crs) # Currently visiting course and run dfs on prereqs
            for pre in preMap[crs]:
                if not dfs(pre): return False
            # If doesn't execute, its a course that can be taken
            visitSet.remove(crs) # No longer visiting this
            preMap[crs] = [] # If we have to run DFS again
            return True

        # May need to call it for every single course since it could potentially be not fully connected 
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True 


