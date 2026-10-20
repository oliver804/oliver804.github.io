# Research — 环境、仓库与真实素材核实

调查日期：2026-10-20
调查者：设计/开发执行方（本机操作 + GitHub 公开数据 + 站点 HTTP 探测）

---

## 1. 本机环境

| 项目 | 实测结果 | 影响 |
| --- | --- | --- |
| 工作目录 | 本次项目目录（绝对路径不外写） | 空目录，**不是 git 仓库** |
| git | 2.54.0 (Apple Git-157) | 可用 |
| node | v22.22.2 | 静态站点用不到，不引入构建链 |
| python | 3.13.12 | 仅用于本地校验脚本 |
| GitHub CLI (`gh`) | **未安装** | 无法用 `gh` 建仓/查私有仓 |
| SSH 私钥 | `~/.ssh/id_rsa` 存在（`ssh-rsa 4096`） | 存在，但未被 GitHub 接受 |
| `ssh -T git@github.com` | **`Permission denied (publickey)`** | 该公钥当前未被 GitHub 接受 |
| ssh-agent | `The agent has no identities` | 未加载 |
| `~/.ssh/config` | 不存在 | 无 Host 规则 |
| Keychain 中 github.com 凭据 | 未找到 | 无 HTTPS 免密凭据 |

**结论（重要）**：题述"已配置 SSH Key，可直接访问自己的 GitHub 仓库"在本机不成立。当前无法 clone 私有仓库、无法 push。
处理方式见 `docs/design-plan.md` 的「上线前置条件」。站点代码可以在本地完整做完并跑起来，只差最后的 push。

---

## 2. 仓库现状

### 2.1 个人站仓库 `oliver804.github.io`

- `https://oliver804.github.io/` → **HTTP 404**
- `https://api.github.com/users/oliver804/repos` 只返回 1 个公开仓库，其中不含 `oliver804.github.io`
- `git ls-remote https://github.com/oliver804/oliver804.github.io` 要求输入用户名（GitHub 对不存在或私有仓库的典型响应）

**判定**：该仓库当前不存在，或存在但为私有。不存在需要抢救的旧博客、旧文章、旧图片、CNAME。
**对开发的影响**：无迁移风险，可以从零搭建；但仍需在 push 前确认一次私有仓可能性，避免覆盖。

### 2.2 开源项目 `ChatGPT-Proxy-Launcher`

- 公开仓库，默认分支 `main`，HEAD `577a235`，体积 2137 KB
- 11 stars / 0 forks / 1 open issue，MIT License
- 语言构成（GitHub Linguist）：Swift 76.8 KB、C# 50.0 KB、HTML 34.8 KB、Python 18.5 KB、CSS 15.9 KB、Shell 7.2 KB、PowerShell 5.5 KB、Inno Setup 1.7 KB、JavaScript 0.85 KB、Makefile 0.5 KB
- 最新版本 **v1.2.0**，发布于 2026-10-19T08:34Z
  - `Local-Route-Launcher-1.2.0-arm64.dmg`（2.1 MB）
  - `Local-Route-Launcher-1.2.0-windows-x64-setup.exe`（53.8 MB）
  - 源码 zip、`SHA256SUMS.txt`
- Pages 由 `.github/workflows/pages.yml` 从 `site/**` 发布
- 站点：`https://oliver804.github.io/ChatGPT-Proxy-Launcher/` → 200；英文版 `/en/` → 200
- 仓库 `homepage` 字段指向 `https://oliai.eu.cc` → **当前 404**（域名侧问题，不由本任务处理）

---

## 3. 项目事实清单（只写可验证的部分）

以下每条都能在仓库文件中找到依据，站点文案只允许使用这一层事实。

**定位**（README.en.md）
> 保存本机 HTTP 代理设置，并在启动时把设置传给兼容的 Electron 版 ChatGPT 客户端。使用使用者已有的代理，自身不提供网络访问或代理服务。

**为什么存在**（README / USAGE.en.md / ARCHITECTURE.en.md）
- 使用应用支持的启动参数与环境变量，**不修改系统代理、不修改 DNS**，无需开启 TUN
- 只为单个进程设置代理，而不是给整台机器加一层

**实现方式**（ARCHITECTURE.en.md）
- Chromium 的 `--proxy-server` + `HTTP_PROXY` / `HTTPS_PROXY` / `ALL_PROXY`
- localhost 走直连，避免本机工具被绕进代理
- 通过 Launch Services 启动，请求应用优雅退出而非强杀
- 用户输入作为独立进程参数传递，不做 shell 插值

**功能**（README.en.md）
- 保存 host/port；启动与停止；菜单栏 / 系统托盘
- 三项连接检查：代理连通性（CONNECT 隧道 + TLS 响应）、启动参数是否携带当前设置、观察到的主进程 TCP 连接
- 浅色 / 深色外观，中英文即时切换并记忆

**平台与限制**
- macOS 13+ / Apple Silicon（ad-hoc 签名，未 notarize）；Windows 10 22H2 / 11 x64（未 Authenticode 签名）
- Windows ARM64、Intel Mac、旧版原生 ChatGPT 不在支持范围
- 语音、WebRTC、UDP、忽略环境变量的子进程不保证走代理；诊断是快照，不是"全量走代理"的证明

**命名注意**
- 公开应用名已改为 **Local Route Launcher**，仓库 URL 与偏好设置域名为兼容旧链接而保留。站点上必须用新名字，链接用旧路径。

**真实图像素材**（可直接使用，非虚构）
- `docs/images/preview-dark.en.png` 1440×1600、`preview-light.en.png`
- `docs/images/windows-dark.en.png` 747×1024、`windows-light.en.png`
- 图注已声明：macOS 版用示例诊断数据渲染；Windows 版为默认设置下渲染，无账号数据

---

## 4. 隐私盘点

| 信息 | 状态 | 决定 |
| --- | --- | --- |
| `Oliver` | 项目 README、LICENSE、GitHub 用户名中已公开 | **可公开**，作为唯一署名 |
| GitHub 显示名（含真实姓氏） | GitHub 个人页公开 | **不使用**，只写 Oliver，避免把姓氏放进品牌 |
| `oliver804x@gmail.com` | 已在项目 README 的 Author 行公开 | 可用作联系入口（已在公域，非新增暴露）；如不愿保留可删 |
| 本机 git user.email（私人邮箱） | 私域 | **禁止出现**在站点仓库的任何文件与提交信息里 |
| 本机用户目录绝对路径 | 本机 | **禁止出现**在 HTML/CSS/构建产物/提交里 |
| SSH 公钥注释中的私人邮箱 | 私域 | **禁止出现** |
| 雇主/职位/团队/城市/年龄 | 未获取 | 一律不写 |
| `oliai.eu.cc` 域名 | 项目 homepage 字段 | 不改动，个人站也不指向它 |

GitHub 个人页当前 bio、company、location、blog 均为空，贡献图仅显示 21 次/年、集中在单一仓库。**不要**在 About 页写"多年经验""服务过 X 个用户"这类无法验证的话。

---

## 5. 参考站点（逐个实测 HTTP 状态）

| 站点 | 状态 | 值得借鉴的点 | 不要照搬 |
| --- | --- | --- | --- |
| jvns.ca | 200 | 内容密度可以很高而不乱；标题直白；阅读体验优先于装饰 | 配色与手绘风属于作者个人，不宜复制 |
| danluu.com | 200 | 极端克制的排版证明"内容即设计"；纯文本也能建立权威感 | 无任何视觉层级，不适合品牌首页 |
| simonwillison.net | 200 | 项目 + 长文 + 链接博客三者共存的信息架构；按主题归档 | 结构偏"聚合器"，个人辨识度靠作者本人 |
| fabiensanglard.net | 200 | 用真实截图/实物图建立可信度；技术细节本身就是卖点 | 视觉风格偏复古个人站 |
| thesephist.com | 200 | 首页把"在做什么"写成连续叙述而不是卡片列表 | 动效与自研工具链成本高 |
| maggieappleton.com | 200 | 手记/花园式内容的组织方式；命名与栏目有统一隐喻 | 插画依赖，非工程向 |
| rsms.me | 200 | 字体与排版的极致控制；极简但辨识度极高 | 需要自研字体，成本不可复制 |
| leerob.com | 200 | 现代个人站的信息密度与速度控制 | 接近"开发者模板"的主流审美，正是要避开的那类 |
| arp242.net | 200 | 文章列表的克制排版；观点鲜明 | 视觉近乎无设计 |
| bartwronski.com | 200 | 技术长文 + 图片 + 公式的混排节奏 | 偏博客，弱品牌首页 |

**横向结论**：真正有辨识度的个人站，辨识度来自①排版控制力 ②内容真实性 ③一个贯穿全站的隐喻。来自装饰的辨识度极少能维持三年以上。

---

## 6. Gemini 咨询：无法完成，且不伪造

用户要求"必须实际完成咨询并保存真实回答"。实测：

- 本机无 `gemini` CLI（`which gemini` → not found）
- 无 `~/.gemini` 配置目录
- 环境变量中无 `GEMINI_API_KEY` / `GOOGLE_API_KEY`
- 本会话未提供可操作浏览器的会话（无 Google 账号登录态，无法访问 gemini.google.com 对话界面）

**因此没有、也不会有"Gemini 的回答"。** 任何署名 Gemini 的文字都会是伪造，与任务第九节"不得伪造"直接冲突。

替代方案：由本执行方（设计方向）给出同等结构的七问七答，明确标注为**非 Gemini 意见**，见 `docs/design-plan.md` 第 2 节。用户可自行把同一组问题发给 Gemini，把真实回答贴回来，我再做一次交叉比对并调整方案——这一步不影响现在先把站点做出来。

---

## 7. 待用户确认项（汇总）

1. **推送凭据**：公钥未授权，需要把 `~/.ssh/id_rsa.pub` 加到 GitHub，或提供 PAT。否则只能本地交付。
2. **品牌名**：推荐 `Oliver's Lab`（评估见设计文档第 1 节）。备选裸签名 `oliver804`。
3. **联系邮箱**：是否在页脚保留 `oliver804x@gmail.com`（该地址已在项目 README 公开）。
4. **第一篇笔记**：现有文稿由本次执行根据项目文档撰写，发布前建议你改写一遍或保留"drafted with AI assistance"说明。
5. **是否要 Gemini 复核**：如需要，请把真实回答贴回；不需要则按本方案执行。
