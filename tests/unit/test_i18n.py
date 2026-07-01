#!/usr/bin/env python3
"""
i18n 模組單元測試
"""

from cursor_feedback_mcp.i18n import get_i18n_manager


def test_i18n_manager_singleton():
    """get_i18n_manager 應回傳同一實例"""
    manager_a = get_i18n_manager()
    manager_b = get_i18n_manager()
    assert manager_a is manager_b


def test_i18n_translation_returns_str():
    """翻譯查詢應回傳字串（找不到時回傳 key 本身）"""
    manager = get_i18n_manager()
    result = manager.t("app.title")
    assert isinstance(result, str)
    assert result != ""
