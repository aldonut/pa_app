from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.students


def main():
    selection = input('1 to insert \n'
                      '2 to update \n'
                      '3 to read   \n'
                      '4 to delete \n')

    print selection

    if selection == 1:
        insert()
    elif selection == 2:
        update()
    elif selection == 3:
        read()
    elif selection == 4:
        delete()
    else:
        print '\n invalid entry \n'

def insert():
    try:
        name = raw_input('name: ')
        id = input('id: ')
        email = raw_input('email: ')
        major = raw_input('major: ')
        intended_majors = raw_input('inteded majors: ')
        city_of_origin = raw_input('city of origin: ')
        housing_type = raw_input('housing type: ')



        db.students.insert_one(
            {
                "name" : name,
                "id" : id,
                "email" : email,
                "major" : major,
                "intended_majors" : intended_majors,
                "city_of_origin" : city_of_origin,
                "housing_type" : housing_type

            }
        )

    except Exception, e:
        print str(e)


main()