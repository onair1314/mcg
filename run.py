# -*- coding: utf-8 -*-
"""Entry point.

Usage:
    python run.py            # 自动选择 5055 起的空闲端口
    python run.py 8080       # 指定端口
"""
import socket
import sys
import webbrowser

from app import app


def find_free_port(preferred=5055, host="127.0.0.1"):
    """优先用 preferred，被占用就向后找一个空闲端口。"""
    for port in range(preferred, preferred + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex((host, port)) != 0:  # 连不上 => 空闲
                return port
    return 0  # 让系统随机分配


if __name__ == "__main__":
    host = "127.0.0.1"
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = find_free_port()

    url = f"http://{host}:{port}/"
    print("=" * 46)
    print(f"  MCG 网站已启动 ->  {url}")
    print("  按 Ctrl+C 停止")
    print("=" * 46)
    try:
        webbrowser.open(url)  # 自动打开浏览器
    except Exception:
        pass
    app.run(host=host, port=port, debug=True, use_reloader=True)
