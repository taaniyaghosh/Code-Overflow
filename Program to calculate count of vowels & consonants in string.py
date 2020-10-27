"""
    Python Program to Count Vowels and Consonants in a String
"""

str1 = input("Enter String : ")
vowels = consonants =  0
vowel_list = list('aeiouAEIOU')
for i in str1:
    if i in vowel_list:
        vowels +=  1
    else:
        consonants += 1
 
print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)
