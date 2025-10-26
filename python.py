# -------------------------------------------------------------
# Freelance Income Tracker
# Author: [Your Name]
# Description:
#   This script helps freelancers calculate their total income,
#   taxes, and net earnings based on multiple projects.
#   It also generates a text report summarizing performance.
# -------------------------------------------------------------

# Get number of projects from the user
num_projects = int(input("Enter your number of projects: "))

# Initialize totals
total_income = 0
total_bonus = 0
total_hours = 0
projects = []

# Collect project data
for i in range(1, num_projects + 1):
    print(f"\nProject {i}:")

    # Input project details
    project_name = input("Enter your project name: ")
    hours = float(input("Enter worked hours: "))
    rate = float(input("Enter your hourly rate: "))
    bonus = float(input("Enter your work bonus: "))

    # Calculate income per project
    income = (hours * rate) + bonus

    # Store project info in list
    projects.append({
        "project_name": project_name,
        "hours": hours,
        "rate": rate,
        "bonus": bonus,
        "income": income
    })

    # Update totals
    total_income += income
    total_bonus += bonus
    total_hours += hours

    print(f"Project {project_name} income = ${income:.2f}")

# Calculate average hourly rate
average_rate = total_income / total_hours

# Determine tax rate based on total income
if total_income <= 2500:
    tax_rate = 0.05
elif total_income <= 5000:
    tax_rate = 0.10
else:
    tax_rate = 0.15

# Compute tax and net income
tax_income = total_income * tax_rate
net_income = total_income - tax_income

# Progress bar toward income goal
goal = 5000
progress_ratio = min(net_income / goal, 1.0)
progress_bar = "#" * int(progress_ratio * 20)

print("\nIncome Progress")
print(f"[{progress_bar:<20}] {progress_ratio * 100:.1f}% of $5000 goal\n")

# Generate summary report
report = f"""
📊 FREELANCE INCOME REPORT

Projects Completed   : {num_projects}
Total Hours          : {total_hours:.2f}
Average Hourly Rate  : ${average_rate:,.2f}
Total Bonus          : ${total_bonus:,.2f}
Gross Income         : ${total_income:,.2f}
Tax Rate Applied     : {tax_rate * 100:.0f}%
Tax Amount           : ${tax_income:,.2f}

Net Income (After Tax): ${net_income:,.2f}
"""

print(report)

# Display motivational message based on income level
if net_income > 5000:
    message = "🔥 Excellent month! You’re crushing it!"
elif net_income > 2500:
    message = "👏 Great work! Keep building momentum!"
else:
    message = "💡 Stay focused — next month will be better!"

print(message)

# Save report to a text file
file_name = "freelance_income_report.txt"

with open(file_name, "w", encoding="utf-8") as file:
    file.write(report)
    file.write("\nDetailed Breakdown:\n")
    for p in projects:
        file.write(
            f"{p['project_name']}: {p['hours']}h * ${p['rate']}/h + ${p['bonus']} bonus = ${p['income']:.2f}\n"
        )
    file.write(f"\n{message}\n")

print(f"\n📝 Report saved to '{file_name}' successfully.")

