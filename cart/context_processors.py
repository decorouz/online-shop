from .cart import Cart


def cart(request):
    """
    This will be run everytime we open up a template.
    """
    return {"cart": Cart(request)}
