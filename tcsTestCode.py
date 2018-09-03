def removeVowels(word):
    vowels='aeiou'
    Vowels='AEIOU'
    newWord=''

    for letter in word:
        if letter in vowels or letter in Vowels:
            cap=letter.replace(letter,'$')
        else:
            cap=letter
            
        newWord+=cap
    return newWord
def removeConsonant(word):
    consonant='bcdfghjklmnpqrstvwxyz'
    Consonant='BCDFGHJKLMNPQRSTVWXYZ'
    newWord=''
    for letter in word :
        if letter in consonant or letter in Consonant :
            con=letter.replace(letter,'#')
        else:
            con=letter
        newWord+=con
    return newWord
def Uppercase(word):
    string=word
    s=string.upper()
    return s
        

first=input('Enter first word: ')
Sec=input('Enter 2nd Word: ')
third=input('Enter 3rd word: ')

firstWord= removeVowels(first)
SecWord= removeConsonant(Sec)
ThirdWord=Uppercase(third)
print(firstWord+SecWord+ThirdWord)






