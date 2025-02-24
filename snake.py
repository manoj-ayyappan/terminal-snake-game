import curses
import random

# Initialize the game window


def setup_window():
    curses.initscr()
    win = curses.newwin(20, 60, 0, 0)  # Create a 20x60 window
    win.keypad(True)
    win.timeout(200)  # Game speed
    curses.noecho()
    curses.curs_set(0)  # Hide cursor

    # Draw border
    win.border('|', '|', '-', '-', '+', '+', '+', '+')
    return win

# Main game function


def play_game():
    win = setup_window()

    snake = [(5, 10), (5, 9), (5, 8)]  # Initial snake position
    food = (10, 20)  # Initial food position
    win.addch(food[0], food[1], ord('*'))  # Food as *

    key = curses.KEY_RIGHT  # Initial direction
    score = 0

    while True:
        next_key = win.getch()
        key = key if next_key == -1 else next_key

        # Calculate new snake head position
        head = (snake[0][0] + (key == curses.KEY_DOWN) - (key == curses.KEY_UP),
                snake[0][1] + (key == curses.KEY_RIGHT) - (key == curses.KEY_LEFT))

        # Check for collisions (wall or itself)
        if head in snake or head[0] <= 0 or head[0] >= 19 or head[1] <= 0 or head[1] >= 59:
            break

        snake.insert(0, head)

        # Eat food
        if head == food:
            score += 1
            food = None
            while food is None:
                new_food = (random.randint(1, 18), random.randint(1, 58))
                food = new_food if new_food not in snake else None
            win.addch(food[0], food[1], ord('*'))  # Place new food
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], " ")

        win.addch(head[0], head[1], ord('@'))  # Draw snake head

    curses.endwin()
    print(f"Game Over! Your score: {score}")


if __name__ == "__main__":
    play_game()
