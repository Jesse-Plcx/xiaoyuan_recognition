import time
from screen_capture import capture_screen
from text_recognition import recognize_text
from calculation import calculate
from handwriting_simulation import simulate_handwriting

def main():
    # 根据实际情况调整屏幕截取区域
    region = (50, 0, 352, 600)  # 3位数减3位数

    print("开始演示...")

    result = -1

    try:
        while True:
            # 捕获屏幕
            screenshot = capture_screen(region)
            
            # 识别文本
            expression = recognize_text(screenshot)
            print(f"识别到的表达式: {expression}")
##
            # 初始化变量以跟踪重复结果
            if 'previous_result' not in locals():
                previous_result = None
                repeat_count = 0

             
            # 检查结果是否重复
            if result == previous_result:
                repeat_count += 1
            else:
                repeat_count = 0

            # 如果结果连续重复多次，将9替换为5
            if repeat_count >= 2:
                expression = expression.replace('9', '5')
                print(f"检测到多次重复结果，将9替换为5。新表达式: {expression}")

            # 更新previous_result
            previous_result = result
##
            # 计算结果
            result = calculate(expression)
            print(f"计算结果: {result}")
            
            # 模拟手写结果
            simulate_handwriting(result)
            
            time.sleep(1)  # 添加短暂延迟以避免过于频繁的循环


    except KeyboardInterrupt:
        print("演示结束")

if __name__ == "__main__":
    main()