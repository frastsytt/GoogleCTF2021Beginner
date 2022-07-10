import random
import os
from mt19937predictor import MT19937Predictor

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


predictor = MT19937Predictor()


mersenne_list = []

file1 = open('robo_numbers_list.txt', 'r')
for line in file1:
    mersenne_list.append(int(line.replace("-", "")) - (1 << 31))


for num in mersenne_list:
    predictor.setrandbits(num, 32)

with open("secret.enc", "rb") as file:
    secret = list(file.read())

flag = ""


def decodeSecret(s):
    key = [predictor.getrandbits(8) for i in range(len(s))] ## array of numbers thats length is equal to the amount of chars in input
    return ([a^b for a,b in zip(key,s)])

for el in decodeSecret(secret):
    flag += chr(el)

print(flag)