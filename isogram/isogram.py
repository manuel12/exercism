def is_isogram(string):
  alpha_lowered_str = [char for char in string.lower() if char.isalpha()]
  alpha_lowered_set = {char for char in string.lower() if char.isalpha()}
  return len(alpha_lowered_str) == len(alpha_lowered_set)

