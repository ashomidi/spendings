def calculate_equal_share(spendings):
    total_spent = sum(spendings)
    num_people = len(spendings)
    equal_share = total_spent / num_people
    return equal_share


def calculate_payments(spendings):
    equal_share = calculate_equal_share(spendings)
    payments = []
    for spending in spendings:
        difference = equal_share - spending
        payments.append(round(difference, 2))
    return payments


def determine_payments(payments):
    transactions = []
    for idx, payment in enumerate(payments):
        if payment > 0:
            for i in range(idx):
                if payments[i] < 0:
                    amount = min(abs(payments[i]), payment)
                    transactions.append((i + 1, idx + 1, amount))
                    payment -= amount
                    payments[i] += amount
                    if payment == 0:
                        break
    return transactions


def main():
    spendings = []
    num_people = int(input("Enter the number of people: "))

    for i in range(num_people):
        spending = float(input(f"Enter spending for person {i + 1}: $"))
        spendings.append(spending)

    payments = calculate_payments(spendings)
    transactions = determine_payments(payments)

    if len(transactions) == 0:
        print("Everyone has spent the same amount. No payments needed.")
    else:
        print("Transactions:")
        for transaction in transactions:
            print(f"Person {transaction[1]} should pay ${transaction[2]:.2f} to Person {transaction[0]}")


if __name__ == "__main__":
    main()
