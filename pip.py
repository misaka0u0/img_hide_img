from tkinter import Tk     # 从tkinter库中导入Tk类，用于创建GUI窗口
from tkinter import filedialog     # 导入filedialog模块，用于打开文件选择对话框
from PIL import Image     # 从PIL库导入Image类，用于打开和处理图片

# 创建一个Tk窗口实例，但不显示它
root = Tk()
root.withdraw()  # 隐藏Tk窗口

# 弹出"打开文件"对话框，让用户选择一张图片
image_path = filedialog.askopenfilename(title='请选择图片文件', filetypes=[('Image Files', '*.jpg *.jpeg *.png')])

# 使用PIL库打开选择的图片
if image_path:  # 如果用户选择了文件
    img = Image.open(image_path)
    img.show()  # 显示图片
else:
    print("没有选择文件")
