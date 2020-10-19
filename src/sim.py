from src.bandit import Bandit, Agent

########### SIMULATION #############

BANDITS = [Bandit(mean=bandit_mean) for bandit_mean in np.arange(0.2, 2.1, 0.2)]
Agent01 = Agent(list_of_bandits=BANDITS, T=1000)

Agent01.play_bandit(1)
Agent01.play_epsilon_greedy(no_of_steps_first=2, epsilon=0.01)

print(f"We expect no {Agent01.expected_to_be_highest} to be the best bandit. \n")
print("Summary: \n")
for bandit_no, bandit_expectation in enumerate(Agent01.bandit_expectations, 1):

    print(f"Bandit No {bandit_no}:")
    print(f"Expected Mean: {bandit_expectation.Expected_mean}")
    print(f"Number played: {bandit_expectation.No_explored} \n")