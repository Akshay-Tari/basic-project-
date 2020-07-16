def isphonenumber(text)
    if len(text)!=12:
        return False
    for i in range(0,3):
        if not text[i].isdecmial();
            return False
    if text[3]!='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
print('145-521-5485 is phone number ')
print(isphonenumber('654-654-5464'))
print('moshi moshi is a phone number ')
print(isphonenumber('Moshi moshi'))
