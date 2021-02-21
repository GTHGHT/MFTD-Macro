import os
import csv
import img_hash
import cv2


while True:
    file_location = input("Input The Summon Image Path/Directory : ")
    basename = os.path.basename(file_location)
    summon_name = os.path.splitext(basename)[0]
    summon_type = input("Is It Relic Or Character (R For Relic, C For Character) : ").casefold()
    if summon_type == "c":
        summon_type = "Character"
    elif summon_type == "r":
        summon_type = "Relic"
    else:
        print("Input Invalid")
        exit()
    try:
        summon_star = int(input("Input The Summon Star : "))
        summon_score = int(input("Input The Summon Score (Personal Preferences) : "))
    except ValueError:
        print("Input Invalid")
        exit()
    if os.path.exists("Bluestacks/summon_list.csv"):
        with open("Bluestacks/summon_list.csv", "a", newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            hash_ = img_hash.calc_image_hash(cv2.imread(file_location))
            csv_writer.writerow([hash_,summon_name, summon_type,summon_star, summon_score])
    else:
        if not os.path.exists("Bluestacks/"):
            os.mkdir("Bluestacks/")
        with open("Bluestacks/summon_list.csv", "w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerow([
                "Hash",
                "Name",
                "Type",
                "Star",
                "Weight"
            ])
        print("summon_list.csv not found, populate the created csv first")
        exit(0)

    exit_input = input("Exit (Y/N)?").casefold()
    if exit_input == "y":
        exit()
