# Sam Treadwell
# 9/29/2022
# Fall 2022, CS 5001
# Determining in which season the entered date occurs

def main():
    try:
        day = int(input("Enter a day: "))
        month = int(input("Enter a month: "))
        year = int(input("Enter a year: "))

        # Validate day input
        if day < 1 or day > 31:
            raise ValueError("Invalid day. Day must be between 1 and 31.")

        # Validate month input
        if month < 1 or month > 12:
            raise ValueError("Invalid month. Month must be between 1 and 12.")

        # Validate days in the month
        if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
            raise ValueError("Invalid day. April, June, September, and November have 30 days.")
        elif month == 2:
            # Check for leap year
            leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            if (leap_year and day > 29) or (not leap_year and day > 28):
                raise ValueError("Invalid day. February has 28 or 29 days depending on the year.")

        # Define each season for the months they contain
        def season(month):
            if month == 3 or month == 4 or month == 5:
                return "Spring"
            elif month == 6 or month == 7 or month == 8:
                return "Summer"
            elif month == 9 or month == 10 or month == 11:
                return "Fall"
            elif month == 12 or month == 1 or month == 2:
                return "Winter"

        # Print the entered date
        print(month, "/", day, "/", year)
        
        # Print and define which season the entered date is in
        s = season(month)
        print("This is", s)

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()
