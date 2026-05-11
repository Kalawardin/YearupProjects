favorite_city = ["Izmir","San Diego","Chicago","Aydin","Edirne"]

for index, city in enumerate(favorite_city, 1):
    if index == 1:
        print(f"{index} {city} <- top pick!")
    else:
        print(f"{index} {city}")