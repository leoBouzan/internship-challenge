def invert_str(s):
    letter = ''
    inverted_str = ''
    for i in range(len(s) - 1, -1, -1):
        letter = s[i]
        inverted_str +=letter
    return inverted_str

while True:
    try:
        s = input('Digite uma string: ')
        print(invert_str(s))

        break

    except ValueError:
        print('Digite uma string válida')
