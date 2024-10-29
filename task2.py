salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

def required_capital_for_10_months(salary, spend, increase, months=10):
    total_needed = 0
    current_spend = spend

    for month in range(months):
        if salary < current_spend:
            total_needed += (current_spend - salary)

        current_spend *= (1 + increase)

    return round(total_needed)

required_capital = required_capital_for_10_months(salary, spend, increase)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_capital)
