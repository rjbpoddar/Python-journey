import time
import json

def load_data():
    try:
        with open('list.txt', 'r') as file:
            loaded_data = json.load(file)
            return loaded_data
    except:
        return []

def save_data(videos):
    with open('list.txt', 'w') as file:
        json.dump(videos, file)

def list_all(videos):
    print('-' * 40)
    for index, video in enumerate(videos, 1):
        print(f"{index}. Name is {video['name']} and time is {video['duration']}")
    print('-' * 40)

def add_video(videos):
    name = input("Enter the name of the video: ")
    duration = input("Enter the time of the video: ")
    videos.append({
        'name': name,
        'duration': duration
    })
    save_data(videos)

def update_video(videos):
    list_all(videos)
    index = int(input("Enter the number corresponding to the video you want to update: "))
    if 1 <= index <= len(videos):
        new_name = input("Enter the updated name: ")
        new_time = input("Enter the updated time: ")
        videos[index - 1] = {
            'name': new_name,
            'duration': new_time
        }
        save_data(videos)
    else:
        print("Invalid video number.")

def delete_video(videos):
    list_all(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data(videos)

    else:
        print("Invalid video number.")

def main():
    videos = load_data()
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
                list_all(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                print('Exiting from the app.....')
                time.sleep(2.5)
                break
            case _:
                print('Invalid input, Please try again.')

if __name__ == '__main__':
    main()
