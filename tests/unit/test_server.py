#!/usr/bin/env python3
"""
server 模組單元測試
"""

import json

from cursor_feedback_mcp.server import (
    create_feedback_text,
    is_remote_environment,
    is_wsl_environment,
)


def test_get_system_info_returns_valid_json():
    """get_system_info 應回傳合法 JSON 且包含關鍵欄位"""
    from cursor_feedback_mcp.server import get_system_info

    raw = get_system_info()
    data = json.loads(raw)

    assert "平台" in data
    assert "Python 版本" in data
    assert isinstance(data["環境變數"], dict)


def test_create_feedback_text_with_feedback():
    """含文字回饋時應包含用戶回饋段落"""
    text = create_feedback_text({"interactive_feedback": "測試內容"})
    assert "用戶回饋" in text
    assert "測試內容" in text


def test_create_feedback_text_empty():
    """空資料時回傳預設提示"""
    text = create_feedback_text({})
    assert text == "用戶未提供任何回饋內容。"


def test_environment_detection_returns_bool():
    """環境偵測函數應回傳布林值"""
    assert isinstance(is_wsl_environment(), bool)
    assert isinstance(is_remote_environment(), bool)
