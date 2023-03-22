#########If our cats were human, how old would they be?###########


def cat_to_human(cat_years):
    if cat_years < 0:
        return "please enter your cat's age."
    elif cat_years <= 18:
        human_years = cat_years / 18.0
    elif cat_years <= 24:
        human_years = 1 + (cat_years - 18) / 10.5
    else:
        human_years = 2 + (cat_years - 24) / 4.0
    return "{:.1f}".format(human_years)

print("Human Age\tCat Age")
for cat_years in range(0, 100):
    human_years = cat_to_human(cat_years)
    print("{:d}\t\t{}".format(cat_years, human_years))


    #a.can yılmaz



