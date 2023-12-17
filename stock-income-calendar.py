import requests
import tkinter as tk

def get_dividend_data(symbol):
    api_key = "SYCORXKZW2OC5QIM"  # Replace with your Alpha Vantage API key
    base_url = "https://www.alphavantage.co/query"

    params = {
        "function": "OVERVIEW",
        "symbol": symbol,
        "apikey": api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data.get("DividendPerShare", ""), data.get("ExDividendDate", ""), data.get("DividendDate", "")

def display_dividend_calendar():
    symbols = entry.get().split(",")
    dividend_calendar.delete(1.0, tk.END)

    for symbol in symbols:
        dividend, ex_date, pay_date = get_dividend_data(symbol)
        if dividend and ex_date and pay_date:
            dividend_calendar.insert(tk.END, f"{symbol}\n")
            dividend_calendar.insert(tk.END, f"  Dividend: {dividend}\n")
            dividend_calendar.insert(tk.END, f"  Ex-Date: {ex_date}\n")
            dividend_calendar.insert(tk.END, f"  Pay-Date: {pay_date}\n\n")

# Create the main window
app = tk.Tk()
app.title("Dividend Income Calendar")

# Create and place widgets
label = tk.Label(app, text="Enter stock symbols (comma-separated):")
label.pack(pady=10)

entry = tk.Entry(app, width=30)
entry.pack(pady=10)

button = tk.Button(app, text="Get Dividend Calendar", command=display_dividend_calendar)
button.pack(pady=10)

dividend_calendar = tk.Text(app, height=15, width=50)
dividend_calendar.pack(pady=10)

# Run the application
app.mainloop()

