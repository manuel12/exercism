'''
Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
'''

scrabble_points = {
  'aeioulnrst': 1,
  'dg': 2,
  'bcmp': 3,
  'fhvwy': 4,
  'k': 5,
  'jx': 8,
  'qz': 10
}

def score(word):
  scrabble_score = 0
  for char in word.lower():
    for k, v in scrabble_points.items():
      if char in k:
        scrabble_score += v
  return scrabble_score
