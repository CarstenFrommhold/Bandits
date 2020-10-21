import abc
from random import normalvariate, random, randint, betavariate
from collections import namedtuple
from scipy.stats import beta

# Lets write a Bandit Agent Setup from Scratch

Bandit_Expectation = namedtuple("Bandit_Expectation", ["No_explored", "Expected_mean"])
Bandit_Beta_Expectation = namedtuple("Bandit_Beta_Expectation", ["Alpha", "Beta", "BetaScipy"])

def argmax(list):
    f = lambda i: list[i]
    return max(range(len(list)), key=f)

class Bandit(abc.ABC):

    def __init__(self, mean):
        self.mean = mean

    @abc.abstractmethod
    def play(self):
        pass

class NormBandit(Bandit):

    def play(self):
        return normalvariate(self.mean, 1)

class BernoulliBandit(Bandit):

    def __init__(self, mean):
        super().__init__(mean)
        if self.mean < 0 or self.mean > 1:
            raise Exception("Mean should be a probability!")

    def play(self):
        return int(random() <= self.mean)

class Agent():

    def __init__(self, list_of_bandits, T):
        self.list_of_bandits = list_of_bandits
        self.no_of_bandits = len(list_of_bandits)
        self.sum_won = 0
        self.bandit_expectations = [Bandit_Expectation(0,0) for _ in self.list_of_bandits]
        self.expected_to_be_highest = 0
        self.T = T

    def play_bandit(self, bandit_no):

        # Play once
        won = self.list_of_bandits[bandit_no].play()

        # Update wins
        self.sum_won += won

        # Update expectation of bandit
        expected_mean = self.bandit_expectations[bandit_no].Expected_mean
        no_explored = self.bandit_expectations[bandit_no].No_explored

        self.bandit_expectations[bandit_no] = Bandit_Expectation(
            Expected_mean=(expected_mean * no_explored + won) / (no_explored + 1),
            No_explored=no_explored + 1
        )

        # Update expected highest bandit
        self.expected_to_be_highest = argmax(
            [bandit_expectation.Expected_mean for bandit_expectation in self.bandit_expectations])

    def play_epsilon_greedy(self, no_of_steps_first, epsilon):
        """ Do Exploration Step first and then play random bandit with probability epsilon
        """

        # First step exploration
        for step in range(0,no_of_steps_first):

            for bandit_no in range(0, self.no_of_bandits):
                self.play_bandit(bandit_no)

        # Play Epsilon Greedy
        for _ in range(0,self.T-no_of_steps_first*self.no_of_bandits):

            # Flip a coin
            r = random()

            # Explore or exploit
            if r <= epsilon:
                self.play_bandit(randint(0, self.no_of_bandits-1))
            else:
                self.play_bandit(bandit_no=self.expected_to_be_highest)


    def play_thompson_sampling(self):

        # TODO: Generalize, this is for BernoulliDist

        self.bandit_beta_expectations = [Bandit_Beta_Expectation(1, 1, beta(a=1, b=1)) for _ in self.list_of_bandits]

        for _ in range(0, self.T):

            beta_samples = [bandit_beta_expectation.BetaScipy.pdf(x=betavariate(
                bandit_beta_expectation.Alpha, bandit_beta_expectation.Beta
            ))
                for bandit_beta_expectation in self.bandit_beta_expectations]

            # Play highest
            arm_played = argmax(beta_samples)
            arm_alpha = self.bandit_beta_expectations[arm_played].Alpha
            arm_beta = self.bandit_beta_expectations[arm_played].Beta
            if self.list_of_bandits[arm_played].play() > 0:
                arm_alpha +=1
            else:
                arm_beta +=1
            # Update
            self.bandit_beta_expectations[arm_played] = Bandit_Beta_Expectation(arm_alpha,
                                                                                arm_beta,
                                                                                beta(a=arm_alpha, b=arm_beta))

        # Print Expectations:
        for no, bandit_beta_expectation in enumerate(self.bandit_beta_expectations):
            print(no)
            print(bandit_beta_expectation.Alpha)
            print(bandit_beta_expectation.Beta)