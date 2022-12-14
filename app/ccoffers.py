import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    res = fetchCreditCardOffers(user_input)
    print(res)

def fetchCreditCardOffers(card: str) -> str:
    offers = {"swiggy": "40% off"}
    return offers

if __name__ == "__main__":
    main()
