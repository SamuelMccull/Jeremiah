input = "Think i did an ok job"
amount = 2
output = ""

for letter in input:
     output += chr(ord(letter) + amount)

print(output)