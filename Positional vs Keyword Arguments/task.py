# # Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

#Functions with multiple inputs
def greet_with(name, location):
    print(f"Hello {name}, I see you are from {location}. How do you like it?")

greet_with("Gerald", "Baltimore")

#assign values manually / different order than function default
greet_with(location="Bollywood", name="Tyson")

# ---------------------------------------
# ---------------------------------------
# ---------------------------------------

#Love Score Calculator Challenge in Udemy
def calculate_love_score(name1, name2):
    first_digit = 0
    second_digit = 0
    word1 = "true"
    word2 = "love"
    list1 = list(word1)
    list2 = list(word2)
    for letters in name1.lower():
        if letters in list1:
            first_digit += 1
    for letters in name1.lower():
        if letters in list2:
            second_digit += 1

    for letters in name2.lower():
        if letters in list1:
            first_digit += 1
    for letters in name2.lower():
        if letters in list2:
            second_digit += 1

    print(first_digit)
    print(second_digit)
    love_score = (first_digit * 10) + second_digit
    print(love_score)


calculate_love_score("Kanye West", "Kim Kardashian")