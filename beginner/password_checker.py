#Password Checker

ok=True
have=False

while ok:
    password = input('Password: ')
    for i in password:
        if i.isupper():
            have=True
    if have:    
        if len(password)>8:
            ok=False
        else:
            print('Less than 8 characters, type it again!')
    else:
        print('An uppercase letter, please, type it again!')       
    
print('Successfully created password!')


