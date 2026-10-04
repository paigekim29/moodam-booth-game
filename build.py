#!/usr/bin/env python3
"""src/index.html 에 이미지를 박아 넣어 단독 실행 HTML 하나를 만든다."""
import base64, pathlib

ROOT = pathlib.Path(__file__).parent
# 부스에서 더블클릭할 파일과, 웹 호스팅용 index.html 을 같이 만든다
OUTPUTS = [ROOT / "무담게임.html", ROOT / "index.html"]

IMAGES = {
    "__IMG_ATTRACT__": ("assets/web/attract.jpg", "jpeg"),
    "__IMG_PRIZE__": ("assets/web/prize.jpg", "jpeg"),
    "__IMG_UNIT__": ("assets/web/unit.png", "png"),
    "__IMG_LOGO__": ("assets/web/logo.png", "png"),
}

html = (ROOT / "src/index.html").read_text(encoding="utf-8")

for token, (path, kind) in IMAGES.items():
    data = base64.b64encode((ROOT / path).read_bytes()).decode()
    html = html.replace(token, f"data:image/{kind};base64,{data}")

if "__IMG_" in html:
    raise SystemExit("치환되지 않은 이미지 플레이스홀더가 남아 있습니다")

for out in OUTPUTS:
    out.write_text(html, encoding="utf-8")
    print(f"완성: {out.name}  ({out.stat().st_size/1024:.0f} KB)")
