#! python3
import re, pyperclip
# TODO: Create a regex for phone numbers
phoneRegex = re.compile(r''' 
# 415-555-000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(\d\d\d)|(\d\d\d)? # area code (optional)
(\s|-) # first separator
\d\d\d # first 3 digits
- # separator
\d\d\d\d #last 4 digits
(((ext(\.)?\s)|x)# extension word-part(optional)
 (\d{2,5}))?# extension number part
''', re.VERBOSE)

# TODO: Create a regex for email addresses
emailRegex = re.compile(r''' 
#some.+_thing@something.com

[a-zA-Z0-9_.+]+ # namepart
@ # @ symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)

# TODO: Get the text off the clipboard
text = ''' Jessie Mckay jmckay67@aol.com 479-205-4874
Tom Jordan tjordan@msn.com 678-560-3485
Clayton Cross ccross20@gmail.com 724-900-2986
Rayford Sutton rayfords66@hotmail.com 242-391-3183
Jerome Gentry jgentry@me.com 604-720-6426
Weldon Camacho wcamacho57@icloud.com 651-807-8065
Quinton Franks qfranks@comcast.net 209-754-9111
Adam Hubbard cygzfjd61@outlook.com 641-433-6698
Jarred Fox jfox39@live.com 701-528-9851
Arnoldo Parker aparker39@sbcglobal.net 304-491-9583
Sid Mcdaniel mcdanie3354@att.net 863-583-8107
Raymon Combs uqcwsntti71@att.net 507-948-3980
Ervin Francis efrancis@optonline.net 546-367-3454
Gilberto Austin austi363@optonline.net 321-854-5616
Lino Barlow lbarlow22@me.com 904-896-2920
Stacey Shepherd sshepherd61@sbcglobal.net 309-387-1990
Roscoe Terry rterry64@outlook.com 605-373-2329
Eddie Meadows eddiem89@yahoo.com 573-454-1209
Carlos Simpson csimpson8@verizon.net 252-822-2439
Jerome Manning jmanning54@optonline.net 586-481-1805
Hong Erickson herickson3@me.com 615-716-5379
Burt Graham bgraham70@sbcglobal.net 903-995-3368
Mario Sloan msloan55@verizon.net 205-868-3935
Jeffry Mcintosh jmcintosh@icloud.com 881-376-21'''
# TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedPhone)
print(extractedEmail)

# TODO: Copy extracted email/phone to the clipboard
