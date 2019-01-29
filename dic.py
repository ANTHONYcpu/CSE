states = {
    "CA": "California",
    "FL": "Florida",
    "AK": "Alaska",
    "GA": "Georgia"
}

print(states["CA"])
print(states["AK"])

nested_dictionary = {
    "CA": {
        "NAME": "Califotnia",
        "POPULATION": 39500000  # 39,500,000
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000  # 21,300,000
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000  # 737,000
    },
    "GA": {
        "NAME": "georgia",
        "POPULATION": 10500000  # 10,500,000
    }
}

print(nested_dictionary["GA"]["POPULATION"])
print(nested_dictionary["FL"]["NAME"])

georgia = nested_dictionary["GA"]
print(georgia)