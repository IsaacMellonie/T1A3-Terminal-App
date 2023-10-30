from main import is_email_valid
import pytest


def test_is_email_valid():
    example_email = "mrbig@gmail.com"
    assert is_email_valid(example_email) == True
    

def test_is_email_valid_2():
    example_email_2 = "asdadsfasda234234"
    assert is_email_valid(example_email_2) == True

