# f = open('sample.txt')xz≈
# content = f.read()
# print(content)
# f.close()


# automatically close the file "with"
# with open('sample.txt', 'w+', encoding='utf-8') as f:
#     # content = f.read()
#     # print(content)
#     for i in range(1, 11):
#         f.write(f'this is line {i}\n')
#     # f.seek(0)
#     content = f.read()
#     print(content)

# with open('ex.txt', 'a+') as f:
#     f.write('\nDmitry')
#     f.seek(0)
#
#     content = f.readlines()
#     for i, line in enumerate(content):
#         if line == 'Luke\n':
#             line = line.replace('\n', ' ')
#             line += 'Skywalker\n'
#             content[i] = line
#     with open('ex.txt', 'w+') as f:
#         f.writelines(content)
#
#     with open('ex.txt', 'r+') as f:
#         f.seek(0)
#         content = f.readlines()
#         f.seek(0)
#         line = f.readline(5)
#         print(content)
#         print(line)
#         print(content.count('Darth\n'), content.count('Luke Skywalker\n'), content.count('Lea\n'))

import json

# conv py dict into json file
my_family = {
    "parents": ['Beth', 'Jerry'],
    "children": ['Summer', 'Morty']
}

json_file = 'family.json'

with open('family.json', 'w') as f:
    json.dump(my_family, f)  # name of dict and file object

# from py dict to json string
json_my_family = json.dumps(my_family)
print(json_my_family)
print(type(json_my_family))

# load json string to py dict
parsed_family = json.loads(json_my_family)
print(parsed_family)
print(type(parsed_family))

# convert json file into py dict

# with open('family.json', 'r') as f:
    # print(json.load(f))

