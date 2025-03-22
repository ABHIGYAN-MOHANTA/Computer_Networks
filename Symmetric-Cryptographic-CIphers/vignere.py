def generate_table():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    table = []
    for i in range(26):
        row = ''
        for j in range(26):
            row += alphabet[(i + j) % 26]
        table.append(row)
    return table

def prepare_input(text):
    text = text.replace(' ', '').lower()
    return text

def encrypt(table, text, key):
    text = prepare_input(text)
    key = prepare_input(key)
    key_index = 0
    encrypted_text = ''
    for char in text:
        key_char = key[key_index % len(key)]
        key_index += 1
        row = table[ord(char) - ord('a')]
        col = ord(key_char) - ord('a')
        encrypted_text += row[col]
    return encrypted_text

def decrypt(table, text, key):
    text = prepare_input(text)
    key = prepare_input(key)
    key_index = 0
    decrypted_text = ''
    for char in text:
        key_char = key[key_index % len(key)]
        key_index += 1
        row = table[ord(key_char) - ord('a')]
        col = row.index(char)
        decrypted_text += chr(col + ord('a'))
    return decrypted_text

table = generate_table()
text = 'attackatdawn'
key = 'lemon'
encrypted_text = encrypt(table, text, key)
print('Encrypted text:', encrypted_text)
decrypted_text = decrypt(table, encrypted_text, key)
print('Decrypted text:', decrypted_text)