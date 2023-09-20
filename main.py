import random
import re
words = ["adidas", "nike", "puma"]
select_word = random.choice(words)
attempts = int(input("Number of attempts?: "))
quest = "Top Sport Brands"
print("You have:", attempts, "try to guess")
print("question:", quest, len(select_word), "letters")
sample = " "
count = 0
while True:
    if count == attempts:
        print("Ty proigral")
        break

    elements = input("enter letter or word:")
    if len(elements) == 1:
        if elements in select_word:
            sample += elements
            pattern = f"[^{sample.strip()}]"
            print(re.sub(pattern, "*", select_word))
            continue

        else:
            print("invalid laetter")
            count += 1
            continue

    else:
        if elements == select_word:
            print("you won")
            break

        else:
            print("invalid word")
            count += 1
