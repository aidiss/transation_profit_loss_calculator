import pandas as pd


class NotEnoughStocksError(ValueError):
    pass


def combine_buys_and_sales(buys: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    return buys.assign(
        quantity=(buys["quantity"] - sales["quantity"]).combine_first(buys["quantity"])
    ).astype({"quantity": float})


def sell_stocks_positional(buys, sales, sale_prices, position):
    position_buys = buys[buys["position"] == position]
    selling = sell_stocks(position_buys.drop(columns=["position"]), sales, sale_prices)
    selling = selling.assign(position=position)
    return selling


def sell_stocks(buys, sale, sale_price):
    """

    Example:
    >>> buys = pd.DataFrame({"quantity": [10, 20, 30]}, index=["a", "b", "c"])
    >>> sale = 25
    >>> sale_price = 5
    >>> sell_stocks(buys, sale, sale_price)
       quantity  unit_price
    b        10           5
    c         15           5

    """
    # Check if there are enough stocks to sell
    total_stocks_available = buys["quantity"].sum()
    if total_stocks_available < sale:
        raise NotEnoughStocksError(
            f"requested {sale}, only {total_stocks_available} available."
        )

    # Initialize variables for tracking stocks left to sell and the quantities sold
    left_to_sell = sale
    quantities_sold = []
    indexes = []  # Keep track of which buys we are selling from

    # Iterate over each purchase to determine the quantity sold from each
    for index, quantity in buys["quantity"].items():
        if left_to_sell == 0:
            break  # No stocks left to sell

        # Determine how many stocks to sell from this purchase
        sell_from_this_purchase = min(quantity, left_to_sell)
        left_to_sell -= sell_from_this_purchase

        # Track the quantity sold and from which purchase
        quantities_sold.append(sell_from_this_purchase)
        indexes.append(index)

    # Create a DataFrame to represent the selling transaction
    selling = pd.DataFrame(
        {"quantity": quantities_sold, "unit_price": sale_price},
        index=indexes,
    )
    return selling


def main(buys, sales):
    sales_log = []  # Keep track of the sales
    for _, sale in sales.iterrows():
        filtered_buys = buys[buys["position"] == sale.position]
        res = sell_stocks_positional(
            buys, sale.quantity, sale.unit_price, sale.position
        )
        total_buys_price = filtered_buys[["quantity", "unit_price"]].product(axis=1)
        total_sales_price = res[["quantity", "unit_price"]].product(axis=1)
        res["profit_loss"] = total_sales_price - total_buys_price
        sales_log.append(res)
        # Deduct the sales from the buys
        buys = combine_buys_and_sales(buys, res)
    return buys, sales_log
