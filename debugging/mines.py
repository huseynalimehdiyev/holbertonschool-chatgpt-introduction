#!/usr/bin/python3
import random
import os

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        # Randomly place mines using linear indexing
        self.mines = set(random.sample(range(width * height), mines))
        # Initialize the visible board (for display)
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        # Track which cells have been revealed
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    # Function to print the current board
    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                # If reveal=True or cell is revealed, show content
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')  # Show mine
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')  # Show count or empty
                else:
                    print('.', end=' ')  # Hidden cell
            print()

    # Count the number of mines surrounding a given cell
    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    # Reveal a cell
    def reveal(self, x, y):
        # If it's a mine, return False → game over
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        # If no adjacent mines, recursively reveal neighbors
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    # Check if player has won (all non-mine cells revealed)
    def check_win(self):
        for y in range(self.height):
            for x in range(self.width):
                if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
                    return False
        return True

    # Main game loop
    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                # Reveal the cell; if mine → game over
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                # Check if player has won
                if self.check_win():
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
