# Simple cyphering encryption and decryption python program

# User statement
message = " "

# End Encrypted/Decrypted Result
result = " "

# User input menu selection
menuInput = " "

while menuInput != 'exit':
    print("Do you want to encrypt or decrypt the message?")
    menuInput = input(
        "Enter 'e' to Encrypt, 'd' to Decrypt, 'exit' to Exit Program: ")

    if menuInput == "e":
        message = input("\nEnter the message to encrypt: ")

        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) - 2)

        print(result)
        result = ""

    elif menuInput == "d":
        message = input("Enter the message to decrypt: ")

        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) + 2)

        print(result + '\n\n')
        result = ""

    elif menuInput != "exit":
        print("You have entered an invalid menuInput. Please try again.")
