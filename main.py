### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, quantity in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < quantity:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins")
        large_dollars = int(input("How many large dollars?: ")) * 1.0
        half_dollars = int(input("How many half dollars?: ")) * 0.5
        quarters = int(input("How many quarters?: ")) * 0.25
        nickels = int(input("How many nickels?: ")) * 0.05

        total = large_dollars + half_dollars + quarters + nickels
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change >= 0:
                print(f"Here is ${change} in change.")
                return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, quantity in order_ingredients.items():
            self.machine_resources[ingredient] -= quantity
        print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appetit!")

# ### Make an instance of SandwichMachine class and write the rest of the codes ###
# sandwich_machine = SandwichMachine(resources)

# def order_sandwich():
#     while True:
#         print("What size sandwich would you like? (small/ medium/ large/ off/ report): ")
#         choice = input().lower()

#         if choice in ["small", "medium", "large"]:
#             order_ingredients = recipes[choice]["ingredients"]
#             cost = recipes[choice]["cost"]
#             if sandwich_machine.check_resources(order_ingredients):
#                 print("Please insert coins.")
#                 coins = sandwich_machine.process_coins()
#                 if sandwich_machine.transaction_result(coins, cost):
#                     sandwich_machine.make_sandwich(choice, order_ingredients)
#         elif choice == "off":
#             break
#         elif choice == "report":
#             for ingredient, quantity in sandwich_machine.machine_resources.items():
#                 unit = "slice(s)" if ingredient != "cheese" else "ounce(s)"
#                 print(f'{ingredient.capitalize()}: {quantity}{unit}')
#         else:
#             print("Invalid input. Please choose from small, medium, large, off, or report.")


# order_sandwich()

