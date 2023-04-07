from brain_games.games.logic import greet, congrats
from brain_games.games.brain_even import even_game

def main():
    name = greet()
    i = 0
    even_game(name)
    congrats(name, i)

if __name__ == '__main__':
    main()