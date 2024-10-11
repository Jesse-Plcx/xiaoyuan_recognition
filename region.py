
import pyautogui

print("将鼠标移动到要捕获的区域，然后按下 Ctrl+C 退出。")
try:
    pyautogui.displayMousePosition()
except KeyboardInterrupt:
    print("\n已停止显示鼠标位置。")


#输入
#77 383 
#647 563

#输出
#78 841
#635 1160