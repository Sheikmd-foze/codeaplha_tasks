# StockTacker 📈

A simple command-line tool to track your stock portfolio and calculate your total investment value.

## Features

- Add stocks to your portfolio by ticker symbol and quantity
- Automatically calculates the value of each holding based on preset prices
- Displays a clean investment summary
- Optionally save the summary to a text file (`investment_summary.txt`)

## Available Stocks

Currently supports the following tickers (with hardcoded prices):

| Ticker | Price |
|--------|-------|
| AAPL   | $180  |
| TSLA   | $250  |

## Requirements

- Python 3.x (no external dependencies)

## Usage

Run the script from your terminal:

```bash
python StockTacker.py
```

You'll be prompted to enter stock tickers and quantities:

```
Available stocks: ['AAPL', 'TSLA']
Enter stock name (or 'done' to finish): AAPL
Enter quantity of AAPL: 10
Enter stock name (or 'done' to finish): TSLA
Enter quantity of TSLA: 5
Enter stock name (or 'done' to finish): done

--- Investment Summary ---
AAPL: 10 shares x $180 = $1800
TSLA: 5 shares x $250 = $1250

Total Investment: $3050

Save to file? (y/n): y
Saved to investment_summary.txt
```

## How It Works

1. The script stores stock prices in a dictionary (`stock_prices`).
2. It loops, asking for a stock ticker and quantity until you type `done`.
3. If you enter the same stock multiple times, the quantities are added together.
4. It prints a summary of each holding and the total investment value.
5. You can optionally save this summary to a local text file.

## Notes / Future Improvements

- Stock prices are currently hardcoded — could be extended to fetch live prices from an API (e.g., Yahoo Finance, Alpha Vantage).
- No input validation for negative or non-integer quantities beyond basic error handling.
- Could add support for removing stocks or editing quantities after entry.

## License

Feel free to use, modify, and distribute this project.
