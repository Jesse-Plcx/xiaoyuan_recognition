import re
from text_recognition import recognize_text
from screen_capture import capture_screen

def calculate(expression):
    """
    解析算术表达式并计算结果。
    支持加法和减法。
    """
    # 使用正则表达式提取数字和运算符
    match = re.match(r'(\d+)\s*([+-])\s*(\d+)', expression)
    if match:
        num1, operator, num2 = match.groups()
        num1, num2 = int(num1), int(num2)
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
    return None

def demo():
    """
    演示整个过程的demo函数。
    """
    print("开始演示...")
    region = (50, 0, 352, 600)  # 3位数减3位数
    
    # 直接调用text_recognition函数
    image = capture_screen(region)  # 3位数减3位数
    expression = recognize_text(image)
    print(f"识别到的表达式: {expression}")
    
    result = calculate(expression)
    print(f"计算结果: {result}")
    
    print("演示结束")

if __name__ == "__main__":
    demo()
