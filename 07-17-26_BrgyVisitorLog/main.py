from data import visitors
from visitor_functions import add_visitor, display_visitors

while True:
    add_visitor(visitors)

    again = input("Add another visitor? (yes/no): ").lower()

    if again == "no":
        break

display_visitors(visitors)