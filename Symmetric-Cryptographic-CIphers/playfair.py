def generate_table(key):
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    table = []
    for char in key:
        if char not in table and char in alphabet:
            table.append(char)
    for char in alphabet:
        if char not in table:
            table.append(char)
    table = [table[i:i+5] for i in range(0, 25, 5)]
    return table

def prepare_input(text):
    text = text.replace(' ', '').lower()
    text = text.replace('j', 'i')
    return text

def find_position(table, char):
    for i in range(5):
        for j in range(5):
            if table[i][j] == char:
                return (i, j)

def encrypt(table, text):
    text = prepare_input(text)
    if len(text) % 2 != 0:
        text += 'x'
    encrypted_text = ''
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i+1]
        pos1 = find_position(table, char1)
        pos2 = find_position(table, char2)
        if pos1[0] == pos2[0]:
            encrypted_text += table[pos1[0]][(pos1[1]+1)%5] + table[pos2[0]][(pos2[1]+1)%5]
        elif pos1[1] == pos2[1]:
            encrypted_text += table[(pos1[0]+1)%5][pos1[1]] + table[(pos2[0]+1)%5][pos2[1]]
        else:
            encrypted_text += table[pos1[0]][pos2[1]] + table[pos2[0]][pos1[1]]
    return encrypted_text

def decrypt(table, text):
    text = prepare_input(text)
    decrypted_text = ''
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i+1]
        pos1 = find_position(table, char1)
        pos2 = find_position(table, char2)
        if pos1[0] == pos2[0]:
            decrypted_text += table[pos1[0]][(pos1[1]-1)%5] + table[pos2[0]][(pos2[1]-1)%5]
        elif pos1[1] == pos2[1]:
            decrypted_text += table[(pos1[0]-1)%5][pos1[1]] + table[(pos2[0]-1)%5][pos2[1]]
        else:
            decrypted_text += table[pos1[0]][pos2[1]] + table[pos2[0]][pos1[1]]
    return decrypted_text

key = 'playfair'
table = generate_table(key)
text = 'Hide the gold in the tree stump'
encrypted_text = encrypt(table, text)
print('Encrypted text:', encrypted_text)
decrypted_text = decrypt(table, encrypted_text)
print('Decrypted text:', decrypted_text)