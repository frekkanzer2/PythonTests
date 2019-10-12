from ClassesModules.Singleton import Singleton


class User:
    def __init__(self, name):
        self.name = name
        self.banned = False


class Administrator:
    def __init__(self, name):
        self.name = name
        self.banned = 0
        self.restored = 0

    def ban(self, usr: User):
        usr.banned = True
        self.banned += 1

    def unban(self, usr: User):
        usr.banned = False
        self.restored += 1


admin = Singleton(Administrator, "Abby")
admin2 = Singleton(Administrator, "Mark")
print("Admin real name: ", admin2.__getattr__("name"))
print("Mark cannot be created")
firstUser = User("Davide")
secondUser = User("Luigi")
thirdUser = User("Alessandro")
admin.ban(firstUser)
admin2.ban(secondUser)
admin2.ban(thirdUser)
admin.unban(secondUser)
print("Number of bans: ", admin.__getattr__("banned"))
print("Number of unbans: ", admin.__getattr__("restored"))
