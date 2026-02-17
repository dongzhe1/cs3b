

# challenge 2
def format_spells(spells, occurrence):
    return list(map(lambda s, x: ' '.join([s + "!!!"] * x), spells, occurrence))


if __name__ == "__main__":
    spells_list = ["protego", "accio", "expecto patronum", "legilimens"]
    counts_list = [1, 0, 2, 1]

    result = format_spells(spells_list, counts_list)
    print(result)
