import uuid

class User():

    id = uuid.uuid4()

    user= []
   #Everything thing about the user is inside class user
    def __init__(self, name, email, password, role, user_id):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.id = user_id

    def add_user(self, User):
         return  self.user.append(User)


    def delete_user(self, User):
        """Implementing abstraction, removing the users is being done behind the scenes"""
        return self.user.remove(User)


#Admin is one form of a user, so this is polymorphism
class Admin(User):
    """Implementing Inheritance """



    def __init__(self):
        super.__init__(name = name, email= email, password= password, role='Admin', user_id =id)

    def add_admin(self, User):
        return self.user.append(User)

    def delete_user(self, User):
        return self.user.remove(User)

