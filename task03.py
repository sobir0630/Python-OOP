class user:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email 
        self.is_active = is_active

user_info = user("@SobirjonDev", "sobirjondev@gmail.com", True)
print(f"info ->> {user_info.username}, {user_info.email}, {user_info.is_active}")
        