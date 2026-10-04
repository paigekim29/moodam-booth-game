#!/bin/bash
# src/index.html 의 이미지 플레이스홀더를 base64로 치환해
# 인터넷 없이 단독 실행되는 HTML 파일 하나를 만든다.
set -e
cd "$(dirname "$0")"

python3 build.py
