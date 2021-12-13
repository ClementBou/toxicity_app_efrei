import pandas as pd
import pytest
import web.predict


def test_positive_sentiment():
    assert web.predict.predict("I am happy today") == "Positive"


def test_neutral_sentiment():
    assert web.predict.predict("There is a cat in the street") == "Neutral"


def test_negative_sentiment():
    assert web.predict.predict("Paul is not satisfied of his work") == "Negative"


def test_checking_language():
    assert web.predict.checking_language("Paul is not satisfied of his work") == 1
    with pytest.raises(Exception):
        web.predict.predict.checking_language("Je suis ici")
