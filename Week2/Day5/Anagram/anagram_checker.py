from collections import Counter


class AnagramChecker:
    def __init__(self, file):
        with open(file, 'r') as f:
            file = f.read()
            file = file.split()
        self.file = file
        self.a_file = []
        for word in self.file:
            self.a_file.append(Counter(word))
        # print(self.a_file)

    def is_valid(self, word):
        if word.upper() in self.file:
            return True
        return False

    def get_anagrams(self, word):
        word = word.upper()
        self.check_word(word)
        anagrams = []
        a_word = Counter(word)
        if not self.check_word(word):
            print("There's no such a word in English, try again\n")
            return
        print("This is a valid English word")
        for i, anagram in enumerate(self.a_file):
            # print(i, anagram)
            # print(a_word)
            if a_word == anagram:
                anagrams.append(self.file[i].lower())
        if word.lower() in anagrams:
            anagrams.remove(word.lower())
        if len(anagrams) >= 1:
            return f'Anagrams for word "{word.lower()}" are: {', '.join(anagrams)}\n'
        else:
            return "There's no anagrams for this word"

    def check_word(self, word):
        if word in self.file:
            return True
        return False


    # @staticmethod
    # def anagram_finder(word1, word2):
    #     if Counter(word1) == Counter(word2):
    #         return True
    #     else:
    #         return False


# our_file = AnagramChecker('sowpods.txt')
# print(our_file.get_anagrams('meat'))
