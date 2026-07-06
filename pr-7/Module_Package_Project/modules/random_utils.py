import random
import string


def generate_random_number(start, end):
    num = random.randint(start, end)
    print(f"Random Number: {num}")


def generate_random_list(count, start, end):
    lst = [random.randint(start, end) for _ in range(count)]
    print(f"Random List: {lst}")


def create_random_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    print(f"Generated Password: {password}")


def generate_otp(digits=6):
    otp = "".join([str(random.randint(0, 9)) for _ in range(digits)])
    print(f"Generated OTP: {otp}")


def random_sampling(dataset, k):
    sample = random.sample(dataset, k)
    print(f"Random Sample: {sample}")
