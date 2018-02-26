import os
import random

#Run this in an infinite loop
while True:
    num_seconds_between_requests = random.randint(1,100)
    num_concurrent_requests = random.randint(1,100)

    # Use siege to test concurrent requests
    os.system("siege -d" + str(num_seconds_between_requests) + " -c" + str(num_concurrent_requests) + " nginx")
