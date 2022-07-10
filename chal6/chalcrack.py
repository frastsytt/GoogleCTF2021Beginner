import binascii
import os
import binascii
import zlib
import gzip
import subprocess

def swapNibbles(x):
    return ( (x & 0x0F)<<4 | (x & 0xF0)>>4 )

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


unsorted_chars = []

with open("chall.txt", "r") as file:
    for line in file:
        for char in line:
            unsorted_chars.append(char)


unsorted_chars = [ord(char) for char in unsorted_chars]
sorted_set_chars = sorted(list(set(unsorted_chars)))
indexes = [sorted_set_chars.index(c) for c in unsorted_chars]

reversed_indexes = [swapNibbles(n) for n in indexes]


hexlist = [hex(n) for n in reversed_indexes]


with open("test.jpg", "wb") as file:
    file.write(bytes(reversed_indexes))


evil_code = ""

for c in (chr(n) for n in bytes(reversed_indexes)):
    if "a" <= c <= "z":
        evil_code += c
        continue
    if len(evil_code) >= 20:
        break
    evil_code = "" ## dont understand the second if/break block

dist_evil = []
for chara in evil_code:
    if chara not in dist_evil:
        dist_evil.append(chara)



evil_output = ""
accumulator = 0

for s in evil_code:
    if s == "a":
        accumulator += 1
    elif s == "e":  # Apply weaver function
        accumulator = (
            (accumulator >> 0 & 1) << 2 |
            (accumulator >> 1 & 1) << 0 |
            (accumulator >> 2 & 1) << 4 |
            (accumulator >> 3 & 1) << 1 |
            (accumulator >> 4 & 1) << 6 |
            (accumulator >> 5 & 1) << 3 |
            (accumulator >> 6 & 1) << 7 |
            (accumulator >> 7 & 1) << 5
        )
    elif s == "u":
        accumulator -= 1
    elif s == "w":
        evil_output += chr(accumulator)
    elif s == "z":
        accumulator = 0



data = binascii.unhexlify(evil_output)
print(data[:20])

print([hex(c) for c in data[:20]])

data = zlib.decompress(data)

print([hex(c) for c in data[:20]])

data = gzip.decompress(data)

print([hex(c) for c in data[:20]])



with open("testfilenoext", "wb") as file:
    file.write(data)


piet_output = subprocess.run(
    ["C:/Users/Roomet/Downloads/npiet-1.3a-win32/npiet.exe", "-e", "10000", "test.ppm"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

piet_output = piet_output.stdout.replace(b"\x01", b"").decode()