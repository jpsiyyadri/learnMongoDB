import colorama
from colorama import Fore, Style

from src.data.category import Category
from src.data.plant import Plant

# Initialize Colorama
colorama.init()


def print_menu(title, options):
    print(f"\n{Fore.CYAN}{title}{Style.RESET_ALL}")
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")
    print(f"{Fore.RED}0. Back{Style.RESET_ALL}")


def list_categories():
    print_menu(
        "List of Categories",
        [f"{category.id}. {category.name}" for category in Category.objects()],
    )
    selected_category_id = input(
        "Enter the ID of the category to view options (or 0 to go back): "
    )
    if selected_category_id == "0":
        return
    else:
        selected_category = Category.objects(id=selected_category_id).first()
        if selected_category:
            category_menu(selected_category)
        else:
            print(f"{Fore.RED}Category not found!{Style.RESET_ALL}")


def category_menu(category):
    while True:
        print_menu(
            f"Options for category '{category.name}'",
            [
                "Show plants under this category",
                "Add a plant",
                "Modify category",
                "Delete category",
            ],
        )
        choice = input("Enter your choice: ")
        if choice == "1":
            show_plants(category)
        elif choice == "2":
            add_plant(category)
        elif choice == "3":
            modify_category(category)
        elif choice == "4":
            delete_category(category)
            break
        elif choice == "0":
            break
        else:
            print(f"{Fore.RED}Invalid choice! Please try again.{Style.RESET_ALL}")


def modify_category(category):
    new_name = input("Enter the new name for the category: ")
    category.name = new_name
    category.save()
    print(
        f"{Fore.GREEN}Category '{category.name}' modified successfully!{Style.RESET_ALL}"
    )


def delete_category(category):
    confirmation = input(
        f"Are you sure you want to delete category '{category.name}'? (yes/no): "
    )
    if confirmation.lower() == "yes":
        category.delete()
        print(
            f"{Fore.GREEN}Category '{category.name}' deleted successfully!{Style.RESET_ALL}"
        )
    else:
        print("Deletion canceled.")


def show_plants(category):
    print_menu(
        f"Plants under category '{category.name}'",
        [f"{plant.plant_id} {plant.name}" for plant in category.plants],
    )
    selected_plant_id = input(
        "Enter the ID of the plant to view options (or 0 to go back): "
    )
    if selected_plant_id == "0":
        return
    else:
        selected_plant = next(
            (
                plant
                for plant in category.plants
                if str(plant.plant_id) == str(selected_plant_id)
            ),
            None,
        )

        if selected_plant:
            plant_menu(selected_plant, category)
        else:
            print(f"{Fore.RED}Plant not found!{Style.RESET_ALL}")


def plant_menu(plant, category):
    while True:
        print_menu(
            f"Options for plant '{plant.name}'", ["Modify plant", "Delete plant"]
        )
        choice = input("Enter your choice: ")
        if choice == "1":
            modify_plant(plant, category)
        elif choice == "2":
            delete_plant(plant, category)
            break
        elif choice == "0":
            break
        else:
            print(f"{Fore.RED}Invalid choice! Please try again.{Style.RESET_ALL}")


def add_plant(category):
    print(
        f"\n{Fore.GREEN}Adding a new plant to category '{category.name}':{Style.RESET_ALL}"
    )

    plant_id = len(category.plants) + 1  # Generate a unique ID for the new plant
    plant_name = input("Enter the name of the plant: ")
    plant_description = input("Enter a description for the plant: ")
    plant_price = float(input("Enter the price of the plant: "))
    plant_image = input("Enter the URL of the plant image: ")
    plant_stock = int(input("Enter the stock quantity of the plant: "))

    new_plant = Plant(
        plant_id=plant_id,
        name=plant_name,
        description=plant_description,
        price=plant_price,
        image=plant_image,
        stock=plant_stock,
    )
    category.plants.append(new_plant)
    category.save()  # Save the updated category with the new plant
    print(
        f"{Fore.GREEN}Plant '{plant_name}' added successfully to category '{category.name}'!{Style.RESET_ALL}"
    )


def modify_plant(plant, category):
    new_name = input("Enter the new name for the plant: ")
    # Update other attributes as needed
    plant.name = new_name
    category.save()
    print(f"{Fore.GREEN}Plant '{plant.name}' modified successfully!{Style.RESET_ALL}")


def delete_plant(plant, category):
    confirmation = input(
        f"Are you sure you want to delete plant '{plant.name}'? (yes/no): "
    )
    if confirmation.lower() == "yes":
        category.plants.remove(plant)
        category.save()
        print(
            f"{Fore.GREEN}Plant '{plant.name}' deleted successfully!{Style.RESET_ALL}"
        )
    else:
        print("Deletion canceled.")


def add_category():
    new_category_name = input("Enter the name of the new category: ")
    Category(name=new_category_name).save()
    print(
        f"{Fore.GREEN}Category '{new_category_name}' added successfully!{Style.RESET_ALL}"
    )


def main():
    while True:
        print_menu(
            "Welcome to the Console App", ["List all categories", "Add a new category"]
        )
        choice = input("Enter your choice: ")

        if choice == "1":
            list_categories()
        elif choice == "2":
            add_category()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print(f"{Fore.RED}Invalid choice! Please try again.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
