from PIL import Image
import os

def ico_to_png(input_path, output_path):
    # 打开ICO文件
    img = Image.open(input_path)

    # 选择ICO文件中的第一个图标
    icon = img.convert("RGBA").resize((100, 100), resample=Image.LANCZOS)

    # 保存为PNG文件
    icon.save(output_path, format="PNG")

def convert_all_ico_to_png(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        # 检查文件是否为ICO文件
        if filename.lower().endswith('.ico'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png")

            # 调用函数进行ICO转PNG
            ico_to_png(input_path, output_path)

            print(f'{filename} 已转换为 {output_path}')

if __name__ == "__main__":
    # 当前目录作为输入目录
    input_directory = os.getcwd()

    # 调用函数进行转换
    convert_all_ico_to_png(input_directory, input_directory)
