class pet:
    def __init__(self, name, Breed, owner):
        self.name = name
        self.breed = Breed
        self.owner = owner
        print(f"my Name is {self.name}, and my breed is {self.breed}")

class owner:
    def __init__(self, name, phonenumber, address):
        self.name = name
        self.phonenumber = phonenumber
        self.address = address

owner1 = owner("Heritage", "09074176779", "Ekiti")
dog1 = pet("Bruce", "German Shepard",owner1)
print(dog1.owner.address)
owner2 = owner("vip", "09074176779", "Ekiti")
dog2 = pet("Bruce", "German Shepard",owner2)

