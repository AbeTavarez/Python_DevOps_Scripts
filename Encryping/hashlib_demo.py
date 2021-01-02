import hashlib

secret_message = 'Is is a super secret message'

bsecret_message = secret_message.encode()

m = hashlib.md5()

m.update(bsecret_message)

m.digest()
