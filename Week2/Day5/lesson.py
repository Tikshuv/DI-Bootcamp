people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
filtered = filter(lambda name: len(name) <= 4, people)
greeted_people = list(map(lambda name: 'Greetings ' + name, filtered))
print(greeted_people)


from collections import Counter

r = Counter(people[3])
print(r)
