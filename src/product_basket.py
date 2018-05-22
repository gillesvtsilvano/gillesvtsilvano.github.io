class Basket(list):
  def __init__(self, products = None):
    if products == None:
      products = []
    list.__init__(self, products)

class Products:
  def __init__(self, items = None):
    if items == None:
      items = []

    self.size = len(items)
    self.current = 0
    self.items = items

  def add_item(self, o):
    self.items.append(o)
    self.size += 1

  def __iter__(self):
    return self

  def __next__(self):
    if self.current == self.size:
      raise StopIteration
    else:
      self.current += 1
      return self.items[self.current - 1]

class Product:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco
  
  def __repr__(self):
    return str((self.nome, self.preco))

b = Basket()
b.append(Product('laranja', 2.50))
b.append(Product('maca', 2.00))
b.append(Product('banana', 1.50))
b.append(Product('uva', 1.0))

product_list = Products([Product('Caneta', 3.99), Product('Caderno', 10.00), Product('Borracha', 3.00)])

b.extend(product_list)

for item in b:
  print(item)
