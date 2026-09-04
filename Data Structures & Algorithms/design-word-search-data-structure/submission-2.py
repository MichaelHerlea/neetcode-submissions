class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_valid_word = False

    def addWord(self, word: str) -> None:
        if len(word) == 0:
            self.is_valid_word = True
            return
        if word[0] not in self.children:
            self.children[word[0]] = WordDictionary()
        self.children[word[0]].addWord(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.is_valid_word
        if word[0] == '.':
            for child in self.children.values():
                if (child.search(word[1:])):
                    return True
            return False;
        if word[0] not in self.children:
            return False
        return self.children[word[0]].search(word[1:])
        
