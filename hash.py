from green import ghash
from tabulate import tabulate
password = str(input('Enter hashed password [Default Format: string]: '))
x = ghash.greencode(password)
y = ghash.redcode(password)
data = [["GreenCode", f"{password}",f"{x}"], ["RedCode", f"{password}", f"{y}"]]
print(tabulate(data, headers=["Format", "Decoded String", "Encoded String"], tablefmt="psql"))