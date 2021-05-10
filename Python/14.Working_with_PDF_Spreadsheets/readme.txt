Working with CSV and PDFs

CSV

-   import csv
    data = open('example.csv',encoding='utf-8') - encoding to support @ symbol in file
    csv_data = csv.reader(data)
    data_lines = list(csv_data)
    len(data_lines)
    data_lines[10] - returns 10th  row - o row contains column field
    data_lines[10][3] - returns 10th row third item
    for line in data_lines[1:]:
        full_names.append(line[1]+' '+line[2])

    file_to_output = open('to_save_file.csv','w',newline='')
    csv_writer = csv.writer(file_to_output,delimiter=',')
    csv_writer.writerow(['a','b','c'])
    csv_writer.writerows([['1','2','3'],['4','5','6']])
    file_to_output.close()

    f = open('to_save_file.csv','a',newline='') - to write on existing file