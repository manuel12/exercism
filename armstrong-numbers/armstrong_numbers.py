def is_armstrong_number(number):
  num_as_list = list(str(number))
  num_digits = len(num_as_list)
  amrstrong_num = 0
  for num in num_as_list:
    amrstrong_num += (int(num)**num_digits)
  return number == amrstrong_num
