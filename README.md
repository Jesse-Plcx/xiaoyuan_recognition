# 小猿识别项目 🐒

[中文](README-zh.md) | [English](README-en.md)

[![GitHub stars](https://img.shields.io/github/stars/Jesse-Plcx/xiaoyuan_recognition.svg)](https://github.com/Jesse-Plcx/xiaoyuan_recognition/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Jesse-Plcx/xiaoyuan_recognition.svg)](https://github.com/Jesse-Plcx/xiaoyuan_recognition/network)
[![GitHub issues](https://img.shields.io/github/issues/Jesse-Plcx/xiaoyuan_recognition.svg)](https://github.com/Jesse-Plcx/xiaoyuan_recognition/issues)
[![GitHub license](https://img.shields.io/github/license/Jesse-Plcx/xiaoyuan_recognition.svg)](https://github.com/Jesse-Plcx/xiaoyuan_recognition/blob/master/LICENSE)

## 🐵 项目介绍
本Python项目运用Tesseract OCR技术，自动识别"小猿口算"应用中的加减法算术题。目前能够解决难度高达三年级的二位到三位算术加减问题，堪称效率的得力助手。

当然也欢迎大佬给出更好的修改建议。

## 🚀 主要功能

- **屏幕捕获**：使用 `pyautogui` 精确捕获指定区域的屏幕截图
- **文本识别**：借助 `pytesseract` 强大的OCR能力识别截图中的算术表达式
- **智能计算**：解析识别出的表达式并进行准确计算
- **手写模拟**：利用 `pyautogui` 逼真地模拟手写计算结果

注：本项目基于android虚拟机进行屏幕获取，代码中的位置参数因人而异。

## 🖥️ 功能演示

![功能演示](./demo.png)

完整运行过程参见demo.mkv文件。

## 🚨 声明
此项目目前仍处于测试初级阶段，未来可能会增加更多功能。
目前本项目仅用于技术学习和研究，请勿用于任何非法用途。
并且本人不推荐炸鱼等相关行为。
