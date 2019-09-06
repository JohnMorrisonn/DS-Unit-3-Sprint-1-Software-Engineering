import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        prod = Product('Test Product Weight')
        self.assertEqual(prod.weight, 20)

    def test_steal_explode(self):
        prod = Product('Big Bomber', price=10, weight=30, flammability=2)
        self.assertEqual(prod.explode(), '...BABOOM!!')
        self.assertEqual(prod.stealability(), 'Not so stealable...')


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        word = generate_products()[0]
        word1, word2 = word.name.split()
        word1 = word1.strip('[').strip(']').strip("'")
        word2 = word2.strip('[').strip(']').strip("'")
        self.assertIn(word1, ADJECTIVES)
        self.assertIn(word2, NOUNS)


if __name__ == '__main__':
    unittest.main()
