from PIL import Image, ImageFilter
import os

def resize_images(input_folder, output_folder, target_size=(100, 100)):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        # 检查文件是否为图片文件或ICO文件
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # 如果是ICO文件，选择其中一个图标尺寸
            if filename.lower().endswith('.ico'):
                img = Image.open(input_path)
                img = img.convert("RGBA")
                img = img.resize(target_size, resample=Image.LANCZOS)
            else:
                # 对其他图片文件进行普通的等比例缩放
                img = Image.open(input_path)
                img.thumbnail(target_size, resample=Image.LANCZOS)

            # 保存缩放后的图片
            img.save(output_path)

            print(f'{filename} 已缩放至 {target_size}')

if __name__ == "__main__":
    # 当前目录作为输入目录
    input_directory = os.getcwd()

    # 创建一个名为resized的子文件夹来保存缩放后的图片
    output_directory = os.path.join(input_directory, 'resized')

    # 调用函数进行图片缩放
    resize_images(input_directory, output_directory)
