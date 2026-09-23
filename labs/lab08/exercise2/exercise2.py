employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

overtime_pay = overtime_hours * 35
gross_salary = base_salary + overtime_pay

if tax_status == "Single":
    if gross_salary >= 5000:
        tax_rate = 0.22
    else:
        tax_rate = 0.18
elif tax_status == "Married":
    if gross_salary >= 6000:
        tax_rate = 0.20
    else:
        tax_rate = 0.15
elif tax_status == "Head":
    if gross_salary >= 5500:
        tax_rate = 0.25
    else:
        tax_rate = 0.19

tax_deduction = gross_salary * tax_rate
epf_deduction = gross_salary * 0.11
sosco_deduction = gross_salary * 0.005

net_salary = gross_salary - tax_deduction - epf_deduction - sosco_deduction

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
