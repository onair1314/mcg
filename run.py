# -*- coding: utf-8 -*-
"""Entry point.

Usage:
    python run.py            # 默认端口 5055
    python run.py 8080       # 指定端口
    PORT=8080 python run.py  # 环境变量指定端口
"""
import os
import socket
import sys
import webbrowser

from app import app

DEFAULT_PORT = 5055
HOST = "127.0.0.1"


def port_in_use(port, host=HOST):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((host, port)) == 0


def resolve_port():
    # 优先级：命令行参数 > 环境变量 PORT > 默认值
    if len(sys.argv) > 1:
        return int(sys.argv[1])
    if os.environ.get("PORT"):
        return int(os.environ["PORT"])
    return DEFAULT_PORT


if __name__ == "__main__":
    port = resolve_port()

    # debug 模式下 reloader 会 fork 一个子进程再次执行本文件。
    # 子进程通过 WERKZEUG_RUN_MAIN=true 标识。
    # 端口检查 / 开浏览器 只在“首个父进程”里做一次，
    # 否则子进程会把父进程占用的端口误判为冲突而退出（曾导致反复报错）。
    is_reloader_child = os.environ.get("WERKZEUG_RUN_MAIN") == "true"

    if not is_reloader_child:
        if port_in_use(port):
            print("=" * 52)
            print(f"  端口 {port} 已被占用，无法启动。")
            print(f"  换个端口再试：  python run.py 8080")
            print(f"  或先查占用进程： lsof -nP -iTCP:{port} -sTCP:LISTEN")
            print("=" * 52)
            sys.exit(1)

        url = f"http://{HOST}:{port}/"
        print("=" * 52)
        print(f"  MCG 网站已启动 ->  {url}")
        print("  按 Ctrl+C 停止")
        print("=" * 52)
        try:
            webbrowser.open(url)
        except Exception:
            pass

    app.run(host=HOST, port=port, debug=True, use_reloader=True)
