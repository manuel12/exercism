def abbreviate(words):
  alpha_chars = [char if char.isalpha() or char == "'"  else " " for char in words]   
  alpha_str = "".join(alpha_chars) 
  splitted_str = alpha_str.split(" ")
  abbreviation_letters = [word[0].upper() for word in splitted_str if word != '']
  return "".join(abbreviation_letters)
