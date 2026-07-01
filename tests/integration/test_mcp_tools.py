#!/usr/bin/env python3
"""
MCP 工具整合測試

透過 FastMCP 的記憶體內 Client 直接呼叫工具，驗證：
- get_system_info 正常回傳
- interactive_feedback 在無人回饋時正常超時（而非拋出 ASGI 500，
  藉此回歸驗證 TemplateResponse 相容性修復）
"""

import json

import pytest
from fastmcp import Client

from cursor_feedback_mcp.server import mcp


@pytest.mark.asyncio
async def test_list_tools():
    """應註冊 interactive_feedback 與 get_system_info 兩個工具"""
    async with Client(mcp) as client:
        tools = await client.list_tools()
        names = {t.name for t in tools}
        assert "interactive_feedback" in names
        assert "get_system_info" in names


@pytest.mark.asyncio
async def test_get_system_info_tool():
    """get_system_info 工具應回傳合法 JSON 文字"""
    async with Client(mcp) as client:
        result = await client.call_tool("get_system_info", {})
        assert not result.is_error
        payload = json.loads(result.content[0].text)
        assert "平台" in payload


@pytest.mark.asyncio
async def test_interactive_feedback_timeout_no_server_error():
    """無人提交回饋時應正常超時，且不出現 Internal Server Error"""
    async with Client(mcp) as client:
        result = await client.call_tool(
            "interactive_feedback",
            {"project_directory": "/tmp", "summary": "測試", "timeout": 2},
        )
        assert not result.is_error
        text = result.content[0].text
        assert "Internal Server Error" not in text
        assert "timeout" in text.lower() or "超時" in text
