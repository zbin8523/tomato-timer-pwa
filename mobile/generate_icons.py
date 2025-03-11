import os
import sys
from PIL import Image

def create_icons(source_image_path, output_dir, sizes):
    """从源图像创建多种尺寸的图标"""
    try:
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        
        # 打开源图像
        img = Image.open(source_image_path)
        
        # 为每个尺寸创建图标
        for size in sizes:
            # 调整图像大小
            resized_img = img.resize((size, size), Image.LANCZOS)
            
            # 保存调整后的图像
            output_path = os.path.join(output_dir, f"icon-{size}x{size}.png")
            resized_img.save(output_path, 'PNG')
            print(f"创建图标: {output_path}")
            
        print("所有图标创建完成!")
        return True
    except Exception as e:
        print(f"创建图标时出错: {e}")
        return False

if __name__ == "__main__":
    # 源图像路径 - 使用绝对路径
    source_image = "/Volumes/storage/trae/tomato/tomato.png"
    
    # 输出目录 - 使用绝对路径
    icons_dir = "/Volumes/storage/trae/tomato/mobile/icons"
    
    # 需要的图标尺寸
    icon_sizes = [72, 96, 128, 144, 152, 192, 384, 512]
    
    # 创建图标
    create_icons(source_image, icons_dir, icon_sizes)