import hashlib

password = "admin"
print(hashlib.md5(password.encode()).hexdigest())