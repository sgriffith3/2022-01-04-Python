pets = ["fluffy the cat", "spot the dog", "leonard the llama"]

with open("mypets.txt", "w") as petfile:
    # not done yet
    pass
    print("My Cute Pets!", file=petfile)
    intro = "Here is a list of my pets"
    petfile.write(intro)
    petfile.writelines(pets)
    for pet in pets:
        petfile.write(f"\n{pet}")
