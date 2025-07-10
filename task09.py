class user:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email 
        self.is_active = is_active
    def activite(self):
        self.is_active = True
        print(f"{self.username} faollashtrildi")
    def deactivite(self):
        self.is_active = False
        print(f"{self.username} biloklandi")
        
new_user = user("@SobirjonDev", "sobirjondev@gmail.com", True)
new_user.activite()
new_user.deactivite()
    

        