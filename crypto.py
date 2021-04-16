"""
Module for keys encryption in GreenHash
"""
from cryptography.fernet import Fernet
class crvar:
    """
    Use this for variables saving. Main values - crvar.key and crvar.token
    """
    pass
class crypto:
    """
    Main class for keys encryption module.
    """
    def encrypt(keys:list):
        """
        Encrypt this (Output in bytes). To convert from bytes to string use .decode()
        Use list for keys, please. Like this: crypto.encrypt([28631, 9813])
        """
        if type(keys) != list:
            raise ValueError("Invalid keys type: %s, %s required" % (type(keys), str))
        key = Fernet.generate_key()
        crvar.key = key
        f = Fernet(key)
        frst = keys[0]
        scnd = keys[1]
        token = f.encrypt(f"{frst}, {scnd}".encode())
        crvar.token = token
        return token
    def decrypt(key, token):
        """
        Decrypt this (Output in bytes). To convert from bytes to string use .decode()
        """
        dekey = Fernet(key)
        x = dekey.decrypt(token)
        return x