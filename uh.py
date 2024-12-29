# Placeholder muna kasi gusto lang may maicommit
# Anyways, ChatGPT bahala sa prompt ko tomorrow
# So, I've made the guesser. Need nalang tips and tricks
import random

# Initialize a dictionary to store counts for numbers 1 through 1000
counts = {i: 0 for i in range(1, 1001)}

# Loop to generate 1000 random integers
for _ in range(1000):
    num = random.randint(1, 1000)  # Generate a random number between 1 and 1000
    counts[num] += 1  # Increment the count for the number

# Print the counts for all numbers
for number, count in counts.items():
    print(f"Number {number}: picked {count} times")


