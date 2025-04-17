def calculate_salary(hourly_rate, hours_worked, tax_rate=0.15):
    gross_salary = hourly_rate * hours_worked
    
    tax = gross_salary * tax_rate
    
    net_salary = gross_salary - tax
    
    return net_salary
       

def main():
    hourly_rate = float(input("Enter hourly rate: "))
    hours_worked = float(input("Enter hours worked: "))

    if hourly_rate < 0 or hours_worked < 0:
        print("Hourly rate and hours worked cannot be negative.")
        return
    
    net_salary = calculate_salary(hourly_rate, hours_worked)
    
    print(f"Net Salary: {net_salary:,.2f}")


if __name__ == "__main__":
    main()

