import random
import string
from difflib import SequenceMatcher
import matplotlib.pyplot as plt

goal = "charles darwin was always seasick"
generation = 0
similarity = 0
fitness_history = []  # List to store fitness values

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase + " "
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

default_str = get_random_string(len(goal))  # length should be same as goal
similarity = int(SequenceMatcher(None, default_str, goal).ratio()*100)
fitness_history.append(similarity)  # Add initial fitness to history
print(default_str)

while similarity < 100:
    temp_str = default_str
    letters = string.ascii_lowercase + " "
    new_letter = random.choice(letters)
    random_index = random.randint(0, len(default_str)-1)  # ensure index is within string length
    temp_str = default_str[:random_index] + new_letter + default_str[random_index+1:]
    new_sim = int(SequenceMatcher(None, temp_str, goal).ratio()*100)
    
    if new_sim >= similarity:  # accept new string only if its fitness is not lower
        default_str = temp_str
        similarity = new_sim
        generation += 1
        fitness_history.append(similarity)  # Store fitness for each generation
        print("#"+str(generation)+" "+str(similarity) + "%"+" "+default_str)

# Plotting the fitness history
plt.figure(figsize=(10, 5))
plt.plot(fitness_history, marker='o', linestyle='-', color='b')
plt.title('Fitness Progression over Generations')
plt.xlabel('Generation')
plt.ylabel('Fitness (%)')
plt.grid(True)
plt.show()
