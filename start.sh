#!/bin/bash

echo "🚀 啟動多角色角色扮演聊天API..."

# 檢查Python是否安裝
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安裝，請先安裝Python3"
    exit 1
fi

# 檢查依賴是否安裝
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt 不存在"
    exit 1
fi

# 安裝依賴
echo "📦 安裝依賴套件..."
pip3 install -r requirements.txt

# 檢查角色目錄
if [ ! -d "characters" ]; then
    echo "❌ characters 目錄不存在"
    exit 1
fi

# 檢查是否有角色檔案
if [ -z "$(ls -A characters/*.yaml characters/*.yml 2>/dev/null)" ]; then
    echo "❌ characters 目錄中沒有角色檔案"
    exit 1
fi

echo "✅ 環境檢查完成"
echo "🌐 啟動服務於 http://localhost:8000"
echo "📖 API文件: http://localhost:8000/docs"
echo "🔍 健康檢查: http://localhost:8000/health"
echo "👥 角色列表: http://localhost:8000/list_roles"
echo ""
echo "按 Ctrl+C 停止服務"
echo ""

# 啟動服務
python3 GRP_PR.py 