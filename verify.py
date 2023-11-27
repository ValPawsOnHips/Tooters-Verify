blockfile = "disposable_email_blocklist.conf"
blockopen = open(blockfile, 'r').read()
allowfile = "allowlist.conf"
allowopen = open(allowfile, 'r').read()

blocklist = blockopen.split(sep="\n")
allowlist = allowopen.split(sep="\n")

email = input("Put in only the domain > ")

block = False
allow = True

for em in blocklist:
    if input == em:
        block = True
        allow = False
        break

for em in allowlist:
    if input == em:
        allow = True
        break

if block == True and allow != True:
    print("TempMail")
    exit()
elif allow == True and block != True:
    print("Fine")
    exit()
elif allow == True and block == True:
    print("Error, domain in both lists")
    exit()
