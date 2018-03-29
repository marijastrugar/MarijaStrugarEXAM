"""
===================   TASK 4   ====================
* Name: Convert To Upper
*
* Write a function `convert_2_upper` that will take
* a string as an argument. The function should
* convert all lowercase letter to uppercase without
* usage of built-in function `upper()`.

* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
#Neće raditi u slučaju da unos budu brojevi, znaci interpunkcije ili velika slova

# Write your function here
def convert_2_upper(recenica):

    nova_recenica= ""

    for karakter in recenica:
        broj_slova = ord(karakter)

        if broj_slova > 96 and broj_slova < 123:
            broj_velikog_slova = broj_slova -32
            karakter = chr(broj_velikog_slova)

        nova_recenica += karakter


    return nova_recenica
recenica = input("Unesite: ")
nova_recenica = print(convert_2_upper(recenica))


def main():
    # Test your function here
    pass

main()
