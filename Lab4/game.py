import random
from logic import feedback


class Mastermind:
    DIFFICULTIES = {
        "1": {"name": "Easy", "length": 4, "max_symbol": 4, "turns": 10},
        "2": {"name": "Medium", "length": 5, "max_symbol": 6, "turns": 9},
        "3": {"name": "Hard", "length": 6, "max_symbol": 8, "turns": 8},
    }

    def __init__(self):
        self.code = []
        self.history = []
        self.turns = 0
        self.code_length = 0
        self.max_symbol = 0
        self.difficulty = None
        self.game_over = False

    def _select_difficulty(self):
        print("Choose difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        while True:
            choice = input("Select difficulty > ").strip()

            if choice.lower() == "q":
                return False

            if choice in self.DIFFICULTIES:
                config = self.DIFFICULTIES[choice]
                self.difficulty = config["name"]
                self.code_length = config["length"]
                self.max_symbol = config["max_symbol"]
                self.turns = config["turns"]
                self.code = [
                    str(random.randint(1, self.max_symbol))
                    for _ in range(self.code_length)
                ]
                return True

            print("Choose 1, 2, or 3.")

    def _show_history(self):
        print("History:")
        for i, (guess, exact, partial) in enumerate(self.history, start=1):
            print(
                f"{i}. Guess: {guess} | "
                f"Exact: {exact} | Partial: {partial}"
            )

    def run(self):
        if self.game_over:
            return

        if not self._select_difficulty():
            return

        print(
            f"{self.difficulty} — enter {self.code_length} digits "
            f"from 1 to {self.max_symbol}."
        )

        while self.turns:
            raw = input(f"{self.turns} turns left > ").strip()

            if raw.lower() == "q":
                return

            valid_symbols = f"12345678"[:self.max_symbol]

            if (
                len(raw) != self.code_length
                or any(ch not in valid_symbols for ch in raw)
            ):
                print(
                    f"Enter exactly {self.code_length} digits "
                    f"from 1 to {self.max_symbol}."
                )
                continue

            guess = list(raw)
            exact, partial = feedback(self.code, guess)

            self.history.append((raw, exact, partial))
            self.turns -= 1

            print("Exact:", exact, " Partial:", partial)
            self._show_history()

            if exact == self.code_length:
                self.game_over = True
                print("Cracked the code!")
                return

        self.game_over = True
        print("The code was", "".join(self.code))