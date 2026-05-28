import hashlib
from pathlib import Path

# Target hash
hash_input = input("Enter MD5 hash: ")

# Wordlist file
wordlist = Path(__file__).with_name("wordlist.txt")

found = False

with open(wordlist, "r", encoding="utf-8") as file:
    for word in file:
        word = word.strip()

        hashed_word = hashlib.md5(word.encode()).hexdigest()

        if hashed_word == hash_input:
            print(f"Password Found: {word}")
            found = True
            break

if not found:
    print("Password not found in wordlist.")
