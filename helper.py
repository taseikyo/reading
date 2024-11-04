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

