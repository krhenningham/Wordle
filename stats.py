class Statistics:
    '''Base class for tracking and analyzing game statistics.'''

    def __init__(self):
        '''Initialize statistics counters and distributions.'''
        self.games_won = 0
        self.games_lost = 0
        self.total_guesses_won = 0
        ''' makes sure that the guesses are between 1 and 6'''
        self.guess_distribution = {guesses: 0 for guesses in range(1, 7)}
        self.total_games_played = 0

    def add_lost_game(self):
        '''Increment the count for a lost game and total games played.'''
        self.games_lost += 1
        self.total_games_played += 1

    def add_won_game(self, num_guesses):
        '''Increment the count for a won game, update guess distribution, and total games played.'''
        self.games_won += 1
        self.total_guesses_won += num_guesses
        self.guess_distribution[num_guesses] += 1
        self.total_games_played += 1

    def get_guess_distribution(self):
        '''Return the distribution of guesses as a fraction of games won.'''
        distribution = {guesses: 0.0 for guesses in range(1, 7)}
        '''Checks if there was a game won'''
        if self.games_won > 0:
            '''Iterates through each entry in guess_distribution and adds it to the distribution'''
            for guesses, games_won in self.guess_distribution.items():
                distribution[guesses] = round(games_won / self.games_won, 5)
        return distribution

    def get_success_metrics(self):
        '''Return the success rate and average guesses to win.'''
        success_rate = self.games_won / self.total_games_played if self.total_games_played > 0.0 else 0.0
        avg_guesses = self.total_guesses_won / self.games_won if self.games_won > 0.0 else 0.0
        return success_rate, avg_guesses

    def print_stats(self):
        '''Print out the current statistics.'''
        print(f"Games Played: {self.total_games_played}")
        print(f"Games Won: {self.games_won}")
        print(f"Games Lost: {self.games_lost}")
        success_rate, avg_guesses = self.get_success_metrics()
        print(f"Success Rate: {success_rate / 100:.5%}")
        print(f"Average Guesses to Win: {avg_guesses:.2%}")
        print("Guess Distribution:")
        for guesses, fraction in self.get_guess_distribution().items():
            print(f"{guesses}: {fraction:.5%}")