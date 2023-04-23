"""
Get head of data.
For given range, copy that many lines from the input file to the output file.
"""

range_to_copy = 5000

with open("data/global_data_50m.txt", "r") as input_file:
    with open("data/global_data_5k.txt","w") as output_file:
        for i in range(range_to_copy):
            line = input_file.readline()
            if not line:
                break
            output_file.write(line)
