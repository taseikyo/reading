#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2024-11-03 15:34:32
# @Author  : Lewis Tian (taseikyo@gmail.com)
# @Link    : github.com/taseikyo
# @Version : python3.13

from PIL import Image
import os
import re


def generate_footnote(ch_idx=1, foot_idx=1):
    """
    @ch_idx: 章节数
    @foot_idx: 脚注序号
    """
    a_idx = f'<sup id="a{ch_idx}-{foot_idx}">[{foot_idx}](#f{ch_idx}-{foot_idx})</sup>'
    f_idx = f'<b id="f{ch_idx}-{foot_idx}">[[{foot_idx}]](#a{ch_idx}-{foot_idx})</b>'
    print(a_idx, f_idx, "\n")


def convert_image_from_png_to_jpg(path, new_width=800):
    """
    将png图片转化为jpg图片
    """
    for file in os.listdir(path):
        if not file.endswith("png"):
            continue

        filepath = f"{path}/{file}"
        print(f"image: {filepath}")

        img = Image.open(filepath)
        # 将图像转换为 RGB 模式（JPEG 不支持透明背景）
        img = img.convert("RGB")

        # 计算按比例调整后的新高度
        width_percent = new_width / float(img.width)
        new_height = int((float(img.height) * float(width_percent)))
        print(f"width: {img.width}, height: {img.height}")
        print(f"new width: {new_width}, new height: {new_height}")

        # 调整图像大小
        img = img.resize((new_width, new_height), Image.LANCZOS)

        # 构造输出路径（仅更改后缀）
        output_path = os.path.splitext(filepath)[0] + ".jpg"
        print(f"new image: {output_path}")
        img.save(output_path, "JPEG")
