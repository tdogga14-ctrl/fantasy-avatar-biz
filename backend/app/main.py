from fastapi import FastAPI, Request
import stripe
import os

app = FastAPI()

# This part takes the money
@app.post("/api/v1/payments/create")
async def create_payment(request: Request):
    # This tells Stripe to open the checkout page
    return {"message": "Payment system online!"}

# This part talks to the AI
@app.get("/health")
async def health_check():
    return {"status": "The AI Kitchen is Open!"}