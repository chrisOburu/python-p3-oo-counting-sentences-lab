# #!/usr/bin/env python3

# class MyString:
#   def __init__(self,value=""):
#     if type(value) == str:
#       self.value = value
#     else:
#       print("The value must be a string.")
  
#   def is_sentence(self,value):
#     return value.endswith(".")
  
#   def is_question(self,value):
#     return value.endswith("?")
  
#   def is_exclamation(self,value):
#     return value.endswith("!")
  
#   def count_sentences(self,value):
#     return len(value.split("."))
  
#   def count_words(self,value):
#     return len(value.split(" "))
  
#   def count_characters(self,value):
#     return len(value)

class MyString:
  def __init__(self, value=''):
      if isinstance(value, str):
          self.value = value
      else:
          raise ValueError("The value must be a string.")

  def is_sentence(self):
      return self.value.endswith('.')

  def is_question(self):
      return self.value.endswith('?')

  def is_exclamation(self):
      return self.value.endswith('!')

  def count_sentences(self):
      # Splitting the value by periods, exclamation marks, and question marks to count sentences.
      import re
      # Pattern to split the string by sentence-ending punctuation
      pattern = r'[.!?]+'
      sentences = re.split(pattern, self.value)
      # Filter out empty strings from the resulting list
      sentences = [s for s in sentences if s.strip()]
      return len(sentences)

# Example usage:
my_string = MyString("Hello! How are you? I am fine. Thanks for asking.")
print(my_string.is_sentence())  # False
print(my_string.is_question())  # False
print(my_string.is_exclamation())  # False
print(my_string.count_sentences())  # 4

