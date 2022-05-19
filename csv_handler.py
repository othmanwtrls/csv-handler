from datetime import datetime, timedelta

def sort_csv_by_priority(csv_list):
    sorted_csv_list = []
    sorted_csv_list.append(csv_list[0])

    working_csv_list = csv_list[1:]
    for task in working_csv_list:
        first_day_to_finish = datetime.strptime(task[1], "%d/%m/%Y") + timedelta(int(task[3]) - 1)
        last_day_to_start = datetime.strptime(task[2], "%d/%m/%Y") - timedelta(int(task[3]) - 1)

        task.append(first_day_to_finish)
        task.append(last_day_to_start)


    nbr_of_element = len(working_csv_list)
    for i in range(nbr_of_element):
        rowToAdd, working_csv_list = get_best_task_to_start(working_csv_list)
        sorted_csv_list.append(rowToAdd)

    for i in range(1, len(sorted_csv_list)):
        sorted_csv_list[i] = sorted_csv_list[i][:-2]

    return(sorted_csv_list)

def get_best_task_to_start(csv_list):
    listToReturn = sorted(csv_list, key = lambda x: x[-1])
    rowToReturn = listToReturn[0]

    for row in listToReturn[1:]:
        if row[-2] < rowToReturn[-2] - timedelta(int(rowToReturn[3])-1):
            rowToReturn = row
            break

    listToReturn.remove(rowToReturn)

    for row in listToReturn:
        if row[-2] - timedelta(int(row[3])-1) <= rowToReturn[-2]:
            row[-2] = rowToReturn[-2] + timedelta(int(row[3]))

    return rowToReturn, listToReturn
