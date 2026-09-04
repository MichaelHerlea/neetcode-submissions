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