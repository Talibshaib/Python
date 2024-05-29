import sqlite3




con = sqlite3.connect('video_manager.db')
cur = con.cursor()

def create_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS video(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        url TEXT NOT NULL,
        duration INTEGER NOT NULL
    )''')
    con.commit()

def list_all_video():
    cur.execute("SELECT * FROM video")
    result = cur.fetchall()
    print(result)

def add_video(name , url , duration ):
    pass

def update_video():
    pass

def delete_video():
    pass



def main():
    while True:
        print("please select any option : \n")
        print("1. list all videos : \n")
        print("2. Add a video : \n")
        print("3. update the video : \n")
        print("4. delete vedio : \n")
        print("5. exit the app : \n")
        index = input("Enter the option you want to choose : \n")

        match index:
            case '1':
                list_all_video()
            case '2':
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                break
            case _:
                print("please enter a valid option : \n")
                continue

if __name__ == "__main__":
    main()
            
