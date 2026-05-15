import random


products = ['Laptop', 
            'Monitor', 
            'Keyboard', 
            'Mouse',
            'Webcam',
            'Headset', 
            'Docking Station', 
            'USB Hub', 
            'Desk Lamp', 
            'Surge Protector'
]

random_product = random.choice(products)

print(random_product)

product_sample = random.sample(products, k = 3)

print(product_sample)

random.shuffle(products)

print(products)

print(random.randint(50,300))





