import sys
import csv

def main():
    check_length()
    Final_name_house= []
    try:
        with open(sys.argv[1], newline='') as file:
            csv_file_1 = csv.DictReader(file)

            for row in csv_file_1:
                new_name = row['name'].split(",")
                Final_name_house.append({'First': new_name[1].lstrip(), 'Last': new_name[0], 'House': row['house']})
                print(Final_name_house)
    except FileNotFoundError:
        sys.exit(f"Could not open {sys.argv[1]}")

    with open(sys.argv[2], "w") as file:
        csv_file_2= csv.DictWriter(file, fieldnames= ["first", "last", "house"])
        csv_file_2.writerow({"first":"first", "last":"last", "house":"house"})

        for row in Final_name_house:
            csv_file_2.writerow({"first": row["First"], "last": row["Last"], "house": row["House"]})

def check_length():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a csv file")



if __name__== "__main__":
    main()

