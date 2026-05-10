student_name = input("Enter student name: ")
student_major = input("Enter major code: ")

match student_major:
    case "BIOL":
        print(f"{student_name} - Biology")
        print("Science Bldg, Room 310")
    case "CSCI":
        print(f"{student_name} - Computer Science")
        print("Sheppard Hall, Room 314")
    case "ENG":
        print(f"{student_name} - English")
        print("Kerr Hall, Room 201")
    case "HIST":
        print(f"{student_name} - History")
        print("Kerr Hall, Room 114")
    case "MKT":
        print(f"{student_name} - Marketing")
        print("Westly Hall, Room 310")
    case _:
        print(f"{student_name} - <unknown>")