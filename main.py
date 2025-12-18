import os
import stripe
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# 1. Initialize App & Stripe
app = FastAPI()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
frontend_url = os.getenv("FRONTEND_URL")

# 2. Strict CORS (Only allow the Frontend to talk to us)
origins = []
if frontend_url:
    origins.append(frontend_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Strictly enforces FRONTEND_URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Data Models
class PaymentRequest(BaseModel):
    # We only need the price_id (or you can hardcode it like your snippet)
    pass 

# 4. The "Config" Endpoint (Frontend calls this first)
@app.get("/api/v1/config/public")
def get_public_config():
    return {
        "stripePublishableKey": os.getenv("STRIPE_PUBLISHABLE_KEY"),
        "maxUploadBytes": 5 * 1024 * 1024, # 5MB limit
        "allowedImageTypes": ["image/jpeg", "image/png", "image/webp"]
    }

# 5. The Payment Endpoint (Redirects back to Frontend)
@app.post("/api/v1/payments/create")
def create_payment_session():
    if not frontend_url:
        raise HTTPException(status_code=500, detail="FRONTEND_URL not set in Render")

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': 'ETHINX Premium Headshot'},
                    'unit_amount': 4900, # $49.00
                },
                'quantity': 1,
            }],
            mode='payment',
            # Success/Cancel redirect to the FRONTEND, not the API
            success_url=f"{frontend_url}/success",
            cancel_url=f"{frontend_url}/cancel",
        )
        return {"id": session.id, "url": session.url}
    except Exception as e:
        print(f"Stripe Error: {e}")
        raise HTTPException(status_code=500, detail="Transaction failed.")

# Health Check
@app.get("/health")
def health():
    return {"status": "API Online", "frontend_target": frontend_url}
