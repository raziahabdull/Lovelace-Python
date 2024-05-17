# def hello(name):
#     print("Hello Akirachix")
#     print(f"Hello {name}")


# def check_anagram(str1,str2):
#     sorted_str1 = str1.lower()
#     sorted_str2 = str2.lower()
#     if sorted(str1 )== sorted(str2):
#         print(" are anagrams")
#     else:
#           print("are not anagrams")

# str1 = "deal"
# str2 = "lead"
# check_anagram(str1,str2)

# def my_vowels(name,vowels):
#     count = sum(name.count(vowel)for vowel in vowels)
#     print(count)
# my_vowels("raziah","aeiouAEIOU")

# def year_of_birth(name,age):
#     year = 2024 - age
#     print(f"Hello {name}, you were born in {year}")

#     year_of_birth("Raziah",20)
#     year_of_birth(name="Raziah",age=20)
#     year_of_birth(age = 20, name="Raziah")

# def my_country(country = "Uganda"):
#     print(f "Hello AkiraChix from {country}")
# my_country(country = "Rwanda")
# my_country(country = "Kenya")
# my_country()

# def greet(*names):
#     for name in names:
#         print(f"Hello {}")
#     print(f"Hello {name}")

def create_sentence(**words):
    print(words)
    sentence = ""
    for word in words.values():
      sentence += word
      sentence += " "
    return sentence



