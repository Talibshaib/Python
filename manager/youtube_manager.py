import json


def load_data():
    try:
       with open('manager.txt','r') as file:
           return json.load(file)
    except FileNotFoundError:
        return []
def save_data_helper(vedios):
    with open('manager.txt' , 'w') as file:
        json.dump(vedios , file)

def list_all_vedio(vedios):
    print('\n')
    for index, vedio in enumerate(vedios, start=1):
        print(f"{index}. Name : {vedio['name']} , Duration : {vedio['time']}")
        
    print('\n')
def add_vedio(vedios):
    name = input("enter the vdeio name : \n")
    time = input("enter the vedio time duration : \n")
    vedios.append({'name':name,'time':time})
    save_data_helper(vedios)
    


def update_vedio(vedios):
    list_all_vedio(vedios)
    index = int(input("Enter the index value : \n"))
    if 1 <= index <= len(vedios):
        name = input('enter the vedio name : \n')
        time = input('enter the time duration : \n')
        vedios[index - 1] = {'name' : name , 'time' : time}
        save_data_helper(vedios)
    else:
        print('Enter the valid index')

#ADDITIONAL METHOD CREATED BY ME
def interchange_vedio(vedios):
    list_all_vedio(vedios)
    index_1= int(input('Enter the first index value : \n'))
    index_2= int(input('Enter the second index value : \n'))
    if index_1 <=len(vedios) and index_2 <= len(vedios):
        temp = vedios[index_1 - 1]
        vedios[index_1 - 1] = vedios[index_2 - 1]
        vedios[index_2 - 1] = temp
        save_data_helper(vedios)
    else:
        print('please enter a valid input : \n')

    
def delete_vedio(vedios):
    list_all_vedio(vedios)
    index = int(input('Enter the index value : \n'))
    if 1<= index <=len(vedios):
        del vedios[index - 1]
        save_data_helper(vedios)
    else:
        print('please enter the valid input : \n')
#ADITION METHOD CREATER BY ME
def delete_all_vedio(vedios):
    list_all_vedio(vedios)
    promp = input('Are you sure you want to delete all vedios : \n')
    if promp.lower() == 'yes':
        vedios.clear()
        save_data_helper(vedios)
    

def main():
    vedios = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube video ")
        print("2. Add a youtube video ")
        print("3. Update a youtube vedio details ")
        print("4. interchange their position")
        print("5. Delete a youtube vedio ")
        print("6. Delete all youtube vedio ")
        print("7. Exit the app")
        choise = input("Enter your choise : \n")
        # print(vedios)
        # break

        match choise:
            case '1':
                list_all_vedio(vedios)
            case '2':
                add_vedio(vedios)
            case '3':
                update_vedio(vedios)
            case '4':
                interchange_vedio(vedios)
            case '5':
                delete_vedio(vedios)
            case '6':
                delete_all_vedio(vedios)
            case '7':
                break
           
if __name__ == "__main__":
    main()

























