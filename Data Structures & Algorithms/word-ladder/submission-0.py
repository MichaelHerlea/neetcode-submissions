class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjacency = {}
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                if pattern not in adjacency:
                    adjacency[pattern] = []
                adjacency[pattern].append(word)
        
        visit = set([beginWord])
        q = deque([beginWord])
        counter = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return counter
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighbor in adjacency[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            q.append(neighbor)

            counter += 1
        
        return 0
