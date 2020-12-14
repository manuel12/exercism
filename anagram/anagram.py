def find_anagrams(word, candidates):
  anagrams = [candidate for candidate in candidates if("".join(sorted(word.lower())) == "".join(sorted(candidate.lower())) and 
  word.lower() != candidate.lower())]  
  return anagrams 