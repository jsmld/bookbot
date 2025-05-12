def count_words(text):
  return len(text.split())

def count_characters(text):
  chars = {}
  for char in text:
    lowered = char.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

def sorted_character_count(chars):
  sorted_list = []
  for char in chars:
    sorted_list.append({"char": char, "num": chars[char]})

  # Using a lambda here is kinda messy but I just wanted to try
  # it because I'm so used to anonymous functions in JavaScript
  sorted_list.sort(reverse=True, key=lambda x: x["num"])

  return sorted_list