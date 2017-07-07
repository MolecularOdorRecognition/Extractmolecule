import json
file = open('convertedFile.txt', 'r', encoding='utf-8')
nfile = open('converted.txt', 'wb')

tar = file.read()

# print(type(tar))
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

for x in range(len(tar)):
    if tar[x] == '<':
        flag = 0
        while tar[x] != '>':
            if flag == 1:
                if tar[x] == "\\":
                    nfile.write('\n'.encode("utf-8"))
                    x += 2
                nfile.write(tar[x].encode("utf-8"))
                # print(tar[x], end="")
            x += 1
            if tar[x] == "\'":
                flag = 1
        nfile.write('\n\n'.encode("utf-8"))
        # print('\n')
nfile.close()
file.close()
f = open('converted.txt', 'r', encoding="utf-8")
tar = f.readlines()
search = {}
d = ''
for x in range(3,len(tar)):
    if tar[x].isupper() and ':' not in tar[x]:
        if tar[x].isalnum():
            if '-' in tar[x]:
                d = tar[x]
                break
        else:
            d = tar[x]
            break

search[d] = {}
search[d]['name'] = d
y = ['name']
for x in range(4,len(tar)):
    if tar[x].isupper() and ':' not in tar[x] and '/' not in tar[x]:
        # print("True")
        # y = list(tar[x].split(":"))
        # search[d][y[0]] = tar[x]
        if hasNumbers(tar[x]):
            # print('in it')
            if ',' in tar[x] or '-' in tar[x]:
                d = tar[x]
        else:
            # print(tar[x])
            d = tar[x]
        while len(tar[x]) == 0 or tar[x] == '' or tar[x] == "'\n" or tar[x] == '\n':
            x += 1
        # print(d)
        search[d] = {}
        y = ['name']
        search[d][y[0]] = d
    if ':' in tar[x]:
        # print(tar[x])
        y = list(tar[x].split(":"))
        search[d][y[0]] = y[1]
    else:
        # print(tar[x])
        # print(d, 'This is y', y)
        search[d][y[0]] += str(tar[x])
    # print(tar[x])
# print('This is my dictionary\n\n\n', search)
jso = json.dumps(search)
target = open('search.txt', 'w+')
target.write(jso)
target.close()

