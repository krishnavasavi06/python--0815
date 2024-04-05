def vowel_count(string):
    vowels='aeiouAEIOU'
    count=0
    for char in string:
        if char in vowels:
            count+=1
    return count
string=input("enter the string:")
count=vowel_count(string)
print("Number of vowels in string:",count)