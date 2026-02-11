class UserService:
    def register_user(self, email, password):
        if "@" not in email:
            return None
        if len(password) < 8:
            return None

        user = {
            "email": email,
            "password": password
        }

        return user
