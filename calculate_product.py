def calculate_product(a, b):
    return a * b

if __name__ == "__main__":
    try:

        a = int(input("Entrez le premier entier: "))
        b = int(input("Entrez le deuxième entier: "))
            result = calculate_product(a, b)
          print(f"Le produit de {a} et {b} est {result}.")
    except ValueError:
        print("Veuillez entrer des entiers valides.")

