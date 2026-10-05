#!/bin/bash
# 2026/10/05 22:58:15

if [ $# -ne 1 ]; then
    echo "用法: $0 <文件路径>"
    exit 1
fi

file="$1"

if [ ! -f "$file" ]; then
    echo "错误：文件不存在: $file"
    exit 1
fi

sed -i \
    -e 's/!/！/g' \
    -e 's/,/，/g' \
    -e 's/;/；/g' \
    -e 's/?/？/g' \
    -e 's/:/：/g' \
    -e 's/\./。/g' \
    "$file"

echo "处理完成: $file"
