import random

guess_word = ["adidas", "nike", "puma"]
rand_words = random.choice(guess_word)

kolicestvo_ugad = int(input("kolicestvo popitok?: "))

print(r"U vas", kolicestvo_ugad, "-Popitok ugadat slovo")
print(r"Vopros: Izvestnie Mirovie Brandy na", len(rand_words), "bukv?")

while rand_words:

    ugaday_slovo = input("Ugadayte bukvu ili slovo!: ")

    if ugaday_slovo in rand_words:
        print("Vy ugadali")
        break

    else:
        print("ne ugadali, sprobuyte we")
