#module to generate otps 
import random
def getotp(size=6):
    if size==6:
        return str(random.randint(10,99)) + str(random.randint(10,99)) + str(random.randint(10,99))
    elif size==4:
        return str(random.randint(10,99)) + str(random.randint(10,99))
    elif size==2:
        return str(random.randint(10,99))
    else: 
        return 0