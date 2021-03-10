##Create a function that takes a string as a parameter and returns a list.

##The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.


def anti_vowel(text):
        for i in "aeiouAEIOU":
            text = text.replace(i,"")
        return sorted(text)

print(anti_vowel('Lubie ziemniaki'))