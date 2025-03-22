import playfair
import vigenere

def main():
    print("Playfair Cipher Test")
    key = 'playfair'
    table = playfair.generate_table(key)
    text = 'Hide the gold in the tree stump'
    encrypted_text = playfair.encrypt(table, text)
    print('Encrypted text:', encrypted_text)
    decrypted_text = playfair.decrypt(table, encrypted_text)
    print('Decrypted text:', decrypted_text)

    print("\nVigenère Cipher Test")
    table = vignere.generate_table()
    text = 'attack at dawn'
    key = 'lemon'
    encrypted_text = vignere.encrypt(table, text, key)
    print('Encrypted text:', encrypted_text)
    decrypted_text = vignere.decrypt(table, encrypted_text, key)
    print('Decrypted text:', decrypted_text)

if __name__ == "__main__":
    main()