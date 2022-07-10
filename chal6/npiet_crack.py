import subprocess
import os
import binascii
import zlib
import brainfuck

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


piet_output = subprocess.run(
    ["npiet", "-e", "10000", "test.ppm"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

piet_output = piet_output.stdout.replace(b"\x01", b"").decode()


zlib_data = binascii.unhexlify(piet_output)
data = zlib.decompress(zlib_data)

print(data[:20])
data = data.decode()
data = data.split("\n")

nya_result = ""
counter = 0
for line in data:

    for char in line:
        if char == "n":
            counter -= 1
        elif char == "y":
            counter += 1
        elif char == "a":
            nya_result += chr(counter)
        elif char == "~":
            counter = 0

unary_code = bin(int(nya_result))[2:]
unary_code = unary_code[1:]

brainfuck_code = ""

for i in range(0, len(unary_code), 3):
    operation = unary_code[i:i+3]

    if operation == "000":
        brainfuck_code += ">"
    elif operation == "001":
        brainfuck_code += "<"
    elif operation == "010":
        brainfuck_code += "+"
    elif operation == "011":
        brainfuck_code += "-"
    elif operation == "100":
        brainfuck_code += "."
    elif operation == "101":
        brainfuck_code += ","
    elif operation == "110":
        brainfuck_code += "["
    elif operation == "111":
        brainfuck_code += "]"

print(brainfuck.evaluate(brainfuck_code))