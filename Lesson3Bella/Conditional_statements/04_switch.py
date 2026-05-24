status_code = 200

match status_code:
    case 200:
        print("Success")
        print('This is a success message. Happy :)')
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status") #The wildcard '_' acts as the 'default' case