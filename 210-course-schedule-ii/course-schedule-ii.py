class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        visited = set()
        path = set()
        result  = []
        def fun(course) :
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            for i in range(len(prerequisites)) :
                if prerequisites[i][0] == course:
                    result1 = fun(prerequisites[i][1])
                    if result1 == False:
                        return False
            path.remove(course)
            visited.add(course)
            result.append(course)
            return True
        for course in range(numCourses):
            if fun(course) == False:
                return []
        return result