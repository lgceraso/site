import random
import string
op = int(input("-> Types:\n[0] Letters\n[1] Letters + Numbers\n[2] Letters + Numbers + Symbols\n"))
carac = int(input("-> How much characters? "))
if op == 0:
    random = ''.join([random.choice(string.ascii_letters) for n in range(carac)])
elif op == 1:
    random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(carac)])
elif op == 2:
    random = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(carac)])
print(random)
