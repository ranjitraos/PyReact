import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    res = fetch_credit_card_offers(user_input)
    print(res)

def fetch_credit_card_offers(card: str) -> str:
    offers = {"swiggy": "40% off"}
    if card == "hdfc": offers["swiggy"] = "25% off"
    return offers

if __name__ == "__main__":
    main()
