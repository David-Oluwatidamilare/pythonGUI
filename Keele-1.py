import csv
import typer


app = typer.Typer()

@app.command()
def locate():
    header = ['Building_Name', 'Classification', 'Building_Number']
    keele = []
    file = open('Keele Project.csv','r', newline='')
    next(file)
    reader = csv.DictReader(file, fieldnames=header)

    for row in reader:
       keele.append(row)

    option = int(input('''Press "1" to enter a building/location name or part-name \nPress "2" to enter a building/location number \nPress "3" to enter a building/location classification\n:'''))
    

    if option == 1:
        buidling_location_name = input('Enter building/location name: ')
        for building_info in keele:
            if building_info['Building_Name'] == buidling_location_name:
                print('Building Number: ', building_info['Building_Number'],'\n','Building Classification: ', building_info['Classification'])

    elif option == 2:
        buidling_location_number = input('Enter building/location number: ')
        for building_info in keele:
            if building_info['Building_Number'] == buidling_location_number:
                print('Building Name: ',building_info['Building_Name'],'\n','Building Classification: ', building_info['Classification'])

    elif option == 3:
        buidling_classification = input('Enter building/location classification: ')
        for building_info in keele:
            if building_info['Classification'] == buidling_classification:
                print('Building Name: ',building_info['Building_Name'],'\n','Building Number: ', building_info['Building_Number'])
                

    else:
        print('Invalid Input!!!')
        print('Try again!!!')
        locate()
        


if __name__ == "__main__":
    app()

