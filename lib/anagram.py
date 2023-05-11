
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        return [w for w in word_list if sorted([letter for letter in w.lower()]) == sorted([letter for letter in self.word.lower()])]

    
