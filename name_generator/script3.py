import random

vowels='aeiouy'
consonants='bcdfghjklmnpqrstvwxz'
letters=vowels+consonants

letter_input_1=input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
letter_input_2=input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
letter_input_3=input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")

def plot():
    if letter_input_1 == 'v':
        l1=random.choice(vowels)
    elif letter_input_1 == 'c':
        l1=random.choice(consonants)
    elif letter_input_1=='l':
        
        