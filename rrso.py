import math

def calculate_series_sum(x, months, installment):
    result = 0.0
    for i in range(1, months + 1):
        result += installment * (1 / math.pow((1 + x), (i / 12)))
    return result

def calculate_rrso(credit_value, months, installment):
    safety_runs_count = 1000
    runs_count = 0
    approximation = 10000
    rsso = approximation

    series_sum = 0
    while runs_count < safety_runs_count and round(series_sum) != round(credit_value):
        if series_sum > credit_value:
            rsso += approximation
            approximation /= 2
        elif series_sum < credit_value:
            rsso -= approximation
            approximation /= 2
        series_sum = calculate_series_sum(rsso, months, installment)
        runs_count += 1

    return rsso * 100

def recalculate(credit_value, credit_months, percentage, commission=0, other_costs=0):
    S = credit_value + (commission / 100) * credit_value + other_costs
    q = 1 + (percentage / 100) / 12
    installment = 0

    if q != 1:
        installment = S * math.pow(q, credit_months) * ((q - 1) / (math.pow(q, credit_months) - 1))
    else:
        installment = S / credit_months

    rrso = calculate_rrso(credit_value - (commission / 100) * credit_value - other_costs, credit_months, installment)
    total_cost = (installment * credit_months) - credit_value + (commission / 100) * credit_value + other_costs

    return installment, rrso, total_cost

# Example usage
credit_value = float(input("Enter the credit amount: "))
credit_months = int(input("Enter the number of months: "))
interest_rate = float(input("Enter the credit interest rate (as a percentage): "))

monthly_installment, rrso, total_cost = recalculate(credit_value, credit_months, interest_rate)
print(f"Monthly Installment: {monthly_installment}")
print(f"RRSO: {rrso}%")
print(f"Total Cost: {total_cost}")
