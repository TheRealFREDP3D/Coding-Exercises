# The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry.
# The hat decides which of the four "Houses" each first-year student goes to.

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

q_1 = int(input("Do you like Dawn or Dusk?\n\t1) Dawn\n\t2) Dusk\n"))
if q_1 == 1:
    gryffindor += 1
elif q_1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")

q_2 = int(
    input(
        "\nWhen I'm dead, I want people to remember me as:\n\t1) The Good\n\t2) The Great\n\t3) The Wise\n\t4) The Bold\n"
    )
)
if q_2 == 1:
    hufflepuff += 2
elif q_2 == 2:
    slytherin += 2
elif q_2 == 3:
    ravenclaw += 2
elif q_2 == 4:
    gryffindor += 2
else:
    print("Wrong input.")

q_3 = int(
    input(
        "\nWhich kind of instrument most please your ear?\n\t1) The violin\n\t2) The trumpet\n\t3) The piano\n\t4) The drum\n\n"
    )
)
if q_3 == 1:
    slytherin += 4
elif q_3 == 2:
    hufflepuff += 4
elif q_3 == 3:
    ravenclaw += 4
elif q_3 == 4:
    gryffindor += 4
else:
    print("Wrong input")

winning_house = max(gryffindor, ravenclaw, hufflepuff, slytherin)

if winning_house == gryffindor:
    print("\nGryffindor!")
elif winning_house == ravenclaw:
    print("\nRavenclaw!")
elif winning_house == hufflepuff:
    print("\nHufflepuff!")
else:
    print("\nSlytherin!")
print("Go meet your companions.")
