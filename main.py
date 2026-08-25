while True:
    print("Choose your option: \n\t1)Encrypt\n\t2)Decrypt\n\t3)Exit")
    choice = input("your choice: ")
    if choice == "1":
        plain_text = input("Text: ")
        encrypted_text = ""
        for character in plain_text:
            x = ord(character) * 2 + 5
            encrypted_text += chr(x)
        print("Encrypted_text: ", encrypted_text)
        print("*" * 40, "\n")
    elif choice == "2":
        encrypted_text = input("Encrypted_text: ")
        plain_text = ""
        for character in encrypted_text:
            x = (ord(character) - 5) // 2
            plain_text += chr(x)
        print("Plain_text: ", plain_text)
        print("*" * 40, "\n")
    elif choice == "3":
        print("Goodbye!")
        print("*" * 40, "\n")
        break
    else:
        print("Your choice is wrong!")
        print("*" * 40, "\n")