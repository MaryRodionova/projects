class Product:
    def __init__(self, name, price, discount=0, stock=0, max_discount=20.0):
        self.name = name.strip() #удалили пробелы
        if len(self.name)<2:
            raise ValueError('Название должно быть больше двух символов')
        self.price = abs(float(price))
        self.discount = abs(float(discount))
        self.stock = abs(int(stock))
        self.max_discount =  abs(float(max_discount))
        if self.max_discount>99:
            raise ValueError('Слишком большая максимальная скидка')
        if self.discount>self.max_discount:
           self.discount=self.max_discount

    
    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
        # Здесь мы можем как-то взаимодейтствовать с учетной/бухгалтерской системой
        self.stock -= items_count

    def discounted(self):
        return self.price - (self.price * self.discount / 100)
    
    def __repr__(self):
        return f'<Product name: {self.name}, price: {self.price}, stock: {self.stock}>' 
    
    #обязательно реализован во всех потомках
    def get_color(self):
        raise NotImplementedError #метод не реализован        

product1=Product('Товар',100,stock=10) 
print(product1)     
product1.sell(5)   
print(product1) 


#Наследование


class Phone(Product):
    def __init__(self, name, price, color, discount=0, stock=0, max_discount=20.0):
        super().__init__(name, price, discount, stock, max_discount) #используем родительский innit
        self.color = color
    def get_color(self):
        return f'Цвет корпуса: {self.color}'
        
    def get_memory_size(self):
        pass
    

    def __repr__(self):
        return f'<Phone name: {self.name}, price: {self.price}, stock: {self.stock}>'


class Sofa(Product):
    def __init__(self, name, price, color, texture, discount=0, stock=0, max_discount=20.0):
        super().__init__(name, price, discount, stock, max_discount)
        self.color = color
        self.texture = texture

    def __repr__(self):
        return f'<Sofa name: {self.name}, price: {self.price}, stock: {self.stock}>'
    
    def get_color(self):
        return f'Цвет оббивки: {self.color},тип ткани {self.texture}'

phone = Phone('iPhone Xs', 100, 'серый')
#print(phone.color) 
print(phone.get_color())



sofa1=Sofa('Большой диван',25312.4,'Желтый','Велюр')        
#print(sofa1)
#print(sofa1.color)
print(sofa1.get_color())

