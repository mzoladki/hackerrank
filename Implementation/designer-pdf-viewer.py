h = list(map(int, input().strip().split(' ')))
word = input().strip()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
dictionary = {}

for i, j in enumerate(alphabet):
    dictionary[j] = h[i]


height = 0

for i in word:
    if dictionary[i] > height:
        height = dictionary[i]

print("Dlugosc slowa {0}, najwieksza litera: {1}".format(len(word), height))

print(len(word)*height)
