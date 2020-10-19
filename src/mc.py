from src.bandit import Agent, Bandit
import numpy as np
import pandas as pd
import pickle

BANDITS = [Bandit(mean=bandit_mean) for bandit_mean in np.arange(0.2, 2.1, 0.2)]

# Monte Carlo
list_of_epsilon = np.arange(0.01, 0.301, 0.01)
list_of_time_horizonts = np.arange(100, 1001, 10)
number_of_simulations = 100

results = pd.DataFrame()

for T in list_of_time_horizonts:

    for epsilon in list_of_epsilon:

        correct_hit = 0
        sum_won = 0

        for _ in range(0,number_of_simulations,1):

            Agent01 = Agent(list_of_bandits=BANDITS, T=T)
            Agent01.play_epsilon_greedy(no_of_steps_first=0, epsilon=epsilon)
            sum_won += Agent01.sum_won
            if Agent01.expected_to_be_highest == 9:
                correct_hit += 1

        average_won = sum_won/(number_of_simulations*T)
        hitrate_best = correct_hit/number_of_simulations*100

        result_sim = pd.DataFrame([{"T": T,
                               "epsilon": epsilon,
                               "average_won": average_won,
                               "hitrate_best": hitrate_best}])

        results = pd.concat([results, result_sim], axis=0)

with open(f"results_based_on_{number_of_simulations}_sim.p", 'wb') as pickle_file:
    pickle.dump(results, pickle_file)