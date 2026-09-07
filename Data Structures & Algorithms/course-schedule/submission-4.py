class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {}
        visit_set = set()
        for course in prerequisites:
            pre_map.setdefault(course[0], []).append(course[1])
        
        def dfs(course):
            if course in visit_set: return False
            if pre_map.get(course, []) == []: return True

            visit_set.add(course)
            for pre in pre_map[course]:
                if not dfs(pre): return False
            visit_set.remove(course)
            pre_map[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        return True