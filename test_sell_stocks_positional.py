import pandas as pd
import pytest

from transation_profit_loss_calculator import sell_stocks_positional


@pytest.fixture
def buys_with_positions():
    return pd.DataFrame(
        {
            "position": ["AAPL", "AAPL", "GOOGL", "MSFT"],
            "quantity": [10, 20, 5, 20],
            "unit_price": [150, 145, 1000, 200],
        },
        index="a b c d".split(),
    )


def test_sell_stocks_positional(buys_with_positions):
    buys = buys_with_positions
    position, sales, sale_price = "AAPL", 15, 155
    expected_selling = pd.DataFrame(
        {"quantity": [10, 5], "unit_price": [155, 155], "position": ["AAPL", "AAPL"]},
        index="a b".split(),
    )
    selling = sell_stocks_positional(buys, sales, sale_price, position)
    pd.testing.assert_frame_equal(selling, expected_selling)
