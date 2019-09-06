'''
ACME Products
'''
import random


class Product:

    '''Models an ACME product.
    Parameters
    -----------------------------
    name : str
    price : int
    weight : int
    flammability : float
    identifier : int
    '''

    def __init__(self, name=None, price=10, weight=20, flammability=0.5,
                 identifier=(random.randint(1000000, 9999999))):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        '''Using price and weight to see if a product is stealable
        '''
        stealable = self.price/self.weight
        if stealable < 0.5:
            return 'Not so stealable...'
        elif stealable < 1.0:
            return 'Kinda stealable'
        else:
            return 'Very stealable!'

    def explode(self):
        '''Using flammability and weight to see if a product is explosive
        '''
        explosive = self.weight * self.flammability
        if explosive < 10:
            return '...fizzle'
        elif explosive < 50:
            return '....boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    '''Override certain parameters of the default Product class for boxing gloves
    '''
    def __init__(self, name=None, price=10, weight=10, flammability=0.5,
                 identifier=(random.randint(1000000, 9999999))):
        super().__init__(name=name, price=price, weight=weight,
                         flammability=flammability,
                         identifier=identifier)

    def explode(self):
        return '...its a glove.'

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
