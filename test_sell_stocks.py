import pandas as pd
import pytest


from transation_profit_loss_calculator import sell_stocks


@pytest.fixture
def buys():
    return pd.DataFrame({"quantity": [1], "unit_price": [1]})


@pytest.fixture
def buys_larger():
    return pd.DataFrame({"quantity": [5, 3, 2], "unit_price": [2, 3, 4]})


def test_sell_stocks_exact(buys):
    selling = sell_stocks(buys, 1, 1)
    expected = pd.DataFrame({"quantity": [1], "unit_price": [1]})
    pd.testing.assert_frame_equal(selling, expected)


def test_sell_stocks_half(buys):
    selling = sell_stocks(buys, 0.5, 1)
    expected = pd.DataFrame({"quantity": [0.5], "unit_price": [1]})
    pd.testing.assert_frame_equal(selling, expected)


def test_sell_stocks_half_price(buys):
    selling = sell_stocks(buys, 1, 0.5)
    expected = pd.DataFrame({"quantity": [1], "unit_price": [0.5]})
    pd.testing.assert_frame_equal(selling, expected)


# Test cases
def test_sell_stocks(buys_larger):
    selling = sell_stocks(buys_larger, 5, 2.5)
    expected = pd.DataFrame({"quantity": [5], "unit_price": [2.5]})
    pd.testing.assert_frame_equal(selling, expected)


def test2(buys_larger):
    # Test 2: Selling an amount that spans multiple purchases
    selling = sell_stocks(buys_larger, 8, 2.5)
    expected = pd.DataFrame({"quantity": [5, 3], "unit_price": [2.5, 2.5]})
    pd.testing.assert_frame_equal(selling, expected)


def test3(buys):
    buys = pd.DataFrame({"quantity": [1], "unit_price": [1]})
    with pytest.raises(ValueError):
        sell_stocks(buys, 2, 1)
