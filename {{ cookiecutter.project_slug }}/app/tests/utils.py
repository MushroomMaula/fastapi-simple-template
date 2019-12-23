from faker import Faker
from faker.providers import python, internet


fake = Faker()
fake.add_provider(python)
fake.add_provider(internet)


def random_string():
    return fake.pystr()
