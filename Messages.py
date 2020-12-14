import random
import os


def get_msg_from_file(folder):
    files = next(os.walk(folder))[2]
    rnd = random.randint(0, (len(files) - 1))
    with open(os.path.join(folder, files[rnd])) as msg:
        return msg.read().rstrip('\n')
