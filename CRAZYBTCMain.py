import requests

currency = "usd"

def get_bitcoin_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin",
            "vs_currencies": currency,
        }
        response = requests.get(url, params=params)
        data = response.json()
        bitcoin_price = data["bitcoin"][currency]
        return bitcoin_price
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    print("Welcome to the Bitcoin Price Tracker!")

    while True:
        print("\nOptions:")
        print("1. Get Bitcoin Price")
        print("2. Change Currency")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bitcoin_price = get_bitcoin_price()
            if bitcoin_price is not None:
                print(f"Bitcoin Price ({currency.upper()}): {bitcoin_price} {currency.upper()}")
        elif choice == "2":
            new_currency = input("Enter the currency code (e.g., 'eur', 'jpy', 'gbp'): ").lower()
            currency = new_currency
            print(f"Currency changed to {new_currency.upper()}.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
