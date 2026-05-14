status_code = int(input('Please enter status code'))

match status_code:
    case 200:
        print('Success')
        print('This is a success message. Happy')
    case 404:
        print('Not found')
    case 500:
        print('Internal Server Error')
    case _:
        print('Unknown status')