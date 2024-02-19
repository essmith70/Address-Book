# My address book

# Dictionary to store key value pair entries

book = {}
while True:
    print()
    print('1 - Add')
    print('2 - Search')
    print('3 - Delete')
    print('4 - exit')
    
    choice = input("Enter your option ")

    if choice == '1':
      name = input('Enter name:')
      phone = input('Enter phone:') 
      book[name] = phone
    elif choice == '2':
      name = input('Enter name:')
      print('Your search result is : ' + book[name] )
    elif choice == '3':
      name = input('Enter name:')
      del book[name]
    elif choice == '4':
      break
    else:
      print('Invalid choice')
      