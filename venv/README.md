
RSI class Documentation
This API class provides a simple interface to calculate the Relative Strength Index (RSI) for stocks using historical price data. The RSI class in this API retrieves stock data using yfinance but can be adapted to use other financial data libraries if required.

Features

    Fetch historical stock data from the past year.
    Calculate the RSI based on the last 14 days of stock prices.
    Output the RSI as a numerical value, facilitating further analysis or integration into trading strategies.

    How to Use

    Initialization: Create an instance of the RSI class with the stock ticker symbol as an argument.

    python

`rsi_calculator = RSI('AAPL')`  # For Apple stock

RSI Calculation: Call the calculate_rsi() method to fetch the data and calculate the RSI.

python

`rsi_value = rsi_calculator.calculate_rsi()`
`print(f"The RSI for AAPL is {rsi_value}")`

Customization

To use a different library for fetching stock data:

    Modify the fetch_data method: Replace the yfinance implementation with another library of your choice. Ensure that the method returns a DataFrame with at least 'Open' and 'Close' prices for each trading day.

    python

`def fetch_data(self):`
    # Implementation for another library
    `return custom_data_frame`

        Ensure Compatibility: The DataFrame must contain 'Open' and 'Close' columns as the RSI calculations depend on these values.

Dependencies

    pandas
    yfinance
    datetime

Install necessary packages using pip:

bash

`pip install pandas yfinance`

Contributing

Contributions to expand or enhance this API are welcome. Particularly valuable would be contributions that:

    Provide support for additional data sources.
    Enhance error handling and data validation.
    Improve the efficiency of data manipulation and RSI calculation.