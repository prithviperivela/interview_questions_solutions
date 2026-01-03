import os
import hashlib

MASTER_FILE = "master.txt"
VAULT_FILE = "vault.txt"


def encrypt(text):
    result = ""
    for char in text:
        result += chr(ord(char) + 3)
    return result


def decrypt(text):
    result = ""
    for char in text:
        result += chr(ord(char) - 3)
    return result



def setup_master_password():
    password = input("Create master password: ")
    hashed = hashlib.sha256(password.encode()).hexdigest()

    with open(MASTER_FILE, "w") as file:
        file.write(hashed)

    print("Master password created successfully")


def verify_master_password():
    password = input("Enter master password: ")
    hashed = hashlib.sha256(password.encode()).hexdigest()

    with open(MASTER_FILE, "r") as file:
        saved_hash = file.read()

    return hashed == saved_hash



def add_credential():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    encrypted_line = (
        encrypt(website) + "|" +
        encrypt(username) + "|" +
        encrypt(password)
    )

    with open(VAULT_FILE, "a") as file:
        file.write(encrypted_line + "\n")

    print("Credential added successfully")


def view_credentials():
    if not os.path.isfile(VAULT_FILE):
        print("No credentials stored")
        return

    with open(VAULT_FILE, "r") as file:
        for line in file:
            website, username, password = line.strip().split("|")

            print("Website:", decrypt(website))
            print("Username:", decrypt(username))
            print("Password:", decrypt(password))
            print("-" * 20)


def search_credential():
    search_site = input("Enter website to search: ")

    if not os.path.isfile(VAULT_FILE):
        print("No credentials stored")
        return

    found = False

    with open(VAULT_FILE, "r") as file:
        for line in file:
            website, username, password = line.strip().split("|")

            if decrypt(website) == search_site:
                print("Website:", decrypt(website))
                print("Username:", decrypt(username))
                print("Password:", decrypt(password))
                found = True

    if not found:
        print("No credential found for this website")



def main():
    if not os.path.isfile(MASTER_FILE):
        setup_master_password()

    if not verify_master_password():
        print("Incorrect master password")
        return

    while True:
        print("\n1. Add Credential")
        print("2. View All Credentials")
        print("3. Search Credential by Website")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_credential()
        elif choice == "2":
            view_credentials()
        elif choice == "3":
            search_credential()
        elif choice == "4":
            print("Exiting password manager")
            break
        else:
            print("Invalid option")


    main()

