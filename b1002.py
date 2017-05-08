s = raw_input()

strlen = len(s)

sum = 0

for i in range(strlen):

    sum = sum + int(s[i])
    
spell = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']

sum = str(sum)

sumlen = len(sum)

for i in range(sumlen-1):

    print spell[int(sum[i])],
    
print spell[int(sum[sumlen-1])]
