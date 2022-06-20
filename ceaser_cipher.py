import string

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
letters = string.printable
reverse_letters = letters[::-1]
while True:
    db = ""
    cipher = ""
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    if choice == "encode":
        db = letters
        cipher = "encoded"
    elif choice == "decode":
        db = reverse_letters
        cipher = "decoded"
    else:
        print("wrong choice")
        continue

    message = input("Type your message\n")
    shift = int(input("Type the shift number: "))

    new_message = ""
    for i in message:
        index = db.index(i)
        new_index = (index + shift) % 100
        new_message += db[new_index]

    print(f"Here's the {cipher} result: {new_message}")

    status = input(
        "Type 'Yes' if you want to go again. Type anything else to quit: ")
    if status.lower() == "yes":
        continue
    else:
        break
print("--------------------------------")
print("Long live your hacker instinct!!")
print("--------------------------------")
