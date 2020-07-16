alphabet = 'abcdefghijklmnopqrstuwxyz'
key = 4

newmsg = ''
message = input('enter the message ')

for char in message:
    position = alphabet.find(char)
    newposition = (position + key)%26
    newchar = alphabet[newposition]
    print('encrpted new char',newchar)
    newmsg+=newchar
print('the final message',newmsg)
