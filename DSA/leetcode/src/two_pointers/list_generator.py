from random import Random


def list_generator(length=10):
    rand = Random()
    return [rand.randint(-10, 10) for _ in range(length)]
