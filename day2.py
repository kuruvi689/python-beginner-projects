
def loan_application_result(salary, credit_score):
    if salary >= 30000 and credit_score >= 700:
        return (
            "Congratulations! Your loan has been approved.",
            "You have a good salary and credit score, which makes you eligible for the loan."
        )
    elif salary >= 30000 and credit_score < 700:
        return (
            "Sorry, your loan application has been denied. You have good salary but your credit score is low.",
            "Try to improve your credit score by paying bills on time."
        )
    elif salary < 30000 and credit_score >= 700:
        return (
            "Sorry, your loan application has been denied. You have good credit score but your salary is low.",
            "Try to increase your salary by gaining new skills or finding a better job."
        )
    else:
        return (
            "Sorry, your loan application has been denied because of low credit score.",
            "You need to improve both your salary and credit score to be eligible for the loan."
        )

# Example usage (uncomment for manual testing):
if __name__ == "__main__":
    salary = float(input("Enter your salary: "))
    credit_score = float(input("Enter your credit score: "))
    result = loan_application_result(salary, credit_score)
    print(result[0])
    print(result[1])

# Example usage (uncomment for manual testing):
# salary = int(input("Enter your salary: "))
# credit_score = int(input("Enter your credit score: "))
# result = loan_application_result(salary, credit_score)
# print(result[0])
# print(result[1])