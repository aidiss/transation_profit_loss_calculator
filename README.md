# Transaction profit loss calculator

## Overview

Transaction profit loss calculator is designed to provide a clear and detailed analysis of stock transactions using the FIFO (First In, First Out) accounting method. This tool is essential for investors and financial analysts looking to gain insights into their trading performance, including the precise calculation of profit or loss on each sale.

### Installation

To install the tool, run the following command:

```bash
pip install -r requirements.txt
```

### Usage

Put you file in the `data/in` folder and run the following command:

```bash
python run.py
```

Check the the terminal or the `data/out` folder for the results.

### How FIFO Works

- **Track Purchases**: Record each stock purchase, including the quantity and price. These purchases are lined up in the order they were made.
- **Track Sales**: Record each stock sale, including the quantity and price. These sales are lined up in the order they were made.
- **For each sale**:
    - **Process Sales**: When you sell stocks, identify the earliest (first) purchases that have not yet been sold. This step follows the FIFO principle, where the first stocks bought are the first ones to be sold.
    - **Calculate Profit or Loss**: For each sale, calculate the profit or loss by subtracting the cost of the earliest purchased stocks (identified in step 2) from the sale price of the stocks sold.
    - **Update Records**: After a sale, update your purchase records by deducting the sold quantity from the earliest not-yet-sold purchase. If a sale completely depletes the earliest purchase, move to the next earliest purchase for subsequent sales.
    - Repeat for Each Sale: Repeat steps 2 to 4 for each sale transaction to maintain accurate and up-to-date records of stock holdings and financial outcomes.

### Key Features

- **FIFO Accounting**: Implements the FIFO method to accurately match purchases with sales.
- **Comprehensive Transaction Analysis**: Loads and analyzes all purchase and sale transactions to calculate net profit or loss.

## Features

- One to one sales
- Multiple positions
- Multiple fractional sales

## Future Development

- Yearly Performance: Calculate yearly performance and generate a yearly report.
- Revolut Adapter: Integrate with Revolut export format.
- Tax Optimization: Implement tax optimization strategies to minimize tax liabilities.
- Web Interface: Develop a user-friendly web interface to facilitate easy access and usage.
- Pandera Integration: Integrate Pandera to validate the input data and ensure data quality.
