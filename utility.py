from bollinger import Bollinger
from sma import SMA
from rsi import RSI

class StockAnalysisUtility:
    def __init__(self):
        self.ticker = None
        self.bollinger = None
        self.sma = None
        self.rsi = None

    def set_ticker(self):
        self.ticker = input("Enter the stock ticker symbol (e.g., AAPL for Apple or BTC-USD for bitcoin): ").upper()

    def run_analysis(self):
        self.set_ticker()
        
        # Bollinger Bands Analysis
        print("\nRunning Bollinger Bands Analysis...")
        self.bollinger = Bollinger()
        self.bollinger.user_ticker = self.ticker
        self.bollinger.run()

        # SMA Analysis
        print("\nRunning SMA Analysis...")
        self.sma = SMA(self.ticker)
        self.sma.fetch_data()
        self.sma.calculate_sma(days=14, periods=3)
        self.sma.display_results()

        # RSI Analysis
        print("\nRunning RSI Analysis...")
        self.rsi = RSI(self.ticker)
        rsi_value = self.rsi.calculate_rsi()
        print(f"RSI for the last 14 days of {self.ticker}: {rsi_value}")

    def print_summary(self):
        print("\n--- Summary of Analysis ---")
        print(f"Stock: {self.ticker}")
        
        if self.bollinger:
            print("\nBollinger Bands: Calculated (see plot)")
        
        if self.sma:
            print("\nSMA Results:")
            self.sma.display_results()
        
        if self.rsi:
            print(f"\nRSI: {self.rsi.calculate_rsi()}")

# Usage
if __name__ == "__main__":
    analyzer = StockAnalysisUtility()
    analyzer.run_analysis()
    analyzer.print_summary()
