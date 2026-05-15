class Restaurant:

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self, customers_served):
        self.number_served += customers_served

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers")

    def customer_rating(self, rating):
        if not isinstance(rating, int):
            print("Please enter a whole number between 1 and 5.")
            return

        if rating < 1 or rating > 5:
            print("Please enter a rating from 1 to 5.")
            return

        self.customer_ratings.append(rating)
        average_rating = sum(self.customer_ratings) / len(self.customer_ratings)
        print(f"Your rating was {rating}. The average rating for this restaurant is {average_rating:.2f}")


restaurant1 = Restaurant("Sushi House", "Japanese food")
restaurant2 = Restaurant("Pasta Corner", "Italian food")
restaurant3 = Restaurant("Taco Spot", "Mexican food")

restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()

restaurant1.print_num_served()
restaurant1.add_num_served(12)
restaurant1.add_num_served(8)
restaurant1.print_num_served()

restaurant2.print_num_served()
restaurant2.add_num_served(10)
restaurant2.add_num_served(15)
restaurant2.print_num_served()

restaurant3.print_num_served()
restaurant3.add_num_served(6)
restaurant3.add_num_served(4)
restaurant3.print_num_served()

restaurant1.customer_rating(5)
restaurant1.customer_rating(4)
restaurant1.customer_rating(3)

restaurant2.customer_rating(4)
restaurant2.customer_rating(5)
restaurant2.customer_rating(5)

restaurant3.customer_rating(2)
restaurant3.customer_rating(3)
restaurant3.customer_rating(4)

restaurant1.customer_rating(6)
restaurant1.customer_rating(2.5)
restaurant1.customer_rating("5 stars!")
        