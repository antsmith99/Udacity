#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    score = 0

    def __init__(self):
        self.my_moves = []
        self.their_moves = []

    def add_to_score(self):
        self.score += 1

    def learn(self, my_move, their_move):
        self.my_moves.append(my_move)
        self.their_moves.append(their_move)


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):

    def move(self):
        if self.their_moves == []:
            return random.choice(moves)
        else:
            return self.their_moves[-1]


class CyclePlayer(Player):

    def move(self):
        if self.my_moves == []:
            return random.choice(moves)
        elif self.my_moves[-1] == "rock":
            return moves[1]
        elif self.my_moves[-1] == "paper":
            return moves[2]
        else:
            return moves[0]


class HumanPlayer(Player):

    def move(self):
        choice = ""
        while choice == "":
            string = input("Please enter your move(rock, paper, or scissors):")
            string = string.lower()
            if string in moves:
                choice = string
                return choice
            else:
                print("Please try again")


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print("Player 1: " + move1 + "  Player 2: " + move2)
        if beats(move1, move2) and move1 != move2:
            self.p1.add_to_score()
        elif beats(move1, move2) is False and move1 != move2:
            self.p2.add_to_score()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print("Round " + str(round) + ":")
            self.play_round()
        print("Game over! " + "Player 1 won: " + str(self.p1.score) +
              " round(s) Player 2 won: " + str(self.p2.score) +
              " round(s)")
        if self.p1.score > self.p2.score:
            print(f"Player 1 wins {self.p1.score} round(s) to {self.p2.score}")
        elif self.p2.score > self.p1.score:
            print(f"Player 2 wins {self.p2.score} round(s)to {self.p1.score}")
        else:
            print(f"Tie Game {self.p1.score} round(s) to {self.p2.score}.")
        # print(f"Their last move: {self.p1.their_moves[-1]}")


if __name__ == '__main__':
    game = Game(RandomPlayer(), CyclePlayer())
    game.play_game()
