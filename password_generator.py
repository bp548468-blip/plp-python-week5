import random
import string

def make_password(length=8):
    character=string.ascii_letters + string.digits
    password=""
    for i in range(length):
        password += random.choice(character)
    return password

p1 = make_password()
p2 = make_password(12)

print("password:", p1)
print("length:", len(p1))
print("password:", p2)
print("length:",len(p2))
