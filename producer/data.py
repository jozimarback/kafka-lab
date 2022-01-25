from faker import Faker

def get_registered_user():
    fake = Faker()
    return {
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year()
    }