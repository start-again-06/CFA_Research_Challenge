import numpy as np


class ReinforcementTrader:
   
    def __init__(self, prices):

        self.prices = prices
        self.position = 0
        self.cash = 10000
        self.shares = 0

    def step(self, action, price):

        reward = 0

        if action == 1:  # buy

            if self.cash >= price:

                self.shares += 1
                self.cash -= price

        elif action == 2:  # sell

            if self.shares > 0:

                self.shares -= 1
                self.cash += price

        portfolio_value = self.cash + self.shares * price

        reward = portfolio_value

        return reward

    def run(self):

        rewards = []

        for price in self.prices:

            action = np.random.choice([0,1,2])  # hold/buy/sell

            reward = self.step(action, price)

            rewards.append(reward)

        return rewards
