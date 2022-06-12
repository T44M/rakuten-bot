import random

##You can add hashtags in the list text##
def main():
    with open('interior_hashtag.txt', 'r', encoding="utf-8_sig") as h:
        revise = h.read().split("\n")
        tags = random.sample(revise, 6)
    
    print(tags)

main()