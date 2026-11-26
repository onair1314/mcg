#!/usr/bin/env bash
# 一键启动 MCG 网站：  ./start.sh  [端口]
set -e
cd "$(dirname "$0")"

pick_python() {
  # 1) 已有可用的 .venv（里面装了 flask）-> 直接用，绝不重建
  if [ -x ".venv/bin/python" ] && .venv/bin/python -c "import flask" >/dev/null 2>&1; then
    echo ".venv/bin/python"; return
  fi
  # 2) 系统 python3 自带 flask -> 直接用
  if python3 -c "import flask" >/dev/null 2>&1; then
    echo "python3"; return
  fi
  # 3) 都没有 flask -> 首次创建虚拟环境并安装（仅此一次）
  echo ""  # 交给下面处理
}

PY="$(pick_python)"

if [ -z "$PY" ]; then
  echo "首次运行：未检测到 Flask，正在创建 .venv 并安装依赖（只需一次）..."
  python3 -m venv .venv
  .venv/bin/pip install --quiet --upgrade pip
  .venv/bin/pip install --quiet -r requirements.txt
  PY=".venv/bin/python"
fi

echo "使用解释器: $PY"
exec "$PY" run.py "$@"
