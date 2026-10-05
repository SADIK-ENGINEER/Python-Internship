# WAP to find word1 word2 is anagram or not

word1 = input("Enter the word1 : ")
word2 = input("Enter the word1 : ")

if sorted(word1) == sorted(word2):
  print("word is angram")
else:
  print("word is not anagram")

  print("___________________________________________________________")