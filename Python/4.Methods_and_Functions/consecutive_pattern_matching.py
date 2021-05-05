word = input()
word_list = list(word)
reduce = []

pattern = int(input())

for index, letter in enumerate(word):
    counter = 0
    oindex=index
    for i in range(pattern):
        if index > (len(word)-1):
            counter = 1
            break
        if letter == word[index]:
            counter == 0
        else:
            counter = 1
        index+=1
        if not(index > len(word)-1):
            if letter == word[index]:
                counter == 1
    print('break{}'.format(oindex))    
    if counter == 0:
        print('check{}'.format(oindex))
        for j in range(pattern):
            reduce.append(oindex)
            oindex+=1

for i in reduce[::-1]:
    word_list.pop(i)

print(''.join(word_list))

    
