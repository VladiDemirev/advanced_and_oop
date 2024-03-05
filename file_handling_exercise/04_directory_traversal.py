import os

directory = input()  # As per the problem description input is "." (current directory)

files_dict = {}  # Create a dictionary {ext: [filename1, filename2, etc.]}

for element in os.listdir(directory):  # Check every element (files and folders) in the current directory
    el_path = os.path.join(directory, element)

    if os.path.isfile(el_path):
        file_ext = el_path.split(".")[-1]

        if file_ext not in files_dict:
            files_dict[file_ext] = []
        files_dict[file_ext].append(element)    # If the element is a file, add it to the files_dict

    else:   # Current element is a directory so repeat the above check
        for el in os.listdir(el_path):
            f = os.path.join(el_path, el)

            if os.path.isfile(f):
                ext = f.split(".")[-1]

                if ext not in files_dict:
                    files_dict[ext] = []
                files_dict[ext].append(el)

# Create the output file and write the content as per the problem requirements
with open(os.path.join(directory, "directory_traversal/report.txt"), "w") as file:

    for extension, filenames in sorted(files_dict.items()):
        file.write(f".{extension}\n")

        for filename in sorted(filenames):
            file.write(f"- - - {filename}\n")
