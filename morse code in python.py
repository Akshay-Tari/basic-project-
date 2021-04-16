# this code is taken form  https://www.geeksforgeeks.org/morse-code-translator-python/

'''
variable key
cipher stores the morse translate form of the english string
decipher store the english translated form of the morse string
citext store morse code of a single character
i keep the count the space between morse characters
message store the string encoded or decoded
'''


# dictionary of morse code chart

morse_code ={'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'}


# function to encrypt the string



def encrypt(message):
    cipher =''
    for letter in message:
        if letter != ' ':
            cipher += morse_code[letter]+' '
        else:
            cipher += ' '
    return cipher


# function to decrypt the string

def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += '  '
    else:
        decipher += list(morse_code.keys())[list(morse_code.values()).index(citext)]
        citext =' '

    return decipher





def main():

    message = input("enter the string to convert in morse code ")
    result = encrypt(message.upper())
    print(result)



    message = input('enter one alphabet morse code at a time ')
    result = decrypt(message)
    print(result)

if __name__ == '__main__':
    main()