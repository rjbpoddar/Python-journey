import sqlite3
import time

con = sqlite3.connect('Koustav.db')

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS yt_Manager(
        id INTEGER PRIMARY KEY,
        name VARCHAR(20),
        time VARCHAR(20)
    );
''')

def list_all():
    cursor.execute('''
        SELECT * FROM yt_Manager
    ''')
    for row in cursor.fetchall():
        print(row)

def add_video():
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    cursor.execute('''
        INSERT INTO yt_Manager(name, time)
        VALUES (?, ?)
    ''', (name, time))
    con.commit()

def update_video():
    index = int(input("Enter the number corresponding to the video you want to update: "))
    new_name = input("Enter the updated name: ")
    new_time = input("Enter the updated time: ")
    cursor.execute('''
        UPDATE yt_Manager
        SET name = ?, time = ?
        WHERE id = ?
    ''', (new_name, new_time, index))
    con.commit()

def delete_video():
    index = int(input("Enter the number corresponding to the video you want to delete: "))
    cursor.execute(
        "DELETE FROM yt_Manager WHERE id = ?",
        (index,)
    )
    con.commit()

def main():
    while True:
        print('\nYoutube Manager App || Select the choice you want to select.')
        print('1. List all youtube videos.')
        print('2. Add one single video.')
        print('3. Update a video.')
        print('4. Delete a video.')
        print('5. Exit from the application.')
        choice = int(input('\nEnter your choice: '))
        
        match choice:
            case 1:
                list_all()
            case 2:
                add_video()
            case 3:
                update_video()
            case 4:
                delete_video()
            case 5:
                print('Exiting from the app.....')
                time.sleep(2.5)
                break
            case _:
                print('Invalid input, Please try again.')

if __name__ == '__main__':
    main()
