# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("What is your initial savings balance? "))
    saving_interest = float(input("What is the interest rate of your savings account? "))
    saving_maturity = int(input("In how many months will your saving account mature? "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, saving_interest, saving_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"The amount of interest you earned during the {saving_maturity} period is {interest_earned}.")
    print(f"Your new balance will be {updated_savings_balance} when the account reaches maturity.")


    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("What is your initial balance for your CD account? "))
    cd_interest = float(input("What is the interest rate of your CD account? "))
    cd_maturity = int(input("In how many months will your CD account mature? "))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"The amount of interest you earned during the {cd_maturity} period is {interest_earned}.")
    print(f"Your new balance will be {updated_cd_balance} when your account reaches maturity.")

if __name__ == "__main__":
    # Call the main function.

    main()