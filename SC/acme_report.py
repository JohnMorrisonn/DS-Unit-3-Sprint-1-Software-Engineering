from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []

    for _ in list(range(num_products)):

        product = Product(name=('{} {}'.format(sample(ADJECTIVES, k=1),
                                sample(NOUNS, k=1))), weight=randint(5, 100),
                          price=randint(5, 100), flammability=uniform(0, 2.5))

        products.append(product)

    return products


def inventory_report(products):
    total_price = 0
    total_weight = 0
    total_flam = 0

    for product in products:
        total_price += product.price
        total_weight += product.weight
        total_flam += product.flammability

    average_price = total_price/len(products)
    average_weight = total_weight/len(products)
    average_flam = total_flam/len(products)

    print('\n\n--------ACME OFFICIAL REPORT--------\n')
    print('Number of Unique Products:', len(products))
    print('Avergae Price:', average_price)
    print('Avergae Weight:', average_weight)
    print('Avergae Flammability:', average_flam)


if __name__ == '__main__':
    inventory_report(generate_products())
