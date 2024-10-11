import pyautogui
import cv2
import numpy as np

def capture_screen(region=None):
    """
    捕获屏幕指定区域的截图。
    region: (左, 上, 宽, 高)
    """
    screenshot = pyautogui.screenshot(region=region)
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screenshot

def demo():
    """
    测试捕获屏幕功能的实验函数。
    """
    print("开始测试捕获屏幕功能...")
    
    # 测试全屏捕获
    full_screen = capture_screen()
    print(f"全屏截图尺寸: {full_screen.shape}")
    
    # 测试指定区域捕获
    # region = (55, 350, 350, 220)  # 2位数减2位数
    # region = (50, 350, 364, 220)  # 3位数减3位数
    region = (50, 0, 352, 600)  # 3位数减3位数
    region_screen = capture_screen(region)
    print(f"指定区域截图尺寸: {region_screen.shape}")
    
    # 保存截图以供查看
    cv2.imwrite("region_screen_test.png", region_screen)
    
    print("测试完成。请查看保存的图片文件。")

if __name__ == "__main__":
    demo()