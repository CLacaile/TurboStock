from app.models import User
class AuthenticationBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user != None:
                if user.password == password:
                    return user
            return None
        except User.DoesNotExist:
            return None

    def has_perm(self, user, perm, obj=None):
        print("caca")

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except Exception:
            return None
