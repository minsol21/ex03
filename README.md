# EvoRobotics Group Assignment

## Team Members
- **Minsol Kim**
- **Yu Zeyuan**

## Project Files and Directory Structure

- `EvoRob03.py`: Contains the main genetic algorithm.
- `plots/`: Directory containing all the generated plots.
  - `fitness_distribution.png`: Plot of the fitness progression over generations.

## Tasks Completed

- **Algorithm Implementation**: Developed the Python script to perform genetic string evolution using a genetic algorithm.
- **Fitness Evaluation**: Implemented fitness evaluation using the `SequenceMatcher` from Python's `difflib` module.
- **Plot Generation**: Generated plots showing the distribution of generations needed to achieve the target string.
- **Results Documentation**: Captured and documented the output of typical runs, showing each generation's number and its respective string.
- **Mathematical Estimation**: Provided a mathematical estimation of the expected number of generations required to match the target string.
- **Empirical Simulation**: Conducted multiple simulations to empirically determine the average number of generations needed, comparing it to the mathematical estimation.

## Answer to "Good-Natured" Optimization Problem
This problem is described as "good-natured" because it involves optimizing a playful scenario using a model that mimics natural evolutionary processes. The "fitness landscape" in this context is relatively straightforward and benign, focused solely on increasing alignment with a fixed target string through slight, random changes. This contrasts with more competitive or survival-based applications of genetic algorithms in complex, multi-variable optimization landscapes.

## Mathematical Estimation and Empirical Comparison
**Estimation**:
Given a target string of 30 characters and a character set of 27 (26 letters + space), the probability of any single character mutating correctly is 1/27. Assuming independence, the expected number of mutations for one correct character can be approximated as 27 mutations. For the string to entirely match, it would naively be expected to take about 27*30 = 810 mutations in a purely random process without selection mechanisms.

#### Empirical Data
Our empirical finding that it takes around 23,000 generations on average suggests that the mutation and selection process is less efficient than our model might hope. This could be due to:
- High dependence on initial random strings.
- A low mutation rate or low retention rate of beneficial mutations.
- The possibility that many mutations are neutral or detrimental, which doesn't change the string much from generation to generation.

From our simulations, the average number of generations needed to reach the goal string across 10 trials was approximately 23000. This discrepancy from the naive mathematical estimation highlights the efficiency gained from the selective pressure in the genetic algorithm, which progressively builds upon closer approximations to the target.

It sounds like there's a need to revisit and refine the mathematical estimation of the expected number of generations needed for the genetic algorithm to evolve the target string. Let's take a closer look at how to properly estimate this for a more accurate alignment with your empirical findings.

### Rethinking the Estimation

The original naive estimation didn't accurately account for the nuances of genetic algorithms, such as the selective pressure and incremental improvements over generations. Genetic algorithms typically don't change every character randomly in each generation; instead, they build on incremental improvements, which significantly affects the number of generations needed.

#### Estimating Genetic Algorithm Efficiency
1. **Mutation Rate and Effectiveness**: Unlike the initial assumption that each character might randomly match the goal string (1/27 chance), the algorithm uses mutations more effectively. Each mutation has the potential to be retained if it improves or maintains the fitness level, rather than being a completely random guess.

2. **Selective Retention**: The key to fewer generations than the naive model is the selective retention of beneficial mutations. In each generation, the mutation of just one character at a random position—if beneficial—is retained. This significantly increases the likelihood that each generation will yield a closer match to the target string than a purely random approach would suggest.

3. **Cumulative Improvements**: Over multiple generations, these small improvements accumulate, leading to a rapid approach toward the goal string, especially as the string becomes closer to the target.

#### Correcting the Mathematical Model
To more accurately estimate the expected number of generations, consider that each character’s correct mutation is kept when beneficial, and each generation can potentially correct multiple characters as the string approaches the goal. This reduces the naive estimation significantly:

- If we assume that each beneficial mutation has a chance of \(1/27\) of occurring and being retained, and the likelihood of each position mutating correctly increases as fewer positions are incorrect, the expected time to find the correct character decreases as the algorithm progresses.


### Revised Mathematical Estimation
A more detailed model would incorporate probabilities for each type of mutation and their impact, but generally, it would suggest:
- **Number of Generations**: The number of beneficial mutations needed to approach a nearly correct string, factoring in that each generation does not guarantee an improvement.

Given this complexity and the results from your simulations, it is clear that simple probability estimations may not suffice, and detailed simulation or a more complex stochastic model might be necessary to predict the number of generations more accurately.

### Conclusion
Revisiting our simulation setup or considering different strategies in mutation and selection might help in understanding the disparity in the expected versus observed number of generations. Adjusting parameters like mutation rates or implementing strategies like crossover might also alter the dynamics and efficiency of our evolutionary algorithm.
