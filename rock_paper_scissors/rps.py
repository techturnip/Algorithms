#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    base_plays = ['rock', 'paper', 'scissors']
    possible_plays = []

    def rec_fn(n, res=[]):
        if n == 0:
            return possible_plays.append(res)

        for play in base_plays:
            rec_fn(n-1, res+[play])

    rec_fn(n)
    return possible_plays


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
