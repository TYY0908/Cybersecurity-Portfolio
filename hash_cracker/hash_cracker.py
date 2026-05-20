import hashlib

# Target hash
hash_input = input("Enter MD5 hash: ")

# Wordlist file
wordlist = "/Users/tyy0908/Desktop/Cybersecurity_Portfolio/hash_cracker/wordlist.txt"

found = False

with open(wordlist, "r") as file:
    for word in file:
        word = word.strip()

        hashed_word = hashlib.md5(word.encode()).hexdigest()

        if hashed_word == hash_input:
            print(f"Password Found: {word}")
            found = True
            break

if not found:
    print("Password not found in wordlist.")