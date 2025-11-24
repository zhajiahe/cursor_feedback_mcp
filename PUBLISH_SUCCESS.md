# 🎉 发布成功！

## 📦 项目信息

- **项目名称**: cursor-feedback-mcp
- **最新版本**: 2.6.2
- **PyPI 地址**: https://pypi.org/project/cursor-feedback-mcp/2.6.2/
- **作者**: zhajiahe
- **Python 版本**: >=3.12

## ✅ 完成的工作

### 1. 项目重命名
- ✅ 源代码目录：`mcp_feedback_enhanced` → `cursor_feedback_mcp`
- ✅ 包名：`mcp-feedback-enhanced` → `cursor-feedback-mcp`
- ✅ 命令：`mcp-feedback-enhanced` → `cursor-feedback-mcp`

### 2. 配置更新
- ✅ 版本号：2.6.0 → 2.6.2
- ✅ 作者信息：Minidoracat → zhajiahe
- ✅ Python 版本：3.11+ → 3.12+
- ✅ GitHub 仓库：更新为新地址

### 3. 代码更新
- ✅ 所有 Python 文件中的导入引用
- ✅ 所有文档和配置文件
- ✅ 命令行帮助信息
- ✅ 版本显示信息

### 4. 构建和发布
- ✅ 成功构建 wheel 和 tar.gz 包
- ✅ 通过 twine check 验证
- ✅ 成功上传到 PyPI

## 🚀 使用方法

### 方式一：使用 uvx 直接运行（推荐）

```bash
# 运行命令
uvx cursor-feedback-mcp

# 查看版本
uvx cursor-feedback-mcp version

# 查看帮助
uvx cursor-feedback-mcp --help

# 测试 Web UI
uvx cursor-feedback-mcp test --web
```

### 方式二：使用 pip 安装

```bash
# 安装
pip install cursor-feedback-mcp

# 运行
cursor-feedback-mcp version
```

### 方式三：使用 uv tool 安装

```bash
# 安装
uv tool install cursor-feedback-mcp

# 运行
cursor-feedback-mcp version
```

### 方式四：在 Cursor 中配置

在 Cursor 的 MCP 配置文件（通常是 `~/.cursor/mcp.json` 或项目的 `mcp.json`）中添加：

```json
{
  "mcpServers": {
    "cursor-feedback-mcp": {
      "command": "uvx",
      "args": ["cursor-feedback-mcp"],
      "timeout": 86400,
      "env": {
        "MCP_DEBUG": "false",
        "MCP_WEB_HOST": "127.0.0.1",
        "MCP_WEB_PORT": "8765",
        "MCP_DESKTOP_MODE": "false",
        "MCP_LANGUAGE": "zh-CN"
      },
      "autoApprove": ["interactive_feedback"]
    }
  }
}
```

## 📝 功能特性

### 已修复的问题
1. ✅ 超时设置问题：修复了超时时间永远是 600s 的问题，现已支持 24 小时超时
2. ✅ 图片上传问题：修复了无法上传图片报错序列号错误的问题
3. ✅ 断网重连功能：新增断网不断链接功能，适合使用手机热点的场景

### 主要功能
- 🌐 Web UI 界面支持
- 🖼️ 图片上传功能
- 📝 Markdown 渲染
- ⏱️ 可配置超时时间
- 🔄 自动重连机制
- 🌍 多语言支持
- 🎨 现代化深色主题

## 🧪 测试

### 快速测试

```bash
# 测试版本命令
cursor-feedback-mcp version

# 测试 Web UI
cursor-feedback-mcp test --web
```

### 完整测试

详见 `TEST_GUIDE.md` 文件。

## 📚 相关链接

- **PyPI 项目页面**: https://pypi.org/project/cursor-feedback-mcp/
- **GitHub 仓库**: https://github.com/zhajiahe/cursor-feedback-mcp
- **原项目**: https://github.com/Minidoracat/mcp-feedback-enhanced

## 🙏 致谢

感谢原作者 [Minidoracat](https://github.com/Minidoracat) 的 [mcp-feedback-enhanced](https://github.com/Minidoracat/mcp-feedback-enhanced) 项目！

## 📅 发布日期

2025-11-24

---

**注意**: PyPI 可能需要几分钟时间来同步新版本。如果立即使用 `uvx` 遇到问题，请稍等片刻后重试。

