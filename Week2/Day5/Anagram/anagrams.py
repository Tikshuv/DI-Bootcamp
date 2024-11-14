from anagram_checker import AnagramChecker

while True:
    our_anagram = AnagramChecker('sowpods.txt')
    word = input('Type a word for anagrams(just one word) or type "exit" to exit: ')
    if word.isalpha():
        if word.lower() == 'exit':
            break
    if len(word.split()) > 1:
        raise ValueError("Only one word is allowed")
    for letter in word:
        if not letter.isalpha():
            raise ValueError('Only english letter are allowed')
    print(f"\nYour word is: {word}")
    word = word.upper().strip()
    print(our_anagram.get_anagrams(word))


