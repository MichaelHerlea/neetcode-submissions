class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisites_dict = {course : [] for course in range(numCourses)}
        output = []

        for course, prerequisite in prerequisites:
            prerequisites_dict[course].append(prerequisite)
        
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for prerequisite in prerequisites_dict[course]:
                if dfs(prerequisite) is False:
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if dfs(course) is False:
                return []
        
        return output