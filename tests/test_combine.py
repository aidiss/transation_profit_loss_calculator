import pytest
import pandas as pd
from pandas.testing import assert_frame_equal

from transation_profit_loss_calculator import combine_buys_and_sales


@pytest.fixture
def setup_buys_sales():
    buys = pd.DataFrame(
        {
            "position": ["AAPL", "AAPL", "GOOGL", "MSFT"],
            "quantity": [10, 20, 5, 20],
            "unit_price": [150, 145, 1000, 200],
        },
        index=["a", "b", "c", "d"],
    )

    sales = pd.DataFrame(
        {
            "quantity": [5, 10],
            "unit_price": [155, 155],
        },
        index=["a", "b"],
    )
    return buys, sales


def test_combine_with_matching_sales(setup_buys_sales):
    buys, sales = setup_buys_sales
    updated_buys = combine_buys_and_sales(buys, sales)
    expected = pd.DataFrame(
        {
            "position": ["AAPL", "AAPL", "GOOGL", "MSFT"],
            "quantity": [5, 10, 5, 20],
            "unit_price": [150, 145, 1000, 200],
        },
        index=["a", "b", "c", "d"],
    ).astype({"quantity": float})

    assert_frame_equal(updated_buys, expected)


# Add more tests as necessary
