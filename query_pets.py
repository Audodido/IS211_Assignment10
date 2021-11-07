import sqlite3

conn = sqlite3.connect('pets.db') 

cur = conn.cursor() 

def get_user():

    with conn:

        id = ''

        while id != '-1':

            try: 
                id = input("Enter an ID #:")

                if id == '-1':
                    print('Goodbye.')
                    break

                else:

                    cur.execute('''
                    SELECT ppl.first_name, 
                    ppl.last_name, 
                    p.name
                    FROM people_pets pp
                    LEFT JOIN pets p
                    ON pp.pet = p.id
                    LEFT JOIN people ppl
                    ON pp.person = ppl.id
                    WHERE ppl.id == ?''', id) 

                    results = cur.fetchall()
                    if len(results) > 0:
                        print(results)
                    else:
                        print('No users found with that ID. Please try again.')

            except:
                print('Invalid entry. Please try again.')



if __name__ == "__main__":
    get_user()