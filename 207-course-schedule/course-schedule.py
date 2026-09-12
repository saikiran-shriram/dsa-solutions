class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        path = set()
        def fun(course) :
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            for i in range(len(prerequisites)) :
                if prerequisites[i][0] == course:
                    result = fun(prerequisites[i][1])
                    if result == False:
                        return False
            path.remove(course)
            visited.add(course)
            return True
        for course in range(numCourses):
            if fun(course) == False:
                return False
        return True
                
            
                
