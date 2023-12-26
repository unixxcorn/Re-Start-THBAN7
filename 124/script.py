import ceasar_tool as ct

def main():
    print("Ceasar Cipher")
    alphabets = ct.getDoubleAlphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    msg = ct.getMessage()
    key = ct.getCipherKey()
    
    cipher = ct.encryptMessage(msg, key, alphabets)
    print("Cipher: " + cipher)
    
    decipher = ct.decryptMessage(cipher, key, alphabets)
    print("decipher: " + decipher)

if __name__ == "__main__":
    main()