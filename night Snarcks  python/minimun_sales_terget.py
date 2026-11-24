baseSalary = 5000
targetIncome = 30000

sales = 0
income = 0

while income < targetIncome:

    sales += 1
    commission = 0

    for range in range(1, 4):

        if range == 1:
            commission += min(sales, 5000) * 0.06

        elif range == 2:
            commission += min(max(sales - 5000, 0), 5000) * 0.08

        else:
            commission += max(sales - 10000, 0) * 0.10

    income = baseSalary + commission

print("Minimum sales required:", sales)
print("Total commission:", commission)
print("Annual income:", income)
