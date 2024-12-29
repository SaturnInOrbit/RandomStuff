# Placeholder muna kasi gusto lang may maicommit
# Anyways, ChatGPT bahala sa prompt ko tomorrow
# So, I've made the guesser. Need nalang tips and tricks
import random

# Initialize an empty dictionary to store counts
counts = {}

# Loop to generate 1000 random integers
for _ in range(1000):
    num = random.randint(1, 100)  # Replace 1, 100 with your desired range
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

# To check how many times a specific number was picked
specific_number = 42  # Replace with the number you want to check
count = counts.get(specific_number, 0)
print(f"The number {specific_number} was picked {count} times.")

