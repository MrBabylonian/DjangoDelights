### Project Overview

**"Django Delights"** represents the culminating project in the **"Build Python Apps with Django"** skill path offered by Codecademy.com. The project entails the creation of a comprehensive inventory management and sales tracking system, designed to streamline restaurant operations for managerial staff. This hands-on experience provides practical application of the skills acquired throughout the course.

### Features

- **User Authentication**: Ensures secure access to the system.
- **Menu Management**: Enables creation, deletion, and management of menu items, inclusive of their prices and required ingredients. It also provides an automatic calculation of cost per menu item.
- **Recipe Requirements**: Keep track of ingredients required per menu item and get automatically calculated cost per ingredient according to required amount.
- **Inventory Tracking**: Facilitates the addition, deletion, and management of inventory items. It also allows to monitor stock levels and adjusts ingredient prices.
- **Sales Tracking**: Allows for the registration or deletion of sales, and automatically calculates total revenue, total cost, and profit. It also deducts the used ingredients from the stock for each sale. (Note: If there are insufficient ingredients in stock for a menu item, the sale cannot be processed.)

### Original Codecademy Project Requirements

You’ve been asked by a restaurant owner to build an application that will help keep track of how much food they have throughout the day. The owner starts the day with:
- An inventory of different Ingredients, their available quantity, and their prices per unit
- A list of the restaurant’s MenuItems, and the price set for each entry
- A list of the ingredients that each menu item requires (RecipeRequirements)
- A log of all Purchases made at the restaurant

Knowing that information, the restaurant, Django Delights’ owner has asked for the following features:
- They should be able to enter in new recipes along with their recipe requirements, and how much that menu item costs.
- They should also be able to add to the inventory a name of an ingredient, its price per unit, and how much of that item is available.
- They should be able to enter in a customer purchase of a menu item. When a customer purchases an item off the menu, the inventory should be modified to accommodate what happened, as well as recording the time that the purchase was made.

Here are some helpful tips to get you started thinking about the project: Your ingredients, recipes, and purchase data should be stored in a database, and should be rendered back to the Django views. Your Django backend should supply endpoints to create new recipes via a form submission, submit customer purchases from a different form, and get information about the total cost of inventory, the total revenue for the day, the different purchases that were made, and how much inventory is required to restock (as an initial example) to render them into a Django view.

### Project Requirements

- Build an inventory and sales application using Django
- Develop locally on your machine
- Version control your application with Git and host the repository on GitHub
- Use the command line to manage your application locally and test out queries
- Users can log in, log out, and must be logged in to see the views
- Users can create items for the menu
- Users can add ingredients to the restaurant’s inventory and update their quantities
- Users can add the different recipe requirements for each menu item
- Users can record purchases of menu items (only the ones that are able to be created with what’s in the inventory!)
- Users can view the current inventory, menu items, their ingredients, and a log of all purchases made

### Prerequisites

- HTML
- CSS
- Python
- Django
- Git
- Command Line
