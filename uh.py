# Placeholder muna kasi gusto lang may maicommit
# Anyways, ChatGPT bahala sa prompt ko tomorrow
# So, I've made the guesser. Need nalang tips and tricks
import random
import time
counter = 0
while True:
    ran = random.randint(1,1000)
    print(ran)
    counter += 1
    time.sleep(0.001)
    if counter == 100:
        break
    else:
        continue
