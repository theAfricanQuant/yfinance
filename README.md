# Stock Analysis with yfinance

This project provides tools for downloading and analyzing stock market data using the yfinance library.

## Setup

This project uses [uv](https://docs.astral.sh/uv/getting-started/installation/) for Python package management and runs on Python 3.10.

### Setting up with uv

1. **Install uv** (if you haven't already):
   check the documentation above for installation instructions.


2. **Initialize uv with Python 3.10**:
   ```bash
   # Create a new virtual environment with Python 3.10
   uv init --python python 3.10 
   
   # Activate the virtual environment
   source .venv/bin/activate  # On Linux/macOS
   # OR
   .venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies with uv**:
   ```bash
  uv add yfinance ipykernel
   ```
   

## yfinance Library

[yfinance](https://pypi.org/project/yfinance/) is a popular library for downloading historical market data from Yahoo Finance API.

Key features:
- Download historical market data from Yahoo Finance
- Access key stock information and financial statements
- Handle stock splits, dividends, and capital gains
- Work with options chains, institutional holders data, and more

## Basic Usage

```python
import yfinance as yf

# Function to get stock data using method chaining
def get_stock_data(ticker, start_date, end_date, interval="1d"):
    return (
        yf.download(ticker, start=start_date, end=end_date, interval=interval)
        .pipe(lambda df: df.set_axis(df.columns.droplevel(1), axis=1))
        .pipe(lambda df: df.rename_axis(None, axis='columns'))
    )

# Example usage
aapl_data = get_stock_data("AAPL", "2023-01-01", "2023-12-31")
aapl_data.head()

# Plot closing prices
aapl_data['Close'].plot(title="AAPL Stock Price")
```

## Resources

- [yfinance Documentation](https://pypi.org/project/yfinance/)
- [Yahoo Finance](https://finance.yahoo.com/)
- [uv Documentation](https://docs.astral.sh/uv/)
