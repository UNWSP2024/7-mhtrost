def rain_fall():
    rainfall = []

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    for i in range(12):
        amount = int(input(f"Enter amount of rainfall: {months[i]}: "))
        rainfall.append(amount)

    total_rainfall = sum(rainfall)

    average_rainfall = total_rainfall / 12
    minimum_rainfall = min(rainfall)
    maximum_rainfall = max(rainfall)

    maximum_month = months[rainfall.index(maximum_rainfall)]
    minimum_month = months[rainfall.index(minimum_rainfall)]

    print("---- Rainfall Statistics ----")
    print(f"Total rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f}")
    print(f"Minimum rainfall amount and month: {minimum_rainfall:.2f} {minimum_month}")
    print(f"Maximum rainfall amount and month: {maximum_rainfall:.2f} {maximum_month}")

rain_fall()