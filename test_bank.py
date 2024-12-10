import pytest
from bank import value

@pytest.mark.parametrize("greeting, dollars",[
        ("hello", 0),
        ("hello, John", 0),
        ("hello John", 0)
    ])
def test_bank_with_lowercase_greeting_starting_with_h( greeting, dollars):
        assert value(greeting) == dollars

@pytest.mark.parametrize("greeting, dollars",[
        ("HELLO", 0),
        ("HELLO, JOHN", 0),
        ("HELLO JOHN", 0)
    ])
def test_bank_with_uppercase_greeting_starting_with_h(greeting, dollars):
        assert value(greeting) == dollars

@pytest.mark.parametrize("greeting, dollars",[
        ("hi", 20),
        ("hi, John", 20),
        ("hi John", 20)
    ])
def test_bank_with_lowercase_greeting_starting_with_h_but_not_hello( greeting, dollars):
        assert value(greeting) == dollars

@pytest.mark.parametrize("greeting, dollars",[
        ("HI", 20),
        ("HI, JOHN", 20),
        ("HI JOHN", 20)
    ])
def test_bank_with_uppercase_greeting_starting_with_h_but_not_hello(greeting, dollars):
        assert value(greeting) == dollars


@pytest.mark.parametrize("greeting, dollars",[
        ("morning", 100),
        ("morning, John", 100),
        ("mornin John", 100)
    ])
def test_bank_with_greeting_not_starting_with_h(greeting, dollars):
        assert value(greeting) == dollars


@pytest.mark.parametrize("greeting, dollars",[
        ("MORNING", 100),
        ("MORNING, JOHN", 100),
        ("MORNING JOHN", 100)
    ])
def test_bank_with_uppercase_greeting_not_starting_with_h(greeting, dollars):
        assert value(greeting) == dollars
