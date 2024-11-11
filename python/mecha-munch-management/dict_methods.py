"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    return add_item({}, notes)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    # Loop each recipte update and upthe recipe in ideas
    for recipe in recipe_updates:
        ideas[recipe[0]] = recipe[1]
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {
        item: [cart[item], aisle_mapping[item][0], aisle_mapping[item][1]]
        for item in cart
    }
    return dict(sorted(fulfillment_cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    print(f"** Starting {fulfillment_cart=}")
    print(f"** Starting {store_inventory=}")

    for item in store_inventory:
        new_inventory = store_inventory[item][0] - fulfillment_cart[item][0]
        #print(f"{item=}  {new_inventory=}")
        if new_inventory < 1:
            new_inventory = 'Out of Stock'

        store_inventory[item][0] = new_inventory

        #print(f"in loop {store_inventory=}")
    print(f"Returning  {store_inventory=}")
    return store_inventory
