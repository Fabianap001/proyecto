from werkzeug.security import check_password_hash,generate_password_hash

class User():

    def __init__(self, id, inputUsername, inputPassword, fullname="") -> None: 
        self.id=id
        self.inputUsername = inputUsername
        self.inputPassword = inputPassword
        self.fullname = fullname
        
    def check_password(self,hashed_inputPassword,inputPassword):
        return check_password_hash(hashed_inputPassword,inputPassword)
    
    print(generate_password_hash("avianka"))



