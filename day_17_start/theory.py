class User:
    def __init__(self, username, id):
        print(f"{username} is being created...")
        print(f"{username} launched")
        self.username = username
        self.id = id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("cemodan", "01")
user_2 = User("cantinflas", "02")

user_1.follow(user_2)
print(user_2.followers)