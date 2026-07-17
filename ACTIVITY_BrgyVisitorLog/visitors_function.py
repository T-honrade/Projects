def add_visitor(visitors):
    name = input("Enter visitor name: ")
    purpose = input("Enter visitor purpose: ")

    visitors.append({
        "name": name,
        "purpose": purpose
    })


def display_visitors(visitors):
    print("\n===== BARANGAY VISITOR LOG =====")

    for i, visitor in enumerate(visitors, start=1):
        print(f"{i}. {visitor['name']} - {visitor['purpose']}")

    print(f"\nTotal Visitors: {len(visitors)}")