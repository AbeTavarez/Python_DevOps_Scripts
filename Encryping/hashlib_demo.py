import hashlib

secret_message = 'Is is a super secret message'

bsecret_message = secret_message.encode()

# Creates Hashed Object
m = hashlib.md5()


m.update(bsecret_message)


print(m.digest())
