from scripts.even_or_odd import even_or_odd


def test_even_or_odd():
    assert even_or_odd(4) == "Even"
    assert even_or_odd(7) == "Odd"
