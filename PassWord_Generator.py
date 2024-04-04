# Create PassWord Generator

# Import Packages
import random
import string

import tqdm

# Create Letters, Numbers and Symbols
upper_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase
numbers = string.digits
symbols = "!@#$%^&*()_-."  # You Can Add More Symbols....

# Main Code

# The User Choose What He/She Wants
letters_and_numbers = input(
    "Do You Want Your PassWord To Be From _Letters And Numbers_ (Y/N) "
)

while letters_and_numbers not in ["Yes", "Y", "yes", "y", "No", "N", "no", "n"]:

    print(f"[{letters_and_numbers}] Is Not Defined")
    letters_and_numbers = input(
        "Do You Want Your PassWord To Be From _Letters And Numbers_ (Y/N) "
    )

else:

    if (
        letters_and_numbers == "Yes"
        or letters_and_numbers == "Y"
        or letters_and_numbers == "yes"
        or letters_and_numbers == "y"
    ):
        # Symbols Choose
        symbols_with_letters_and_numbers = input(
            "Do You Want Symbols In Your PassWord (Y/N) "
        )

        while symbols_with_letters_and_numbers not in [
            "Yes",
            "Y",
            "yes",
            "y",
            "No",
            "N",
            "no",
            "n",
        ]:
            print(f"[{symbols_with_letters_and_numbers}] Is Not Defined")
            symbols_with_letters_and_numbers = input(
                "Do You Want Symbols In Your PassWord (Y/N) "
            )

        else:
            # Symbols Choose == Y
            if (
                symbols_with_letters_and_numbers == "Yes"
                or symbols_with_letters_and_numbers == "Y"
                or symbols_with_letters_and_numbers == "yes"
                or symbols_with_letters_and_numbers == "y"
            ):

                # The Length Of The PassWord
                length = int(input("Enter The Length Of Your PassWord: "))

                # The Prefix Of The PassWord
                prefix = input("Enter The Prefix Plese: ")

                # Create PassWord
                password = prefix + "".join(
                    random.sample(
                        upper_letters + lower_letters + numbers + symbols, length
                    )
                )
                print(f"×Your PassWords:\n│\n╰─> {password}")

            # Symbolds Choose == N
            elif (
                symbols_with_letters_and_numbers == "No"
                or symbols_with_letters_and_numbers == "N"
                or symbols_with_letters_and_numbers == "no"
                or symbols_with_letters_and_numbers == "n"
            ):

                # Length Of PassWord
                length = int(input("Enter The Length Of Your PassWord: "))

                # The Prefix Of The PassWord
                prefix = input("Enter The Prefix Plese: ")

                # Create PassWord
                password = prefix + "".join(
                    random.sample(upper_letters + lower_letters + numbers, length)
                )
                print(f"×Your PassWords:\n│\n╰─> {password}")

    elif (
        letters_and_numbers == "No"
        or letters_and_numbers == "N"
        or letters_and_numbers == "no"
        or letters_and_numbers == "n"
    ):

        just_letters = input("Do You Want Your PassWord To Be From Just Letters (Y/N) ")

        while just_letters not in ["yes", "Yes", "y", "Y", "no", "No", "n", "N"]:

            print(f"[{just_letters}] Is Not Defined")
            just_letters = input(
                "Do You Want Your PassWord To Be From Just Letters (Y/N) "
            )

        else:

            if (
                just_letters == "yes"
                or just_letters == "y"
                or just_letters == "Yes"
                or just_letters == "Y"
            ):

                # Symbols Choose
                symbols_with_letters = input(
                    "Do You Want Symbols In Your PassWord (Y/N) "
                )

                while symbols_with_letters not in [
                    "Yes",
                    "Y",
                    "yes",
                    "y",
                    "No",
                    "N",
                    "no",
                    "n",
                ]:
                    print(f"[{symbols_with_letters}] Is Not Defined")
                    symbols_with_letters = input(
                        "Do You Want Symbols In Your PassWord (Y/N) "
                    )

                else:
                    # Symbols Choose == Y
                    if (
                        symbols_with_letters == "Yes"
                        or symbols_with_letters == "Y"
                        or symbols_with_letters == "yes"
                        or symbols_with_letters == "y"
                    ):

                        # The Length Of The PassWord
                        length = int(input("Enter The Length Of Your PassWord: "))

                        # The Prefix Of The PassWord
                        prefix = input("Enter The Prefix Plese: ")

                        # Create PassWord
                        password = prefix + "".join(
                            random.sample(
                                upper_letters + lower_letters + symbols, length
                            )
                        )
                        print(f"×Your PassWords:\n│\n╰─> {password}")

                    # Symbolds Choose == N
                    elif (
                        symbols_with_letters == "No"
                        or symbols_with_letters == "N"
                        or symbols_with_letters == "no"
                        or symbols_with_letters == "n"
                    ):

                        # Length Of PassWord
                        length = int(input("Enter The Length Of Your PassWord: "))

                        # The Prefix Of The PassWord
                        prefix = input("Enter The Prefix Plese: ")

                        # Create PassWord
                        password = prefix + "".join(
                            random.sample(upper_letters + lower_letters, length)
                        )
                        print(f"×Your PassWords:\n│\n╰─> {password}")

            elif (
                just_letters == "No"
                or just_letters == "N"
                or just_letters == "no"
                or just_letters == "n"
            ):

                print("So You Want Your PassWord To Be From Just Numbers, No Problem")

                # Length Of PassWord
                length = int(input("Enter The Length Of Your PassWord: "))

                # The Prefix Of The PassWord
                prefix = input("Enter The Prefix Plese: ")

                # Create PassWord
                password = prefix + "".join(
                    random.sample(numbers, length)
                )
                print(f"×Your PassWords:\n│\n╰─> {password}")
