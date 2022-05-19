import sys
import csv

from html_handler import *

def get_pile_path():
    try:
        with open(sys.argv[1]) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            csv_list = []
            for row in csv_reader:
                csv_list.append(row)
            return csv_list
    except Exception as e:
        print(e)
        print("File not accessible\n")
        print("Please, respect this format :")
        print("task_manager.py [csv path] [-s : to sort the csv]")
        return None



def main():
    csv_list = get_pile_path()
    if csv_list:
        if len(sys.argv) == 3 and sys.argv[2] == "-s":
            print("List sorted")
        else:
            generate_html_from_csv_list(csv_list)
            print("List no sorted")

if __name__ == "__main__":
    main()
