from random import normalvariate
from collections import namedtuple
import numpy as np

Bandit_Expectation = namedtuple("Bandit_Expectation", ["No_explored", "Expected_mean"])

def argmax(list):
    f = lambda i: list[i]
    return max(range(len(list)), key=f)

class Bandit():

    def __init__(self, mean):
        self.mean = mean

    def play(self):
        return normalvariate(self.mean, 1)


def explore(bandit_expectations, no_steps, explicit_bandit=None):

    """ Exploration Step
    """

    if explicit_bandit is None:

        for bandit_no, bandit in enumerate(BANDITS, 0):

            expected_mean = bandit_expectations[bandit_no].Expected_mean
            no_explored = bandit_expectations[bandit_no].No_explored

            sum = 0
            for trial in range(0, no_steps):
                sum = sum + bandit.play()

            # Update Bandit Expectation
            bandit_expectations[bandit_no] = Bandit_Expectation(
                Expected_mean = (expected_mean * no_explored + sum) / (no_explored + no_steps),
                No_explored =  no_explored + no_steps
            )

        return bandit_expectations

    else:

        expected_mean = bandit_expectations[explicit_bandit].Expected_mean
        no_explored = bandit_expectations[explicit_bandit].No_explored

        sum = 0
        for trial in range(0, no_steps):
            sum = sum + BANDITS[explicit_bandit].play()

        # Update Bandit Expectation
        bandit_expectations[explicit_bandit] = Bandit_Expectation(
            Expected_mean=(expected_mean * no_explored + sum) / (no_explored + no_steps),
            No_explored=no_explored + no_steps
        )

        return bandit_expectations




########### SIMULATION #############

BANDITS = [Bandit(mean=bandit_mean) for bandit_mean in np.arange(0, 2.1, 0.2)]
T = 1000
n_bandits = len(BANDITS)
trials_per_bandit = 2
T_rest = T - trials_per_bandit*len(BANDITS)


q = [Bandit_Expectation(0,0) for _ in BANDITS]


q = explore(bandit_expectations=q, no_steps=10)
q = explore(bandit_expectations=q, no_steps=2, explicit_bandit=1)

print(q)
final_choice = argmax([bandit_expectation.Expected_mean for bandit_expectation in q])
print(final_choice)






