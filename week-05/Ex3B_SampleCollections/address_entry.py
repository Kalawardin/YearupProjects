contact_info = {
    "name": "John Smith",
    "address": "123 Main Street",
    "city": "Chicago",
    "state": "IL",
    "zip": "60601"
}

#print(f"{contact_info['name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")

del contact_info["name"]

full_name = {
    "first name": "John",
    "last name": "Smith"
}

full_name.update({"honorific": "Mr."})
contact_info.update({"full_name": full_name})
print(f"{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}\n{contact_info['address']}\n{contact_info['city']}, {contact_info['state']} {contact_info['zip']}")