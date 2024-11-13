# Instructions : The goal of the exercise is to create a class that will help you analyze a specific text. A text can
# be just a simple string, like “Today, is a happy day” or it can be an external text file.
#
#
#
# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”
#
# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code
#
# Implement the following methods: a method to return the frequency of a word in the text (assume words are separated
# by whitespace) return None or a meaningful message. a method that returns the most common word in the text. a
# method that returns a list of all the unique words in the text.
#
class Text:
    def __init__(self, text):
        self.text = text.lower()

    def words(self):
        s_words = self.text.split()
        for i, word in enumerate(s_words):
            s_words[i] = ''.join(letter for letter in word if letter.isalpha())
            if s_words[i] == '':
                s_words.pop(i)
        return s_words

    def frequency(self):
        words_set = set(self.words())
        f_dict = {}
        words = self.words()
        for word in words_set:
            f_dict[word] = words.count(word)
        f_dict = dict(sorted(f_dict.items(), key=lambda item: item[1], reverse=True))
        return f_dict

    def most_common(self):
        freq = self.frequency()
        most = max(zip(freq.values(), freq.keys()))[1]
        return most

    def all_uniques(self):
        freq = self.frequency()
        uniques = [word for word in freq if freq[word] == 1]
        return uniques


our_text = Text('A good book would sometimes cost as much as a good house.')
print(our_text.frequency())
print(our_text.most_common())
print(our_text.all_uniques())
text = 'asdada'

#
# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.
#
# Implement a classmethod that returns a Text instance but with a text file:
#
#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.
#
print('Part II')
with open('the_stranger.txt', 'r') as f:
    content = f.read()
    # print(content)

stranger = Text(content)
print(stranger.most_common())
print(stranger.frequency())
print(stranger.all_uniques())
#
# Now, use the provided the_stranger.txt file and try using the class you created above.
#
#
#
# Bonus:
# Create a class called TextModification that inherits from Text.
#
# Implement the following methods:
# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.
# Note: Instead of creating a child class, you could also implements those methods as static methods in the Text class.
#
# Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)
