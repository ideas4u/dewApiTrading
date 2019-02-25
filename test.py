from hashlib import md5
sign = ""
signString = "qwertgfdsa"
bytes_signString = bytes(signString,'utf-8')
digest = md5(bytes_signString).digest()
HEX_DIGITS = "0123456789abcdef"
ret = ""
for item in range(len(bytes_signString)):
    ret = ret + HEX_DIGITS[(bytes_signString[item] >> 4 & 0x0f)]
    ret = ret + HEX_DIGITS[bytes_signString[item] & 0x0f]
sign = ret
print(sign)