#!/bin/bash
# 批量重命名
for f in *"$1"*; do
  mv "$f" "${f//$1/$2}"
done
echo "完成"
