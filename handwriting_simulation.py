import pyautogui

def simulate_handwriting(result):
    """
    在指定位置模拟手写结果。
    """
    scale=4.4

    # 根据文件上下文提供的输出范围设置坐标
    x, y = 78, 841
    width, height = 635 - 78, 1160 - 841
    
    # 计算绘制位置，取中心点
    draw_x = x + width // 2
    draw_y = y + height // 2
    
    # 定义每个数字的绘制路径
    digit_paths = {
        '0': [(10, 0), (0, 10), (0, 10), (-10, 0), (0, -10), (0, -10)],
        '1': [(0, 10), (0, 10)],
        '2': [(10, 0), (0, 10), (-10, 0), (0, 10), (10, 0)],
        '3': [(5, 0), (5, 5), (-5, 5), (5, 5), (-5, 5), (-5, -5)],
        '4': [(0, 10), (10, 0), (3, 0), (-5, 0),(0, 10), (0, -10), (0, -10)],
        '5': [(10, 0), (-10, 0), (0, 10), (10, 0), (0, 10), (-10, 0)],
        '6': [(10, 0), (0, 5), (0, -5), (-10, 0), (0, 10), (0, 10), (10, 0), (0, -10), (-10, 0)],
        '7': [(10, 0), (0, 10), (0, 10)],
        # '8': [(10, 0), (0, 10), (0, 10), (-10, 0), (0, -10), (0, -10), (0, 10), (5, 0), (5, 0)],
        '8': [(10, 0), (0, 5), (-10, 10), (0, 5), (10, 0), (0, -5), (-10, -10), (0, -5)],
        '9': [(0, 10), (10, 0), (0, -10), (-10, 0), (0, 10), (10, 0), (0, 10), (1, 5)]
    }

    

    pyautogui.moveTo(draw_x, draw_y, duration=0.2)
    # 计算结果的总宽度
    total_width = len(str(result)) * 20 * scale
    start_x = draw_x - total_width / 2  # 居中起始位置

    for digit in str(result):
        pyautogui.moveTo(start_x, draw_y, duration=0.01)
        path = digit_paths.get(digit, [])
        pyautogui.mouseDown()
        for move in path:
            pyautogui.dragRel(move[0] * scale, move[1] * scale, duration=0.01)
        pyautogui.mouseUp()
        start_x += 20 * scale  # 移动到下一个数字的位置

def demo():
    """
    演示模拟手写功能的示例函数。
    """
    print("开始演示模拟手写功能...")
    
    # 测试不同的数字和缩放比例
    test_cases = (1234567890)
    

    print(f"\n测试用例: 结果 = {test_cases}")
    simulate_handwriting(test_cases)
    
    print("\n演示完成。")

if __name__ == "__main__":
    demo()