def isPhoneNumber(text):
    if len(text) != 12:
        return False #Not a phone Number
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # No area Code
    if text[3] != '-':
        return False # Missing dash
    for i in range (4, 7):
        if not text[i].isdecimal():
            return False # no first digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False #missing last 4 digits
    return True
print(isPhoneNumber('Hello'))

message = 'Call me 444-555-5486 tomorrow, or at 458-564-8888 to my office line'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone Number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone number.')