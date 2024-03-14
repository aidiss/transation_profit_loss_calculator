import pandas as pd
from transation_profit_loss_calculator import main
from transation_profit_loss_calculator.config import (
    BUYS,
    SALES,
    SALES_LOG,
    BUYS_AFTER_SALES,
    DTYPES,
)

if __name__ == "__main__":
    buys = pd.read_csv(BUYS, dtype=DTYPES, index_col=0)
    sales = pd.read_csv(SALES, dtype=DTYPES, index_col=0)

    print("Portfolio before sales")
    print(buys.to_string())
    print("Sales")
    print(sales.to_string())

    buys.to_csv(BUYS_AFTER_SALES)
    buys, sales_log = main(buys, sales)
    sales_log_df = pd.concat(sales_log)[["position", "quantity", "unit_price", "profit_loss"]]
    print("Portfolio after sales")
    print(buys.to_string())
    print("Sales log")
    print(sales_log_df.to_string())
    sales_log_df.to_csv(SALES_LOG)
