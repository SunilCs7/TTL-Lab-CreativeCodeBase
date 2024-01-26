# Get user input
hour2954 = int(input("Enter an hour (1-12)2954: "))
am_pm2954 = input("Enter am or pm2954: ")
hours_into_future2954 = int(input("Enter how many hours into the future2954: "))

# Calculate future hour
future_hour2954 = (hour2954 + hours_into_future2954) % 12
future_am_pm2954 = "am" if (hour2954 + hours_into_future2954) < 12 else "pm"

print(f"The hour {hours_into_future2954} hours into the future will be {future_hour2954} {future_am_pm2954}2954.")
