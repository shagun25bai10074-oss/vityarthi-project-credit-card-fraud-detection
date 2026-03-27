# Simple Credit Card Fraud Detection (Basic Python)

# Function to check fraud
def check_fraud(amount, location, usual_location, hour, transactions_last_hour):
    risk_score = 0

    # Rule 1: High amount
    if amount > 50000:
        risk_score += 2

    # Rule 2: Different location
    if location != usual_location:
        risk_score += 2

    # Rule 3: Too many transactions in last hour
    if transactions_last_hour > 5:
        risk_score += 2

    # Rule 4: Odd hours (late night)
    if hour < 6 or hour > 22:
        risk_score += 1

    # Decision
    if risk_score >= 5:
        return "Fraudulent Transaction "
    elif risk_score >= 3:
        return "Suspicious Transaction "
    else:
        return "Normal Transaction "


# Sample transactions (you can modify these)
transactions = [
    {"amount": 2000, "location": "India", "usual_location": "India", "hour": 14, "transactions_last_hour": 1},
    {"amount": 75000, "location": "India", "usual_location": "India", "hour": 16, "transactions_last_hour": 2},
    {"amount": 12000, "location": "USA", "usual_location": "India", "hour": 2, "transactions_last_hour": 6},
    {"amount": 500, "location": "India", "usual_location": "India", "hour": 10, "transactions_last_hour":9}]

for i, t in enumerate(transactions):
    result = check_fraud(
        t["amount"],
        t["location"],
        t["usual_location"],
        t["hour"],
        t["transactions_last_hour"]
    )
    
    print(f"Transaction {i+1}: {result}")
