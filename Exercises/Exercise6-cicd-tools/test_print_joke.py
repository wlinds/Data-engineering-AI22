from print_joke import get_random_reaction


def test_get_random_reaction_type():
    reaction = get_random_reaction()
    assert str(reaction)  # check that makes sure the reaction is a string type


def test_get_random_reaction_repeats():
    # Write a test that checks that multiple calls to get_random_reaction()
    # doesn't give you the same reaction every time
    reactions = []
    for i in range(10):
        result = get_random_reaction()
        reactions.append(result)

    duplicate_count = 0
    for i in range(len(reactions)):
        for j in range(i + 1, len(reactions)):
            if reactions[i] == reactions[j]:
                duplicate_count += 1

    print(
        f"{duplicate_count} duplicate(s) found in {len(reactions)} reaction iterations."
    )

    assert duplicate_count < len(reactions)


# Come up with a test of your own and implement it here.
def not_null():
    assert get_random_reaction() != None
