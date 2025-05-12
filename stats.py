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
