import csv

input_file_path = 'input.txt'
output_file_path1 = 'output1.csv'
output_file_path2 = 'output2.csv'
output_file_path3 = 'output3.csv'
output_file_path4 = 'output4.csv'
output_file_path5 = 'output5.csv'
total_lines = 25
output_files = [output_file_path1, output_file_path2, output_file_path3, output_file_path4, output_file_path5]
lines_to_process = total_lines / len(output_files)  # Use integer division
print(lines_to_process)

with open(input_file_path, 'r') as input_file, \
     open(output_file_path1, 'w', newline='') as output_files[0], \
     open(output_file_path2, 'w', newline='') as output_files[1], \
     open(output_file_path3, 'w', newline='') as output_files[2], \
     open(output_file_path4, 'w', newline='') as output_files[3], \
     open(output_file_path5, 'w', newline='') as output_files[4]:

    i = 1
    for n in output_files:
        csv_writer = csv.writer(n)
        start_line =int(1 + lines_to_process*(i-1))
        for line_number, line in enumerate(input_file, start=start_line):
            if line_number == (start_line + lines_to_process):
                break  # Exit the loop after processing the desired number of lines

            # Split the line into fields based on '#' as a delimiter
            parts = line.strip().split('#')

            # Extract the public key (first part) and private key distances (second part)
            public_key = parts[0].strip()
            private_key_distances = parts[1].strip()

            # Write the public key and private key distances as separate columns in the CSV file
            csv_writer.writerow([public_key, private_key_distances])

        i += 1

# No need to close the files explicitly when using 'with' statements.

