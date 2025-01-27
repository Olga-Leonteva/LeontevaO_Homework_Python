def is_year_leap(number):
    return True if number % 4 == 0 else False


y = int(input("год: "))
result = is_year_leap(y)
print(f"год {y} | {result}")
