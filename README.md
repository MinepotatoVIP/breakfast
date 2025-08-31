# Breakfast

Welcome to the **Breakfast** Python package!

## Description

This package allows you to create and manage breakfasts by adding food items, calculating total calories, and simulating the serving time.

It provides the following features:
- Define a breakfast with a name and list of foods.
- Calculate approximate calories based on food items.
- Track preparation and serving times.
- Simulate a delay before serving the breakfast.
- Manage multiple breakfasts with a BreakfastManager class.

## Installation

Clone the repository:

```bash
git clone https://github.com/MinepotatoVIP/breakfast.git
cd breakfast

Make sure you have Python 3 installed. This project does not have external dependencies.
Usage

Here's an example of how to use the package:

from breakfast import BreakfastManager

manager = BreakfastManager()

# Create a breakfast with a delay of 5 seconds before serving
my_breakfast = manager.create_breakfast(
    name="Healthy Morning",
    food="egg, tomato, bread, butter",
    delay_seconds=5
)

# Display all breakfasts
manager.show_all_breakfasts()
