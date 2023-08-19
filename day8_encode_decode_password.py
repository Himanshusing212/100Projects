alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cmnd = input("Enter the command.... 'Encrypt' to encode and 'Decrypt' to decode : ")
ss = input("Enter your  message: ")
n = int(input("Enter the number of Shift: "))

if cmnd == "Encrypt" :
    text = ""
    for letter in ss.lower():
        if letter == ' ':
            new_letter = ' '
        else: 
            pos = alph.index(letter)
            new_pos = pos + n
            if new_pos > 26:
                new_pos = new_pos - 26
            new_letter = alph[new_pos]
        text += new_letter
    print(text)
elif cmnd  == "Decrypt" :
    text = ""
    for letter in ss.lower():
        if letter == ' ':
            new_letter = ' '
        else:
            pos = alph.index(letter)
            new_pos = pos - n
            if new_pos > 26:
                new_pos = new_pos - 26
            new_letter = alph[new_pos]
        text += new_letter
    print(text)
else:
    print("Error found , check the command again!!")

