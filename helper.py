#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2024-11-03 15:34:32
# @Author  : Lewis Tian (taseikyo@gmail.com)
# @Link    : github.com/taseikyo
# @Version : python3.13


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

    :param path: 输入的图片路径
    :param new_width: 输出图片的新宽度，长度与其成比例缩小
    """
    from PIL import Image

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


def extract_pdf_pages(input_pdf, output_pdf, start_page, end_page):
    """
    从 PDF 中提取指定页数范围的页面并保存到新的 PDF 文件中。

    :param input_pdf: 输入的 PDF 文件路径
    :param output_pdf: 输出的 PDF 文件路径
    :param start_page: 开始页数（从 1 开始）
    :param end_page: 结束页数（包含）
    """
    from PyPDF2 import PdfReader, PdfWriter

    if not os.path.exists(input_pdf):
        print(f"{input_pdf} not exists")
        return

    if start_page == 0:
        print(f"起始页码从1开始")
        return

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    if end_page > len(reader.pages):
        print(f"结束页码过大，{end_page} > {len(reader.pages)}")
        return

    # 调整页码范围为 0 索引
    for page_num in range(start_page - 1, end_page):
        writer.add_page(reader.pages[page_num])

    # 保存到新的 PDF 文件
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)
