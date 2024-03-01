from data_structures import *

def test_get_names():
    spicy_foods = [
        {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
        {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
        {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
    ]
    expected_names = ["Green Curry", "Buffalo Wings", "Mapo Tofu"]
    actual_names = get_names(spicy_foods)
    print ("Actual names:", actual_names)
    assert get_names(spicy_foods) == expected_names