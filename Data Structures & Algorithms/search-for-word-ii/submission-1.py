class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = PrefixTree()
        for word in words:
            trie.insert(word)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or board[r][c] not in node.children):
                return;
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_valid_word: res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie, "")
        
        return list(res)
        
class PrefixTree:
    def __init__(self):
        self.children = {}
        self.is_valid_word = False

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.is_valid_word = True
            return
        if word[0] not in self.children:
            self.children[word[0]] = PrefixTree()
        self.children[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.is_valid_word
        if word[0] not in self.children:
            return False
        return self.children[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        if prefix[0] not in self.children:
            return False
        return self.children[prefix[0]].startsWith(prefix[1:])