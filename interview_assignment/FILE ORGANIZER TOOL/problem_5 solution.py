import os
import shutil


def get_category(extension):
    if extension in [".jpg", ".png", ".gif"]:
        return "Images"
    elif extension in [".pdf", ".docx", ".txt"]:
        return "Documents"
    elif extension in [".mp3", ".wav"]:
        return "Audio"
    elif extension in [".mp4", ".mov"]:
        return "Video"
    elif extension in [".zip", ".rar"]:
        return "Archives"
    else:
        return "Others"


def get_unique_filename(folder_path, filename):
    name, ext = os.path.splitext(filename)
    counter = 1

    new_name = filename
    while os.path.exists(os.path.join(folder_path, new_name)):
        new_name = f"{name}({counter}){ext}"
        counter += 1

    return new_name


def main():
    target_dir = input("Enter directory path: ").strip()

    if not os.path.isdir(target_dir):
        print("Directory does not exist")
        return

    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)

        if not os.path.isfile(item_path):
            continue

 
        flag, ext = os.path.splitext(item)
        ext = ext.lower()


        category = get_category(ext)

        category_path = os.path.join(target_dir, category)

        if not os.path.exists(category_path):
            os.mkdir(category_path)

        new_filename = get_unique_filename(category_path, item)

        shutil.move(item_path, os.path.join(category_path, new_filename))

    print("Files organized successfully")


    main()
