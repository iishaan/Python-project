message = input("enter a message to endcoder or decoder")
key = eval(input("Enter a key value from 1 -26:  "))
message = message.upper()
output = ""
for letter in message:
    if letter.isupper():
        value = ord(letter) + key
        letter = chr(value)
        if not letter.isupper():
            value -= 26
            letter = chr(value)
    output += letter
print("Output message: ",output)         