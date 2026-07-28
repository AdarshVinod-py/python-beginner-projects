def encrypt(text : str, key : int) -> str:
    new_word_list :list =[]
    for i in text:
        if i.isupper():
            ascii_value : int = ord(i) - ord('A')
            new_word_list.append(chr(((ascii_value + key)%26)+ord('A')))
        elif i.islower():
            ascii_value : int = ord(i) - ord('a')
            new_word_list.append(chr(((ascii_value + key)%26)+ord('a')))
        elif i.isdigit():
            ascii_value : int = ord(i) - ord('0')
            new_word_list.append(chr(((ascii_value + key)%10)+ord('0')))
        else:
            new_word_list.append(i)
    new_word: str = "".join(new_word_list)
    return new_word

while True:
    choice : str = input("1 -> Encrypt\n2 -> Decrypt:\n3 -> Exit\nEnter your choice(1/2/3):\n")
    if choice not in ('1','2','3'):
        print("invalid choice\n")
    elif choice == '3':
         break
    else:
        word : str= input("Enter word:\n")
        while True:
            try:
                key : int = int(input("Enter Key:\n"))
                break
            except ValueError:
                print("Enter an integer value\n")

        if choice == '1':
            print(encrypt(word,key))
        elif choice == '2':
            print(encrypt(word,-key))

