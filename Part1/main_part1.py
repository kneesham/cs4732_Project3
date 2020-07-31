from Crypto.Hash import SHA256
from Crypto.Hash import keccak
from time import time
import math
import decimal

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
    elif hashmode == "KECCAK":
        while True:
            now = time()
            elapsed_time = now - start_time

            if not elapsed_time >= duration:
                number_of_iterations += 1
                keccak_hash = keccak.new(digest_bits=256)  # we're not doing anything with this object.
                keccak_hash.update(text)
            else:
                break

    print('Total number of hashes (for this run) in 1 second using ' + hashmode + ' is: ' + str(number_of_iterations))

    return number_of_iterations

def check_time(file_text):
    sha256_hash_count = time_hashes(file_text, 1, "SHA256")
    keccak_hash_count = time_hashes(file_text, 1, "KECCAK")

    if(len(file_text) > 256):
        average_time_sha256 = (100494 + 75875 + 89587 + 88556 + 81119 + 92177) / 6.0
        average_time_keccak = (122079 + 114912 + 100479 + 116219 + 112463 + 128695) / 6.0
        #  Averages found by running the program 5 times and manually running and pasting the outputs
    else:
        average_time_sha256 = (58143 + 61520 + 57911 + 47118 + 52947 + 54944) / 6.0
        average_time_keccak = (85794 + 87739 + 82974 + 92978 + 76957 + 81958) / 6.0
        #  Averages found by running the program 5 times and manually running and pasting the outputs

    print("average time second for sha256 = " + str(average_time_sha256))
    print("average time second for keccak = " + str(average_time_keccak))

    average_hashes_collision = pow(2, (256 / 2))
    collision_time_sha256 = average_hashes_collision / average_time_sha256
    collision_time_keccak = average_hashes_collision / average_time_keccak
    # this is the average time in seconds for both.

    time_in_years_sha256 = collision_time_sha256 * (3.1709791983765 * math.pow(10, -8.0))
    time_in_years_keccak = collision_time_keccak * (3.1709791983765 * math.pow(10, -8.0))

    print("The total time it would take to find a collision in sha256 on my computer is: "
          + str(decimal.Decimal(time_in_years_sha256)) + " years")
    print("The total time it would take to find a collision in keccak on my computer is: "
          + str(decimal.Decimal(time_in_years_keccak)) + " years")


small_file_text = open("small_file.txt", "rb").read()
large_file_text = open("large_file.txt", "rb").read()

print("\nChecking the time it would take to brute force a small file: \n")
check_time(small_file_text)
print("\nNow checking the same thing using the larger file: \n")
check_time(large_file_text)