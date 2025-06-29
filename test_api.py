#!/usr/bin/env python3
"""
API 測試腳本
用於測試多角色聊天API的功能
"""

import requests
import json
import time

BASE_URL = "http://localhost:8000"

def test_health():
    """測試健康檢查端點"""
    print("🔍 測試健康檢查...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"✅ 健康檢查: {response.status_code}")
        print(f"   回應: {response.json()}")
    except Exception as e:
        print(f"❌ 健康檢查失敗: {e}")

def test_list_roles():
    """測試角色列表端點"""
    print("\n🔍 測試角色列表...")
    try:
        response = requests.get(f"{BASE_URL}/list_roles")
        print(f"✅ 角色列表: {response.status_code}")
        print(f"   可用角色: {response.json()}")
    except Exception as e:
        print(f"❌ 角色列表失敗: {e}")

def test_single_character():
    """測試單一角色回應"""
    print("\n🔍 測試單一角色回應...")
    payload = {
        "message": "你好，今天天氣真好！"
    }
    try:
        response = requests.post(f"{BASE_URL}/respond", json=payload)
        print(f"✅ 單一角色回應: {response.status_code}")
        result = response.json()
        for reply in result["replies"]:
            print(f"   {reply['name']}: {reply['reply']}")
    except Exception as e:
        print(f"❌ 單一角色回應失敗: {e}")

def test_multiple_characters():
    """測試多角色回應"""
    print("\n🔍 測試多角色回應...")
    payload = {
        "message": "我們要一起去冒險嗎？",
        "characters": ["lazul", "erwin", "levi"]
    }
    try:
        response = requests.post(f"{BASE_URL}/respond", json=payload)
        print(f"✅ 多角色回應: {response.status_code}")
        result = response.json()
        for reply in result["replies"]:
            print(f"   {reply['name']}: {reply['reply']}")
    except Exception as e:
        print(f"❌ 多角色回應失敗: {e}")

def test_emotion_responses():
    """測試不同情緒的回應"""
    print("\n🔍 測試情緒回應...")
    emotions = [
        ("我很開心！", "happy"),
        ("我生氣了！", "angry"),
        ("我很難過...", "sad"),
        ("太棒了！", "excited")
    ]
    
    for message, emotion in emotions:
        print(f"\n   測試 {emotion} 情緒: '{message}'")
        payload = {
            "message": message,
            "characters": ["lazul"]
        }
        try:
            response = requests.post(f"{BASE_URL}/respond", json=payload)
            result = response.json()
            for reply in result["replies"]:
                print(f"   {reply['name']}: {reply['reply']}")
        except Exception as e:
            print(f"   ❌ 失敗: {e}")

def main():
    """執行所有測試"""
    print("🚀 開始API測試...")
    print("=" * 50)
    
    # 等待服務啟動
    print("⏳ 等待服務啟動...")
    time.sleep(2)
    
    test_health()
    test_list_roles()
    test_single_character()
    test_multiple_characters()
    test_emotion_responses()
    
    print("\n" + "=" * 50)
    print("✅ 測試完成！")

if __name__ == "__main__":
    main() 