from faker import Faker
from datetime import datetime


def get_time():
    now = datetime.now()
    return now.strftime('%H:%M:%S')


def hello_from_faker():
    faker = Faker()
    name = faker.name()
    emoji = faker.emoji()
    print(f"{emoji} {name} {emoji} says now is {get_time()}")


def main():
    hello_from_faker()
