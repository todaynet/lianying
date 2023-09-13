import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def rename_txt_to_jpg(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed: {filename} -> {new_filename}")

def convert_images_to_pdf(image_folder, output_pdf_path):
    image_files = [filename for filename in os.listdir(image_folder) if filename.lower().endswith('.jpg')]
    image_files.sort()

    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        img = Image.open(image_path)
        img_width, img_height = img.size
        c.setPageSize((img_width, img_height))
        c.drawImage(image_path, 0, 0, width=img_width, height=img_height)
        c.showPage()
    c.save()

def process_directories(root_directory):
    for directory in os.listdir(root_directory):
        full_directory_path = os.path.join(root_directory, directory)
        if os.path.isdir(full_directory_path):
            print(f"Processing directory: {full_directory_path}")
            
            rename_txt_to_jpg(full_directory_path)
            
            output_pdf_name = f"{directory}.pdf"
            output_pdf_path = os.path.join(full_directory_path, output_pdf_name)
            convert_images_to_pdf(full_directory_path, output_pdf_path)
            print(f"Generated PDF: {output_pdf_path}")

if __name__ == "__main__":
    root_directory = r"C:\ALLD\architecture\py\copyright.lib.buaa.edu.cn"  # 替换为包含多个目录的根目录的实际路径
    process_directories(root_directory)
