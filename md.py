from hashlib import md5

def MD5Digest(text):
    digest = md5(text).digest()
    print("Origin string:",text)
    print("byte arryay:",*text)
    print("md5 result:",*digest)
    return digest

if __name__ == "__main__":
    MD5Digest(b"hello world")

