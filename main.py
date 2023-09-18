import random

guess_word = ["adidas", "nike", "puma"]
rand_words = random.choice(guess_word)
kolicestvo_ugad = int(input("kolicestvo popitok?: "))
print(kolicestvo_ugad,r" Popitok ugadat slovo")
print("vopros: samie izvestnie mirovie brands")


while guess_word:
    ugaday_slovo = input("ugadayte bukvu ili slovo!: ")

    if ugaday_slovo in rand_words:
        print("vy ugadali")
    else:
        print("ne ugadali, sprobuyte we")
        if ugaday_slovo.find(rand_words):
            print(rand_words, r"ss")
        else:
            print("ne ugadali")
            
