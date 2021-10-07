"""
Netology
Import. Module. Package.
Занятие 1. Домашнее задание.
04.10.21
"""

from datetime import date
import application.salary
import application.db.people


def main():
    application.salary.calculate_salary()
    application.db.people.get_employees()
    print(date.today().strftime("%m.%d.%Y"))


if __name__ == '__main__':
    main()


