#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 5 12:15:43 2018

@author: Aslan
"""
#####QUESTION 3 = Casino Owner!####

from enum import Enum
import numpy as np
import StatisticalClasses as Stat
import FigureSupport as Fig

class CoinGame(Enum):  # set up the game w a class
    TAILS = 0
    HEADS = 1

# old stuff below...#
class Game:  # the initial game has a number of common factors
    def __init__(self):
        self._rnd = np.random  # we want random #'s to get expected values.
        self._headProb = head_prob  # prob of heads, from HW5??
        self._CoinGame = []  # this is the actual game/ flip a coin
        self._superresult = []  # outcomes will be recorded here

    def simulate(self, tosses):
        t = 0  # toss start @ zero
        while t < tosses:
            if self._rnd.sample() < self._headProb:  # head odds
                self._CoinGame = CoinGame.HEADS
            else:
                self._CoinGame = CoinGame.TAILS  # it's a binary game!
            self._superresult.append(self._CoinGame.name)
            t += 1  # new tosses add 1

    ####For HW6... broke my counts into Exp-val and losses so i can get clearer 95% CI's###
    def tallyofexpected(self):
        countable = " ".join(map(str, self._superresult))
        wins = countable.count(TTH)  # TTH is the winning sequence
        total = -initialbuyin + (wins * reward)  # how we calculate EV
        return total

    def tallyoflosses(self):
        if self.tallyofexpected() < 0:
            loss = 1
        else:
            loss = 0
        return loss


numbertosses = 20
head_prob = 0.5
initialbuyin = 250
reward = 100
TTH = "TAILS TAILS HEADS"


class theserounds:
    def __init__(self, rounds):
        self.superrounds = rounds
        # notice how I break it down into games/ losses here...
        self.games = []
        self.losses = []
        # separate the losses/ expected so we can get clear EV's/loss probs and their CI's
        self.total_tallyofexpected = []
        self.total_tallyoflosses = []

        for i in range(rounds):
            game = Game()
            self.games.append(game)
            self.losses.append(game)

    def playagame(self):
        for game in self.games:
            game.simulate(numbertosses)  # initiate cointoss
            outcome = game.tallyofexpected()
            outcomeloss = game.tallyoflosses()
            self.total_tallyofexpected.append(outcome)
            self.total_tallyoflosses.append(outcomeloss)

    def get_total_tallyofexpected(self):  # all the values from each round listed here
        return self.total_tallyofexpected
    def get_total_tallyoflosses(self):
        return self.total_tallyoflosses

    # new stuff for EV's here....
    def get_avg_expected(self):  # averages the outcomes, notice this was changed to sum stat
        # b/c we use the package instead of len/ numberofrounds like last week
        self.summary_stats1 = Stat.SummaryStat("Expected Value", self.get_total_tallyofexpected())
        return self.summary_stats1.get_mean()
    def get_avg_tallyoflosses(self):  # returns the average value
        self.summary_stats2 = Stat.SummaryStat("Loss", self.get_total_tallyoflosses())
        return self.summary_stats2.get_mean()

    # the CI's can be found here...
    def get_expectedvalueCI(self, alpha):
        return self.summary_stats1.get_t_CI(alpha)
    def get_expectedlossCI(self, alpha):
        return self.summary_stats2.get_t_CI(alpha)


####New Stuff for HW6#####
alpha = 0.05
numberofrounds = 43000
these_rounds = theserounds(numberofrounds)  # Create rounds
these_rounds.playagame()  # Play rounds

print("The expected value mean in USD$ is...", these_rounds.get_avg_expected())
print("95% CI range of the expected value in USD$ is...", these_rounds.get_expectedvalueCI(alpha))
print("The loss probability mean is...", these_rounds.get_avg_tallyoflosses())
print("95% CI range of the loss probability is...", these_rounds.get_expectedlossCI(alpha))
print("\n")
print("Example from Spyder for Casino dude: EV = -22.2, 95% CI of EV: [-28.105381663979308, -16.29461833602069]. "
      "\n"
      "LP = 0.608, 95% CI of LP = [0.57768994957140107, 0.6383100504285989]")
print("Interpretation for EV: The 95% CI of the expected value means that 95% of the CI's will encompass the true mean (about -22)- though we're not entirely sure what that is!")
print("43,000 is a large # and this rule would ideally be better if seen over a very very large # of repeated trials. Even so, a large # gives us a tighter CI and an EV closer to the true mean, which improves the predictive value of this model.")
print("Interpretation for LP: The 95% CI of the loss prob means that 95% of the CI's will encompass the true mean (about 0.60)- though we're not entirely sure what that is!")
print("43,000 is a large # and this rule would ideally be better if seen over a very very large # of repeated trials. Even so, a large # gives us a tighter CI and an EV closer to the true mean, which improves the predictive value of this model.")
