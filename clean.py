import os

# 设置图片文件夹和txt文件夹的路径
image_folder = '/Users/lmy/Downloads/data/test'  # 替换为你的图片文件夹路径
txt_folder = '/Users/lmy/Downloads/data/xmlLabel/test'  # 替换为你的txt文件夹路径

# 获取图片文件和txt文件的列表
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith('.jpg')]
txt_files = [f for f in os.listdir(txt_folder) if f.lower().endswith('.txt')]

# 去除文件扩展名，方便匹配（同时忽略大小写）
txt_files_no_ext = [os.path.splitext(f)[0].lower() for f in txt_files]

# 遍历图片文件，查找没有对应txt文件的图片
for image in image_files:
    image_name_no_ext = os.path.splitext(image)[0].lower()  # 忽略大小写
    
    if image_name_no_ext not in txt_files_no_ext:
        # 如果没有对应的txt文件，删除图片
        image_path = os.path.join(image_folder, image)
        print(f"Deleting {image_path} because no matching txt file found.")
        os.remove(image_path)