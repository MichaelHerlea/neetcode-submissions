class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjacency = {character: set() for word in words for character in word}
        visited = {}
        result = []
    
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
                return ""
            
            for j in range(min_length):
                if word1[j] != word2[j]:
                    adjacency[word1[j]].add(word2[j])
                    break
        
        def dfs(value):
            if value in visited:
                return visited[value]
            
            visited[value] = True
            for neighbor in adjacency[value]:
                if dfs(neighbor):
                    return True
            visited[value] = False
            result.append(value)
        
        for n in adjacency:
            if dfs(n):
                return ""
        
        result.reverse()
        return "".join(result)