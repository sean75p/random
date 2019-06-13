import random

class Dice(object):
    point_rolled = []

    def roll_the_die(self):
        return random.randint(1,6)

    def roll(self):
        self.die_1 = self.roll_the_die()
        self.die_2 = self.roll_the_die()
        self.total = self.die_1 + self.die_2
        return self.total

    def max_odds(self):
        if self.total in [4, 10]:
            odds_bet = 3 * self.pass_bet
            win_amount = odds_bet * 2
        if self.total in [5, 9]:
            odds_bet = 4 * self.pass_bet
            win_amount = odds_bet * 1.5
        if self.total in [6, 8]:
            odds_bet = 5 * self.pass_bet
            win_amount = odds_bet * (6/5)
        return odds_bet, win_amount

    def pass_line_bet(self):
        odds_bet = 0
        self.win_amount = 0
        self.lose_amount = 0
        craps = [ 2,3, 12]
        pass_line_winner = [7, 11]
        self.point = [4, 5, 6, 8, 9, 10]
        self.pass_bet = 10
        if self.total in craps:
            self.lose_amount = 10
            print("You lose $10")
        elif self.total in pass_line_winner:
            self.win_amount = 10
            print("You win $10")
        else:
            # if a point was rolled
            self.point_rolled = self.total
            print("The point is:", self.point_rolled)
            odds_bet, win_amount = self.max_odds()
            print("Max odds bet is:", odds_bet)
            print("Winnings could be:", win_amount)

            self.roll()
            print(self.total)
            while self.total not in [self.point_rolled, 7]:
                self.roll()
                print(self.total)

            if self.total == 7:
                self.lose_amount = self.pass_bet + odds_bet
                print("You lose:", self.lose_amount)
            if self.total == self.point_rolled:
                self.win_amount = self.pass_bet + win_amount
                print("You win:", self.win_amount)

        self.total_wagered = self.pass_bet + odds_bet


if __name__== "__main__":
    all_points_rolled = []
    total_wins = 0
    total_losses = 0
    total_wagered = 0
    number_of_plays = int(input("How many rounds of craps do you want to play? " ))
    #number_of_plays = 10000

    pass_line_winner = 0
    pass_line_craps = 0

    for i in range(number_of_plays):
        instance = Dice()
        instance.roll()
        print(instance.die_1, instance.die_2)
        print(instance.total)
        instance.pass_line_bet()
        if instance.win_amount == instance.pass_bet:
            pass_line_winner += 1
        if instance.lose_amount == instance.pass_bet:
            pass_line_craps += 1
        all_points_rolled.append(instance.point_rolled)
        total_wins = total_wins + instance.win_amount
        total_losses = total_losses + instance.lose_amount
        total_wagered = total_wagered + instance.total_wagered

    print("------------------------------------------")
    print("Number of times craps was played:", number_of_plays)
    print("total wagered based on $10 pass line bet:", total_wagered)
    print("total_wins:", total_wins)
    print("total_losses:", total_losses)
    print("Net gain:", total_wins - total_losses)
    print("Gain or Loss as a percentage of total wagered:", (total_wins - total_losses)/total_wagered)
    print(all_points_rolled)

    # remove empty lists within the list
    all_points_rolled = [x for x in all_points_rolled if x !=[]]

    print(all_points_rolled)
    print("Occurrences of 4:", all_points_rolled.count(4))
    print("Occurrences of 5:", all_points_rolled.count(5))
    print("Occurrences of 6:", all_points_rolled.count(6))
    print("Occurrences of 8:", all_points_rolled.count(8))
    print("Occurrences of 9:", all_points_rolled.count(9))
    print("Occurrences of 10:", all_points_rolled.count(10))
    print("Occurrences of pass line winner:", pass_line_winner)
    print("Occurrences of pass line craps:", pass_line_craps)

    import matplotlib.pyplot as plt
    import numpy as np

    plt.hist(all_points_rolled)
    plt.show()
