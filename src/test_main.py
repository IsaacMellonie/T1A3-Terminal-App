from main import is_email_valid
import pytest


# Testing that if the email check passes it returns a True value.
def test_is_email_valid():
    example_email = "mrbig@gmail.com"
    assert is_email_valid(example_email) == True
    

# Testing that if the email check fails it returns a False value.
def test_is_email_valid_2():
    example_email_2 = "asdadsfasda234234"
    assert is_email_valid(example_email_2) == False

