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
