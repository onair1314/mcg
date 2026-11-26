#!/usr/bin/env bash
# 一键启动 MCG 网站。双击或在终端运行： ./start.sh
set -e
cd "$(dirname "$0")"

PY=python3

# 检查 Flask；缺失则在本地虚拟环境里自动安装（不污染系统环境）
if ! $PY -c "import flask" >/dev/null 2>&1; then
  echo "未检测到 Flask，正在创建虚拟环境并安装依赖..."
  $PY -m venv .venv
  # shellcheck disable=SC1091
  source .venv/bin/activate
  pip install --quiet --upgrade pip
  pip install --quiet -r requirements.txt
  PY=python
elif [ -d ".venv" ]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
  PY=python
fi

echo "启动中..."
exec $PY run.py "$@"
