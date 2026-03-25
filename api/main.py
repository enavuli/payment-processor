import os
import logging
from datetime import datetime
from payment_processor.payment import PaymentProcessor
from payment_processor.exceptions import PaymentError, InvalidPaymentDetails

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_payment(amount, card_details):
    try:
        processor = PaymentProcessor()
        transaction_id = processor.process(amount, card_details)
        logging.info(f"Payment processed successfully. Transaction ID: {transaction_id}")
        return transaction_id
    except InvalidPaymentDetails as e:
        logging.error(f"Invalid payment details: {e}")
        raise
    except PaymentError as e:
        logging.error(f"Payment processing failed: {e}")
        raise

if __name__ == "__main__":
    amount = 100.0
    card_details = {
        "card_number": "4111111111111111",
        "expiry_date": "12/25",
        "cvv": "123"
    }
    
    try:
        transaction_id = process_payment(amount, card_details)
        print(f"Payment successful. Transaction ID: {transaction_id}")
    except Exception as e:
        print(f"Payment failed: {e}")