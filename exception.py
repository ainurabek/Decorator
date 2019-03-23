def my_decortator(func):
    def wrapper(username=None, password=None):
        # try:
        username=input("Enter your username: ")
        if username == '':
            raise Exception ("No username defined!")
        # except ValueError: 
            # '' 
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