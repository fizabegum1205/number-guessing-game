import random

class NumberGuessingGame:
    def __init__(self):
        self.secret = 0
        self.minimum = 1
        self.maximum = 50
        self.max_attempts = 10
        self.attempts = 0
        self.difficulty_level = 1
        self.guessed_correctly = False
        self.history = []

    def difficulty(self):
        print("\n===== SELECT DIFFICULTY =====")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.minimum = 1
                    self.maximum = 20
                    self.max_attempts = 10
                    self.difficulty_level = 1
                    break
                elif choice == 2:
                    self.minimum = 1
                    self.maximum = 50
                    self.max_attempts = 7
                    self.difficulty_level = 2
                    break
                elif choice == 3:
                    self.minimum = 1
                    self.maximum = 100
                    self.max_attempts = 5
                    self.difficulty_level = 3
                    break
                else:
                    print("Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input! Enter a number.")
        print("\nDifficulty selected!")
        print("Range:", self.minimum, "to", self.maximum)
        print("Maximum attempts:", self.max_attempts)

    def generate_number(self):
        self.secret = random.randint(self.minimum, self.maximum)
        self.attempts = 0
        self.guessed_correctly = False

    def play_game(self):
        print("\n===== GAME STARTED =====")
        print("Guess a number between", self.minimum, "and", self.maximum)
        print("You have", self.max_attempts, "attempts.")
        while self.attempts < self.max_attempts:
            try:
                guess = int(input("\nEnter your guess: "))
                if guess < self.minimum or guess > self.maximum:
                    print("Enter a number between", self.minimum, "and", self.maximum)
                    continue
                self.attempts += 1
                if guess == self.secret:
                    self.guessed_correctly = True
                    print("\nCorrect!")
                    print("You guessed the number in", self.attempts, "attempt(s).")
                    break
                elif guess < self.secret:
                    print("Too low!")
                    difference = self.secret - guess
                    if difference <= 5:
                        print("Hint: You are very close!")
                else:
                    print("Too high!")
                    difference = guess - self.secret
                    if difference <= 5:
                        print("Hint: You are very close!")
                print("Attempts remaining:", self.max_attempts - self.attempts)
            except ValueError:
                print("Invalid input! Enter a number.")
        if not self.guessed_correctly:
            print("\nGame Over!")
            print("The correct number was:", self.secret)

    def calculate_score(self):
        if self.difficulty_level == 1:
            base_score = 100
        elif self.difficulty_level == 2:
            base_score = 200
        elif self.difficulty_level == 3:
            base_score = 300
        else:
            return 0
        if not self.guessed_correctly:
            return 0
        if self.attempts < 1 or self.attempts > self.max_attempts:
            return 0
        score = base_score - (self.attempts - 1) * 10
        return max(score, 0)

    def save_history(self, score):
        result = {"difficulty": self.difficulty_level, "attempts": self.attempts, "score": score}
        self.history.append(result)

    def show_history(self):
        print("\n===== GAME HISTORY =====")
        if len(self.history) == 0:
            print("No games played yet.")
            return
        for i, game in enumerate(self.history, start=1):
            print("Game", i, "| Difficulty:", game["difficulty"], "| Attempts:", game["attempts"], "| Score:", game["score"])

    def show_leaderboard(self):
        print("\n===== LEADERBOARD =====")
        if len(self.history) == 0:
            print("No scores available.")
            return
        leaderboard = sorted(self.history, key=lambda x: x["score"], reverse=True)
        for i, game in enumerate(leaderboard, start=1):
            print(i, ". Score:", game["score"], "| Difficulty:", game["difficulty"], "| Attempts:", game["attempts"])

    def start(self):
        print("\n================================")
        print(" NUMBER GUESSING GAME")
        print("================================")
        while True:
            self.difficulty()
            self.generate_number()
            self.play_game()
            score = self.calculate_score()
            print("\n===== RESULT =====")
            print("Attempts:", self.attempts)
            print("Score:", score)
            self.save_history(score)
            print("\nWhat do you want to do?")
            print("1. Play Again")
            print("2. View Game History")
            print("3. View Leaderboard")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                continue
            elif choice == "2":
                self.show_history()
                break
            elif choice == "3":
                self.show_leaderboard()
                break
            elif choice == "4":
                print("\nThank you for playing!")
                break
            else:
                print("Invalid choice!")
                break

game = NumberGuessingGame()
game.start()