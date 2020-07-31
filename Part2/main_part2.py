from Crypto.Hash import SHA256
from time import time
from base64 import b64decode


def time_hashes(text, duration, hashmode):
    number_of_iterations = 0
    start_time = time()  # Adding a start time to get the difference.

    if hashmode == "SHA256":
        while True:
            now = time()
            elapsed_time = now - start_time

            if not elapsed_time >= duration:
                number_of_iterations += 1
                hash_object = SHA256.new(data=text)  # we're not doing anything with this object.
            else:
                break

    print('Total number of hashes in 1 second using ' + hashmode + ' is: ' + str(number_of_iterations))

    return number_of_iterations


d=  hex(int('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 2))

h = SHA256.new(data=d)

print h.hexdigest()

h.digest()

print hex(h.new())