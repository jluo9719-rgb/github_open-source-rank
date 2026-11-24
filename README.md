# 🚀 GitHub 新兴飙升开源榜

一个零依赖、全自动更新的 GitHub 新兴开源项目排行榜，专注追踪 **近 7 天** 与 **近 30 天** 内新创建且 Star 增长最快的仓库。

> 🌐 **在线预览**：`https://你的域名`（部署到 Cloudflare Pages 后替换）

## ✨ 核心特性

- **双时间维度**：支持一键切换「近 7 天飙升」与「近 30 天飙升」榜单。
- **即时检索过滤**：支持按编程语言筛选，以及按项目名、简介、Topic 标签实时搜索。
- **纯原生零依赖**：抓取脚本仅使用 Python 标准库，前端采用原生 HTML/CSS/JS，无需构建打包。
- **零成本全自动**：通过 GitHub Actions 每日定时抓取数据，Cloudflare Pages 自动触发部署，不占用个人服务器内存与带宽。

## 🛠️ 工作原理

```text
GitHub Actions (每日 UTC 00:00 / 北京时间 08:00 定时运行)
   │
   ▼  调用 GitHub Search API
fetch.py ──▶ 生成/更新 data.json ──▶ 自动 Commit 推送回仓库
                                           │
                                           ▼  监听仓库变动自动发布
                                    Cloudflare Pages ──▶ 自定义域名访问
