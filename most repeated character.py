sentence = "This is a common interview question"
max = 0
char_dict = {}

for char in sentence.lower():
    if char in char_dict:
        char_dict[char] += 1
    else:
        char_dict[char] = 1
for key in char_dict:
    if max < char_dict[key] and key != ' ':
        max = char_dict[key]
        word = key
           

print(f'the most repeated character is {word} and it is repeated {max} times')





#########easy wayyyyyyyyyyyyyyy
# max = 0
# for char in sentence.lower():
#     if max < sentence.count(char):
#         max = sentence.count(char)
#         word = char

# print(f'the most repeated character is {word} and it is repeated {max} times')
