from random import shuffle
text = input("Enter a string: ")
# text = 'HelloWorld'
while len(text) != 10:
    if len(text) > 10:
        print("Too many characters, type less")
    else:
        print("Too few characters, type more")
    text = input("Enter the string again: ")
chars = text[0] + text[-1]
print(chars)

new_str = ''
for i in text:
    new_str += i
    print(new_str)
shuffle_str = list(text)
shuffle(shuffle_str)
print (''.join(shuffle_str))
