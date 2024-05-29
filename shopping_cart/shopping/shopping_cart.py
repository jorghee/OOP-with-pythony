from .stock_products import StockProducts

class ShoppingCart:
  def __init__(self, stock):
    self._stock = stock   # Productos en stock
    self._item = {}   # Productos en el carrito

  def add_item(self, name, quantity):
    if self._stock.get_product(name) and quantity <= self._stock.get_product(name).quantity:
      if self._item.get(name):
        self._item[name] += quantity
      else:
        self._item[name] = quantity
    else:
      print("Producto no disponible...\n")
    
  def finalize_purchase():
    pass

  def calculate_total():
    pass
