from models import User
class AuthenticationBackend:
    def authenticate(self, request, username=None, password=None):
            user = User.objects.get(email=username)
            if user != None:
                if user.password == password:  # check valid password
                    return user  # return user to be authenticated
            return None

    def has_perm(self, user, perm, obj=None):
        print("caca")
