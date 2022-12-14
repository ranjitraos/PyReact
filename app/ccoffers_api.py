from fastapi import FastAPI, HTTPException
from ccoffers import fetch_credit_card_offers

app = FastAPI()


@app.get("/fetch_offers")
async def fetch_credit_card_offers_api(card: str):
    validate_card_input(card)
    offers = fetch_credit_card_offers(card)
    return offers


def validate_card_input(card):
    if card.strip() in {None, ""}:
        raise HTTPException(status_code=400, detail="No card selected!")

# uvicorn ccoffers_api:app --reload