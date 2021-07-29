data = {}
def newuser():
    name = input("\n\tEnter Name :")
    username = input("\n\tEnter Username :")
    if username in data:
        print("\n\tThis username is alredy found")
        return -1;
    password = input("\n\tEnter Password :")

    data[username]=password
def check_user(username,password):
    '''
    this function is check user if user is currect then
    return true
    otherwise false
    '''
    if(data[username] == password):
        return True
    else:
        return False
def olduser():

    username = input("\n\tUsername :")
    password = input("\n\tPassword :")

    if(username in data and data[username]==password):
        print("\n\tLogin Successfuly!!!!")
    else:
        print("\n\tLogin failed :(")

def changepassword():

    username = input("\n\tUsername :")
    password = input("\n\tPassword :")

    if(check_user(username,password) == True):
        print("\n\tinfo is currect")      
    
        username = input("\n\tEnter Username :")
        if(username in data):
            password = input("\n\tEnter New password :")
            if(data[username] == password):
                print("\n\tthis is old password")
                return False
            else:
                data[username]=password
                print("\n\t=============password is update=============")
                return True
        else:
            print("\n\tthis username is not found")
    else:
        print("\n\tdetail incurrect")

def showdata():
    print("\n\n\t",data)

  
            
print("\n\t1.Login :")
print("\n\t2.signup :")
print("\n\t3.change password :")
print("\n\t4.show data")

ch = input("\n\tEnter Your Choice :")

while True:
    if(ch == '1'):
        olduser()
        ch = input("\n\tEnter Your Choice :")
    elif(ch == '2'):
        newuser()
        ch = input("\n\tEnter Your Choice :")
    elif(ch == '3'):
        changepassword()
        ch = input("\n\tEnter Your Choice :")
    elif(ch == '4'):
        showdata()
        ch = input("\n\tEnter Your Choice :")
