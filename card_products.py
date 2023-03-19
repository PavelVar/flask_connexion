PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
    }
}


def get_products():
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
