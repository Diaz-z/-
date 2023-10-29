import hashlib


def md5(n):
    hash_object = hashlib.md5(n.encode('utf-8'))
    return hash_object.hexdigest()
