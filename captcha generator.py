import random
import string
def captcha(length=5):
    characters = string.ascii_letters + string.digits
    captcha = ""
    for _ in range(length):
        captcha += random.choice(characters)
    return captcha
c= captcha()
print(c)
