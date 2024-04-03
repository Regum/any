
loan_amont_all = {
    '1': 2500,
    '2': 1500,
    '3': 7500,
    '4': 4500,
    '5': 3500,
    '6': 60000,
    '7': 2000,
    '8': 3000,
    '9': 5000,
    '10': 6000,
    '11': 7000,
    '12': 6500,
}








def calculate(loan_amount):
    interest = loan_amount * 1.5
    total = loan_amount + interest
    if total > 20000:
        state_duty = ((total * 4) / 100) / 2
        state_duty = max(state_duty, 200)  
    else:
        state_duty = total - 20000
        state_duty = (state_duty * (3 * 100 + 800))
    
    
    return state_duty, interest, state_duty


for key, value in loan_amont_all.items():
    print(calculate(value))