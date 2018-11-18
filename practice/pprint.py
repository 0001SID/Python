import pprint
message = 'This is just a string to check which character appeat how many time'
count = {}
for character in message:
    count.setdefault(character,0)
    count[character] += 1
# pprint.pprint(count)
print(pprint.pformat(count))