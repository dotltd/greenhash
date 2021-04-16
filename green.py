"""
GreenHash v1. The best hashing function only for you
"""
import hashlib
import re

class ghash:
        """
        Main class that controls the GreenHash algorithm
        """
        def greencode (password:str, key:int = 23163, key2:int = 351):
                """
                One of two ways to encode the string. Method: [allthenumbers][letters]
                """
                if(type(password) != str):
                        raise SyntaxError("Invalid DATATYPE provided. STR required.")
                encode = hashlib.sha3_256("{}".format(password).encode()).hexdigest()
                encodenum = str(int(''.join(re.findall(r'\d+', encode))) * int(key) + int(key2) ** int(re.findall(r'\d+', encode)[len(re.findall(r'\d+', encode)) - 1]))[0:16]
                encfin = str(encodenum)[1:20] + ''.join(re.findall(r'[a-z]', encode))[1:15]
                return encfin
        def redcode (password, key:int = 23163, key2:int = 351):
                """
                One of two ways to encode the string. Method: [lettersandnumbers shuffeled]
                """
                if(type(password) != str):
                        raise SyntaxError("Invalid DATATYPE provided. STR required.")
                finalarray = []
                encode = hashlib.sha3_256("{}".format(password).encode()).hexdigest()
                mln = str(int(''.join(re.findall(r'\d+', encode))) * int(key) + int(key2) ** int(re.findall(r'\d+', encode)[len(re.findall(r'\d+', encode)) - 1]))[0:16]
                for nums, letts in zip(mln, re.findall(r'[a-z]', encode)):
                        finalarray.append(letts)
                        finalarray.append(nums)
                x = ''.join(finalarray)
                return x