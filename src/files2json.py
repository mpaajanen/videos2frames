import os
import json

folder_path = r"c:/Users/mikko/videos2frames/frames_kaarina"  # Replace with the path to your folder
json_path = r"c:/Users/mikko/videos2frames/json/files_kaarina.json"  # Replace with the path where you want to save the output JSON file

images = []

for file_name in os.listdir(folder_path):
    if file_name.endswith(".jpg") or file_name.endswith(".png"):  # You can add more file extensions here if needed
        file_name_without_extension = os.path.splitext(file_name)[0]
        image = {"link": file_name_without_extension, "labels": []}
        images.append(image)

data = {"images": images}

with open(json_path, "w") as f:
    json.dump(data, f)
