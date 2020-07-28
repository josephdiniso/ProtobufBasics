#!/usr/src/env python3

import address_pb2

def main():
    # address_book = address_pb2.AddressBook()
    # person = address_book.people.add()
    # person.id = 1234
    # person.name = "John Doe"
    # person.email = "jdoe@example.com"
    # phone = person.phones.add()
    # phone.number = "555-4321"
    # phone.type = address_pb2.Person.HOME

    # person2 = address_book.people.add()
    # person2.id = 3456
    # person2.name = "Joe DiNiso"
    # person2.email = "joseph@"
    # phone = person2.phones.add()
    # phone.number = '515231'
    # phone.type = address_pb2.Person.HOME

    # with open("./proto.pb", "wb") as f:
    #     f.write(address_book.SerializeToString())


    address_book = address_pb2.AddressBook()
    with open("./proto.pb", "rb") as f:
        address_book.ParseFromString(f.read())

    for person in address_book.people:
        print(person.name)
        for phone in person.phones:
            print(phone.number)


    

if __name__=="__main__":
    main()