import sys


def pension_contribution_verification(salary_annual, contribution_employee_monthly):
    """
    Swedish pension contribution calculation / verification
    :param salary_annual: TBD
    :param contribution_employee_monthly: TBD
    :returns sorted list of 'holes' (strings)
    """

    # Constants (changed annually)
    pba = 48300  # Price Base Amount (PBA)
    iba = 71000  # Income Base Amount (IBA)
    iba_75_monthly = iba * 7.5 / 12
    iba_807_annual = iba * 8.07
    contribution_employee_monthly_min = 500
    salary_monthly = salary_annual / 12

    # The company pays a premium of 4.5% of the actual gross salary paid out every month,
    # up to an annual income of 7.5 IBA (2022: monthly salary SEK 44 375)
    # and 30% on salary amounts above 7.5 IBA.
    # Current Default Pension Contribution
    contribution_automatic_monthly = \
        min(salary_monthly, iba_75_monthly) * 0.045 + max(0, salary_monthly - iba_75_monthly) * 0.3

    # Salary Exchange (Monthly Premium)
    contribution_additional_monthly = contribution_employee_monthly * 1.058

    # Total Pension (contribution) After Salary Exchange
    contribution_total_monthly = contribution_automatic_monthly + contribution_additional_monthly

    # Monthly Salary After Salary Exchange
    salary_after_salary_exchange_monthly = salary_monthly - contribution_employee_monthly

    print(f"Current Monthly Salary {salary_monthly}")
    print(f"Current Default Pension Contribution: {contribution_automatic_monthly}")
    # print(f"Eligible for Salary Exchange: {}") # TODO
    print(f"Entered Additional Salary Exchange Amount: {contribution_employee_monthly}")
    # print(f"Entered Amount Can Be Exchanged*: {}") # TODO
    print(f"Salary Exchange (Monthly Premium): {contribution_additional_monthly}")
    print(f"Monthly Salary After Salary Exchange: {salary_after_salary_exchange_monthly}")
    print(f"Total Pension After Salary Exchange: {contribution_total_monthly}")

    # Validation steps
    # The minimum amount of salary exchange is SEK 500 per month
    if contribution_employee_monthly < contribution_employee_monthly_min:
        print("ERROR: contribution_employee below minimum")

    # and the total occupational pension premium (incl. default company contribution)
    # for an employee may never exceed
    # 30% of the employee’s annual salary,
    if contribution_total_monthly > salary_monthly * 0.3:
        print(f"ERROR: Total contribution {contribution_total_monthly} > 30% of the employee’s salary {salary_monthly * 0.3}")

    # and the total occupational pension premium (incl. default company contribution)
    # for an employee may never exceed
    # an amount equivalent to 10 Price Base Amount .
    if contribution_total_monthly > pba * 10 / 12:
        print(f"ERROR: Total contribution exceeds 10 PBA {pba * 10 / 12}")

    # Also, the employee's salary cannot be lower than 8,07 Income Base Amount
    # after the salary exchange, as it will then affect the social security benefits.
    if salary_after_salary_exchange_monthly * 12 < iba_807_annual:
        print("ERROR: salary_after_salary_exchange_monthly error")

    return True


if __name__ == '__main__':
    pension_contribution_verification(int(sys.argv[1]), int(sys.argv[2]))
