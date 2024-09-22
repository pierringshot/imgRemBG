import os
from rembg import remove
from PIL import Image
from glob import glob
from tqdm import tqdm

folder_path = 'images'

image_files = glob(os.path.join(folder_path, "*"))

if not os.path.exists('dist'):
    os.makedirs('dist')


passed_folder = folder_path + "_passed"
if not os.path.exists(passed_folder):
    os.makedirs(passed_folder)

for file in tqdm(image_files, desc="Proses davam edir...."):
    if "_passed" in file:
        print(f"Təkrarlandığı üçün '{file}' buraxılaraq sonrakına keçildi.")
        continue

    file_type = file.split(".")[-1].lower()
    if file_type not in ['jpeg', 'png', 'jpg','webp']:
        print(f"Dəstklənməyən fayl növü olduğu üçün '{file}' ötürülmüşdür.")
        continue

    input_image = Image.open(file)
    output_path = os.path.join(
        'dist', f"{os.path.splitext(os.path.basename(file))[0]}.png")
    output_image = remove(input_image)
    output_image.save(output_path)

    
    passed_file = os.path.join(passed_folder, os.path.basename(file))
    os.rename(file, passed_file)
