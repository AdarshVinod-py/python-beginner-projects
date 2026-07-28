def encrypt(word : str, key : int) -> str:
    char_list : list=[]
    for i in word:
        word_ascii : int = ord(i)
        encrypted_char : str = chr(word_ascii ^ key)
        char_list.append(encrypted_char)
    encrypetd_word : str = "".join(char_list)
    return encrypetd_word


word : str= input("Enter Word:\n")
try:
    key : int = int(input("Enter Key:\n"))
except ValueError:
    print("Please insert an integer value\n")
print(encrypt(word,key))

