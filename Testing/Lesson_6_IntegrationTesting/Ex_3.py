from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Product:
    """
    A simple Product class to store product information.
    """
    product_id: int
    name: str
    price: float

    # def __post_init__(self):
    #     for name, field_type in self.__annotations__.items():
    #         if not isinstance(self.__dict__[name], field_type):
    #             current_type = type(self.__dict__[name])
    #             raise TypeError(f"The field `{name}` was assigned by `{current_type}` instead of `{field_type}`")


class POSSystem:
    """
    A simple Point of Sale (POS) system to manage products and sales.
    """

    def __init__(self):
        # Dictionary to store products (product_id: Product object)
        self.products = {}
        # List to hold items in the current shopping cart
        self.current_cart = []

    def get_all_products(self) -> dict:
        """
        Class method to retrieve a dictionary of all products.
        """
        # Return a copy to avoid modifying original data
        return dict(self.products)

    def add_product(self, product_id: int, name: str, price: float) -> Product | None:
        """
        Adds a new product to the system and returns the product object.
        """
        if product_id in self.products:
            print(f"Error: Product ID {product_id} already exists.")
            return None
        self.products[product_id] = Product(product_id, name, price)
        return self.products[product_id]

    def remove_product(self, product_id: int) -> Product | None:
        """
        Removes a product from the system and returns the removed product object (or None if not found).
        """
        if product_id not in self.products:
            print(f"Error: Product ID {product_id} not found.")
            return None
        removed_product = self.products.pop(product_id)
        return removed_product

    def add_to_cart(self, product_id, quantity) -> str:
        """
        Adds a product to the current shopping cart and returns a success message (or error message).
        """
        if product_id not in self.products:
            return f"Error: Product ID {product_id} not found."
        if quantity <= 0:
            return f"Error: Invalid quantity. Please enter a positive number."
        self.current_cart.append((product_id, quantity))
        return "Product added to cart successfully."

    def remove_from_cart(self, product_id: int, quantity: int) -> str:
        """
        Removes a product from the current shopping cart and returns a success message (or error message).
        """
        if not self.current_cart:
            return "Error: Cart is empty."
        if quantity <= 0:
            return f"Error: Quantity should be positive"
        for i, (cart_id, cart_quantity) in enumerate(self.current_cart):
            if cart_id == product_id:
                if quantity > cart_quantity:
                    return f"Error: Requested quantity ({quantity}) exceeds cart quantity ({cart_quantity})"
                if quantity < cart_quantity:
                    self.current_cart[i] = (cart_id, cart_quantity - quantity)
                else:
                    self.current_cart.pop(i)

                return "Product removed from cart successfully."
        return f"Error: Product ID {product_id} not found in cart."

    def view_cart(self) -> float:
        """
        Displays the items in the current shopping cart and their total price, returning the total price as a float.
        """
        if not self.current_cart:
            print("Cart is empty.")
            return 0.0
        total_price = 0
        print("Shopping Cart:")
        for product_id, quantity in self.current_cart:
            product = self.products[product_id]
            price = product.price * quantity
            total_price += price
            print(
                f"\t- {quantity}x {product.name} (${product.price:.2f}) - ${price:.2f}")
        print(f"Total: ${total_price:.2f}")
        return total_price

    def checkout(self) -> float:
        """
        Finalizes the current sale, clears the cart, and returns the total price.
        """
        if not self.current_cart:
            print("Cart is empty.")
            return 0.0
        # Call view_cart to calculate total before clearing
        total_price = self.view_cart()
        print("Checkout Successful!")
        self.current_cart = []
        return total_price