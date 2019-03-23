def my_decortator(func):
    def wrapper(username=None, password=None):
      
        username=input("Enter your username: ")
        if username == '':
            raise Exception ("No username defined!")
        
            
        else:
            # if username=='username':
        # pass
        # try:
            password=input("Enter new password: ")
            if password == '':
                raise Exception ("No password to change!")
        # except ValueError: 
            # '' 
        func(username)
    return wrapper


@my_decortator
def user(username=None):
    
    print(user())
    return username
        
user()

@my_decortator
def pswd(password=None):

    print(pswd())
    return password

pswd()