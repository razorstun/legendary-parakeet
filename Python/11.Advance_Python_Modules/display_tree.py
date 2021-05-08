import os

for folder, sub_folders, files in os.walk(os.getcwd()):
    print(f"Currently looking at {folder}")
    print('\n')
    print('The subfolders are: ')
    for sub_fold in sub_folders:
        print(f"Subfolder: {sub_fold}")
        print('\n')
        print("The files are: ")
        for f in files:
            print(f"\t Files: {f}")
            print('\n')