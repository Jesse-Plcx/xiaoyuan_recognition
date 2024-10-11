import pytesseract
import cv2

# 手动指定 Tesseract 可执行文件的路径
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def recognize_text(image):
    """
    使用 pytesseract 识别图像中的文本。
    仅识别数字和加减符号。
    """

    # 转为灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 直方图均衡化增强对比度
    equalized_image = cv2.equalizeHist(gray_image)
    
    # 自适应阈值处理以获得二值图像
    binary_image = cv2.adaptiveThreshold(equalized_image, 255,
                                          cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY_INV, 11, 2)

    # 形态学操作去噪声
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    cleaned_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

    # 配置仅识别数字和运算符
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789+- tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz'

    text = pytesseract.image_to_string(image, config=custom_config)
    lines = text.strip().split('\n')
    text = lines[-1] if lines else ''
    return text.strip()

def demo():
    """
    测试文本识别功能的示例函数。
    """
    print("开始测试文本识别功能...")
    
    # 读取screen_capture.py生成的测试图像
    test_image_path = "region_screen_test.png"
    test_image = cv2.imread(test_image_path)
    
    
    # 识别图像中的文本
    recognized_text = recognize_text(test_image)
    
    print(f"识别到的文本: {recognized_text}")
    print("测试完成。")

if __name__ == "__main__":
    demo()
