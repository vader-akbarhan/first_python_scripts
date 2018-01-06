def show_salary_information(annual_salary):

    monthly_salary = annual_salary // 12
    daily_salary = monthly_salary // 21
    hourly_salary = daily_salary // 8

    print("Your monthly salary is {0}".format(monthly_salary))
    print("Your daily salary is {0}".format(daily_salary))
    print("Your hourly salary is {0}".format(hourly_salary))


def show_expertise_information(level):

    if level == "beginner": 
        print("You can do it, hopefully, soon.")
    elif level == "intermediate":
        print("You MUST be heading towards such a level.")
    elif level == "expert":
        print("You would develop another profession before starting imagining happiness mediated by salary for expert IT skills.")
    else:
        print("Unknown level.")


if __name__=="__main__":

    annual_salary = int(input('Type your annual salary (as an integer): '))
    level = input('Type your level ("beginner", "intermediate" or "expert"): ')

    show_salary_information(annual_salary)
    print()
    show_expertise_information(level)
