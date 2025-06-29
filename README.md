# 多角色角色扮演聊天API

一個基於FastAPI的多角色角色扮演聊天系統，支援多個角色同時回應。

## ⚙️  安裝與設置

建議使用虛擬環境來管理專案依賴。

```bash
python3 -m venv venv
source venv/bin/activate  # 在 macOS/Linux 上
venv\Scripts\activate  # 在 Windows 上
```

## 🚀 快速開始

### 安裝依賴
```bash
pip install -r requirements.txt
```

### 啟動服務
```bash
python GRP_PR.py
```

服務將在 `http://localhost:8000` 啟動

## 📖 API 使用

### 主要對話端點
**POST** `/respond`

請求格式：
```json
{
  "message": "你好！",
  "characters": ["lazul", "erwin", "levi"]
}
```

回應格式：
```json
{
  "replies": [
    {"name": "lazul", "reply": "嗯...你好！，這很有趣。"},
    {"name": "erwin", "reply": "關於你好！，我們需要謹慎處理。"},
    {"name": "levi", "reply": "哼，你好！，就這樣。"}
  ]
}
```

### 其他端點
- **GET** `/health` - 健康檢查
- **GET** `/list_roles` - 列出所有可用角色
- **GET** `/docs` - API 文件（Swagger UI）

## 👥 角色配置

角色配置檔案位於 `characters/` 目錄，使用YAML格式：

```yaml
basic_info:
  name: "角色名稱"
  role: "角色職業"
  age: 年齡
  personality: "性格描述"
  background: "背景故事"

speech_patterns:
  neutral: "中性回應模板 {msg}"
  happy: "開心回應模板 {msg}"
  angry: "生氣回應模板 {msg}"
  # ... 其他情緒
```

## 🎯 特色功能

- ✅ 多角色同時回應
- ✅ 基於情緒的回應系統
- ✅ 安全的檔案路徑驗證
- ✅ 完整的錯誤處理
- ✅ OpenAPI 文件自動生成

## 🔧 自定義角色

1. 在 `characters/` 目錄創建新的 `.yaml` 檔案
2. 按照上述格式配置角色資訊
3. 重啟服務即可使用新角色

## 📝 注意事項

- 角色名稱不區分大小寫
- 支援 `.yaml` 和 `.yml` 副檔名
- 預設角色為 `lazul`
- 所有角色檔案必須包含 `basic_info` 和 `speech_patterns` 區塊 