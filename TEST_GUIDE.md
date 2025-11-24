# Cursor Feedback MCP 测试指南

## 📦 构建和安装测试

### 1. 本地构建

```bash
# 清理旧的构建文件
rm -rf dist/

# 构建包
uv build

# 查看构建结果
ls -lh dist/
```

应该看到两个文件：
- `cursor_feedback_mcp-2.6.1-py3-none-any.whl` (wheel 包)
- `cursor_feedback_mcp-2.6.1.tar.gz` (源码包)

### 2. 本地安装测试

```bash
# 使用 uv tool 安装
uv tool install dist/cursor_feedback_mcp-2.6.1-py3-none-any.whl --force

# 或使用 pip 安装
pip install dist/cursor_feedback_mcp-2.6.1-py3-none-any.whl --force-reinstall
```

### 3. 命令测试

```bash
# 测试版本命令
cursor-feedback-mcp version

# 测试帮助命令
cursor-feedback-mcp --help

# 测试 Web UI 模式
cursor-feedback-mcp test --web

# 测试 MCP 服务器模式（需要在 Cursor 中配置）
cursor-feedback-mcp server
```

## 🧪 功能测试

### 测试 1: Web UI 界面

```bash
cursor-feedback-mcp test --web
```

这会：
1. 启动 Web 服务器（默认端口 9765）
2. 自动打开浏览器
3. 显示测试会话界面

**验证点：**
- ✅ 浏览器能正常打开
- ✅ 界面显示正常
- ✅ Markdown 渲染正常
- ✅ 可以输入反馈
- ✅ 可以上传图片

### 测试 2: uvx 直接调用

```bash
# 测试 uvx 调用（需要先发布到 PyPI）
uvx cursor-feedback-mcp version
uvx cursor-feedback-mcp --help
```

### 测试 3: 在 Cursor 中配置

在 Cursor 的 MCP 配置文件中添加：

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

**验证点：**
- ✅ Cursor 能正常加载 MCP 服务器
- ✅ AI 调用 interactive_feedback 工具时能正常工作
- ✅ Web UI 能正常显示和接收反馈
- ✅ 图片上传功能正常
- ✅ 超时设置生效（24小时）

## 🚀 发布到 PyPI

### 1. 检查构建文件

```bash
# 确保构建文件存在且正确
ls -lh dist/
```

### 2. 使用 twine 发布

```bash
# 安装 twine（如果还没安装）
uv add --dev twine

# 检查包的完整性
uv run twine check dist/*

# 发布到 PyPI（使用 .pypirc 中的凭证）
uv run twine upload dist/*

# 或者手动指定凭证
uv run twine upload dist/* --username __token__ --password pypi-YOUR-TOKEN
```

### 3. 验证 PyPI 发布

发布成功后，等待几分钟，然后测试：

```bash
# 使用 uvx 直接运行
uvx cursor-feedback-mcp@latest version

# 或安装后使用
pip install cursor-feedback-mcp
cursor-feedback-mcp version
```

## 📝 测试清单

在发布前，确保以下所有测试通过：

- [ ] 本地构建成功
- [ ] 本地安装成功
- [ ] `cursor-feedback-mcp version` 显示正确版本
- [ ] `cursor-feedback-mcp --help` 显示帮助信息
- [ ] `cursor-feedback-mcp test --web` 能启动 Web UI
- [ ] Web UI 界面显示正常
- [ ] Markdown 渲染正常
- [ ] 可以输入和提交反馈
- [ ] 可以上传图片
- [ ] 在 Cursor 中配置后能正常工作
- [ ] twine check 通过
- [ ] 准备好 PyPI token

## 🐛 常见问题

### 问题 1: 端口被占用

```bash
# 修改环境变量指定其他端口
export MCP_WEB_PORT=9999
cursor-feedback-mcp test --web
```

### 问题 2: 浏览器无法打开

手动打开浏览器访问：`http://127.0.0.1:9765`

### 问题 3: uvx 找不到命令

确保已发布到 PyPI，或使用本地路径：

```bash
uvx --from dist/cursor_feedback_mcp-2.6.1-py3-none-any.whl cursor-feedback-mcp version
```

## 📚 相关链接

- PyPI 项目页面: https://pypi.org/project/cursor-feedback-mcp/
- GitHub 仓库: https://github.com/zhajiahe/cursor-feedback-mcp
- 原项目: https://github.com/Minidoracat/mcp-feedback-enhanced

