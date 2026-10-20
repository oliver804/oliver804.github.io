# Design Plan — Oliver's Lab

## 1. 品牌与命名

### 1.1 定位（一句话）

> 一个把软件真正做完、做完之后还能维护的工程师，在这里留下项目和笔记。

不是求职简历，不是 AI 新闻站，不是"独立开发者成功故事"。证据只有一个：一个真实开源项目 + 它带来的判断力。

### 1.2 命名评估

| 候选 | 表达力 | 长期性 | 风险 |
| --- | --- | --- | --- |
| **Oliver's Lab** | 实验 + 记录，天然包含"笔记"栏目 | 高：只要还在做项目就成立 | "Lab"在 AI 初创语境里被用滥，容易被读成公司名 |
| Oliver's Workshop | 手工、打磨、耐看 | 中：偏重"制作"，弱于"研究" | "Workshop"常被理解为工作坊/教程 |
| Oliver's Projects | 零歧义 | 低：一旦写字就名不副实 | 纯描述，毫无记忆点 |
| `oliver804`（裸签名） | 与 GitHub 完全一致，零解释成本 | 最高 | 缺一个人格化的入口，首页会显得像仓库主页 |

**选择：`Oliver's Lab`。**

关键不在名字，而在**怎么用这个名字**：把 "Lab" 按**实验室日志**的方式做出来，而不是按"AI 创业公司"的方式做出来。手段是排版隐喻——页眉像刊物刊头、栏目标号、图注编号（Fig. 1）、边缘栏（margin rail）放元信息、页脚留 colophon（版本说明）。这样 "Lab" 读起来是"工作记录本"，而不是"品牌"。这也是它与常见模板最直接的差别。

如果日后想彻底去掉这一层包装，只需要改 `<title>`、页眉一处文字、README 一处，共 3 处。

### 1.3 公开文案定稿（英文）

**Eyebrow（页眉上方，等宽小字）**
`Software engineering · Data · AI-assisted development`

**H1**
> Software that holds up after launch.

选它的理由：不说"我是谁"（那是最容易空洞的位置），而是表明一条工程立场。它与"重视实际问题、关注部署与维护"的背景直接对应，且不能被任何模板复用。

**Deck（首屏副文）**
> I'm Oliver. I work on Java services, data platforms and front-end code — the parts that have to keep running after launch: data that must stay correct, systems someone else has to operate, small tools that remove a repeated annoyance. One of them is open source, and it's documented below.

三层结构齐备：①身份 ②方向（Java 服务 / 数据 / 前端）③出口（项目与笔记）。没有"passionate""10x""building the future"。

**项目简述**
> A native macOS and Windows launcher that gives a compatible ChatGPT desktop app its own HTTP proxy — without turning on TUN, changing the system proxy, or touching DNS.

**About 首段**
> This site is a working record, not a portfolio. I keep the projects I finish and the notes I take while building them — including the parts that didn't work.

---

## 2. 七问七答（**非 Gemini 意见**，执行方判断）

> 声明：本机会话无 Gemini 接入，无法实际咨询，也不会代写它的回答（见 `docs/research.md` 第 6 节）。以下为设计执行方的同等分析；如需外部第二意见，请把真实回答贴回，我据此调整。

**Q1 哪种风格最能表达工程师的专业性和产品意识？**
"可被检验的克制"。工程师的专业感来自信息的准确与结构的清晰，不是来自科技感。产品意识来自**一个真实产品被讲清楚了**——包括限制和边界。因此风格应当是：信息密度偏高、层级少、无装饰噪声、所有视觉元素都能被解释（为什么这里有线、为什么这里编号）。

**Q2 不用大量装饰，如何建立辨识度？**
三个低成本杠杆：①**字体组合**——衬线标题 + 系统无衬线正文 + 等宽元信息，这套组合在开发者作品集里罕见（大家都用 Inter + JetBrains Mono）。②**一条竖线**——正文左侧的栏距线贯穿全站，形成"实验记录本"的物理暗示，零装饰成本。③**编号系统**——栏目 01/02/03、图注 Fig. 1/2，让页面像被整理过，而不是被堆叠过。

**Q3 首页先展示介绍、项目还是文章？**
介绍（3 行）→ **项目**（占最大面积）→ 方向 → 笔记。理由：这个品牌目前只有一件证据，证据必须在前两屏内出现。文章不能放前面，因为没有存量内容，会把用户带到空列表。

**Q4 如何平衡技术深度、产品展示与个人品牌？**
三者不并列，而是**一条链**：品牌是一句话（H1），产品是证据（项目块），深度是细节（规格表、限制说明、笔记）。深度不放在首页正文里，而是放在"可点击进去的地方"。首页只负责让人产生"这个人写的东西值得点开"的判断。

**Q5 哪些设计容易显得像 AI 自动生成的？**
按出现频率排：紫蓝渐变；三层发光；全站 16px 圆角白卡 + 阴影；emoji 当图标；"Hi, I'm X 👋"；Skills 进度条；假数据（"50+ 项目""10k 用户"）；每屏一个居中的大标题 + 副标题 + 两个按钮；滚动渐显动画；大段"passionate about"；机器人/神经网络装饰；Inter 字体 + 深色背景 + 网格光晕。本方案逐条规避，见第 6 节检查表。

**Q6 真实存在的优秀个人站？**
见 `docs/research.md` 第 5 节（10 个站点，全部实测 200）。共性结论：辨识度来自排版控制力、内容真实性和一个贯穿全站的隐喻，而不是视觉特效。

**Q7 如何形成可长期扩展的设计系统？**
用"文档系统"而非"组件库"扩展：新页面 = 新的 `<section>` + 已有的 rail / 规格表 / 图注 / 行列表 4 个模式。不新增视觉语言，只新增内容。CSS 单一文件 + 语义类名，不引入框架、不引入构建步骤——五年后仍能直接改。

---

## 3. 两个设计方向

### 方向 A — Lab Notebook（**推荐并已实现**）

| 维度 | 方案 |
| --- | --- |
| 品牌表达 | 实验室日志。页眉是刊头，章节有编号，图有编号，页脚是 colophon |
| 首页布局 | 单栏 + 左侧 132px 边缘栏；首屏文字左对齐、不满宽；项目块用整幅截图做图版 |
| 字体 | 标题 Newsreader（衬线，自托管，含斜体）；正文系统无衬线；元信息系统等宽 |
| 颜色 | 纸白 `#FAF8F3`、墨 `#191B16`、次级 `#5F6457`、分隔线 `#DAD5C7`、主色松绿 `#1D5940` |
| 项目展示 | 规格表（datasheet 风格）+ 双平台真实截图 + 图注 + 明确的三个出口（详情/源码/下载） |
| 笔记与 About | 笔记按"日期 / 标题 / 摘要"三栏行列表；About 用第一人称连续段落，不用小节标题堆砌 |
| 个人特色 | 编号与栏距线构成的"整理感"；对限制的坦率描述 |
| 避免 AI 感 | 无卡片、无阴影、无渐变、无 emoji 图标、无动画 |
| 隐私风险 | 低：所有内容来自公开仓库 |
| 维护成本 | 极低：无构建、无依赖、无 JS；新增一篇笔记 = 复制一个目录 |

### 方向 B — Instrument（备选，未实现）

| 维度 | 方案 |
| --- | --- |
| 品牌表达 | 精密仪器面板。深色、发丝线、全大写标签、密集数据 |
| 首页布局 | 12 栏网格，左右两栏并置：左侧身份与索引，右侧实时状态与项目表 |
| 字体 | 全无衬线（紧凑 grotesque）+ 等宽；标题靠字重与字距区分 |
| 颜色 | 近黑 `#0B0C0B`、发丝线 `#26282A`、单一强调色（琥珀或青） |
| 项目展示 | 表格化，等宽数字，行内展开 |
| 笔记 | 密集索引，像 changelog |
| 个人特色 | 强，但容易与"深色开发者站"混同 |
| 避免 AI 感 | 靠密度与精度，而不是靠缺省 |
| 隐私风险 | 低 |
| 维护成本 | 中：深色模式下的图片、代码块、长文阅读体验都要单独调 |

### 为什么选 A 而不是 B

1. **与已有资产的差异化**：项目官网是浅薄荷绿 + 22px 圆角卡片的营销页面。个人站如果也走"深色科技"或"卡片网格"，要么撞车，要么显得像同一个模板的换色版。A 的纸感 + 硬角与项目官网形成"同一家族、不同语域"，绿系主色做了血缘连接。
2. **长文友好**：这个站的长期价值在笔记。浅纸底 + 衬线 + 66ch 行宽，是十年后仍然舒服的组合；深色密集面板适合浏览，不适合阅读。
3. **抗过时**：纸与墨不会过期，霓虹会。
4. **成本**：A 无构建、无 JS、无深色模式分支，一个人可以维护到不想维护为止。

---

## 4. 设计系统

### 颜色（全部为 WCAG AA 以上组合）

| Token | 值 | 用途 | 对比度 |
| --- | --- | --- | --- |
| `--paper` | `#FAF8F3` | 页面底色 | — |
| `--paper-2` | `#F3F0E7` | 图版底、代码块 | — |
| `--ink` | `#191B16` | 正文、标题 | 14.8:1 on paper |
| `--ink-2` | `#5F6457` | 次级文字、图注 | 5.9:1 |
| `--ink-3` | `#6E7264` | 栏目标号、图注前缀、日期等小字 | 4.65:1 |
| `--rule` | `#DAD5C7` | 分隔线 | 非文字元素 |
| `--rule-2` | `#B9B4A4` | 强调分隔、下划线 | — |
| `--pine` | `#1D5940` | 链接、当前项、焦点环 | 7.2:1 |

无渐变、无阴影、无半透明叠加。

对比度已按 WCAG 2.1 实测（非估算）：正文 16.36:1、次级文字 5.74:1、小号等宽标签 4.65:1、主色 7.74:1，全部达到 AA；正文与标题达到 AAA。最初选用的 `#8A8F80` 只有 3.13:1，作为 11px 标签不合格，已改为 `#6E7264`。

### 字体与尺度

| 角色 | 字体 | 尺寸 |
| --- | --- | --- |
| Display H1 | Newsreader 400 | `clamp(2.6rem, 6.4vw, 4.5rem)` / 0.98 |
| H2 章节 | Newsreader 400 | `clamp(1.75rem, 3.2vw, 2.5rem)` |
| H3 条目标题 | Newsreader 400 | `clamp(1.25rem, 2vw, 1.6rem)` |
| 正文 | system-ui 栈 | `1.0625rem` / 1.66，最大 `66ch` |
| Lede | system-ui | `clamp(1.1rem, 1.5vw, 1.3rem)` / 1.55 |
| Meta / 标签 | 等宽栈 | `0.6875rem`，大写，`letter-spacing .13em` |
| 规格表值 | 等宽栈 | `0.875rem` |

等宽栈：`ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace`。
正文栈：`-apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif`。

### 栅格与节奏

- 容器 `1120px`，左右留白 `clamp(20px, 5.4vw, 72px)`
- `≥ 900px` 时启用边缘栏：`132px | 1fr`，栏右侧 1px 竖线
- 垂直节奏：章节间距 `clamp(64px, 9vw, 120px)`；条目间距 22–28px
- 圆角统一为 `0`（图版 `2px`），阴影全站为 0
- 断点：`900px`（栏折叠）、`700px`（图版上下堆叠、表格转两行）

### 四个可复用模式

1. `railrow` —— 左栏标签 + 右栏内容
2. `spec` —— 规格表（dt 等宽小字 / dd 内容，行间发丝线）
3. `fig` —— 图版 + 编号图注
4. `rows` —— 行列表（替代卡片网格）

新增页面只允许复用这四个模式。

---

## 5. 信息架构与 URL

```
/                                         Home
/projects/                                Projects 索引（当前 1 个，另一个标注 in progress 前先不写）
/projects/local-route-launcher/           项目详情
/notes/                                   笔记索引
/notes/why-the-launcher-drives-the-app/   第一篇笔记
/about/                                   About
/404.html                                 404
/robots.txt  /sitemap.xml  /feed.xml  /.nojekyll
```

- 目录式 URL，静态托管天然支持，永久稳定，可被索引
- 每个页面有独立 `<title>` / description / canonical / OG
- 不设主题切换：纸感是身份的一部分，深色分支会让这套系统变成两套要维护的东西。`color-scheme: light` 显式声明，避免浏览器强制反色
- 不设隐私政策页：全站无分析、无 cookie、无第三方请求（字体自托管），页脚一行 colophon 说明即可
- 提供 RSS：长期读者（含自己）需要，成本是一个手写 XML

---

## 6. 反模板检查表（逐条对应任务要求）

| 要求规避 | 本方案 |
| --- | --- |
| 紫蓝渐变 / 发光 | 无渐变、无 shadow、无 filter |
| 玻璃拟态 + 大量圆角卡 | 全站 0 圆角、无卡片、无 backdrop-filter |
| 机器人 / 芯片 / 神经网络装饰 | 无任何插画与图标，唯一的图形是 1px 线 |
| 巨大口号 + 空首屏 | 首屏第一段就是可验证的具体描述，第二屏就是项目 |
| 过度动画 / 视差 / 跟随鼠标 | 0 动画（仅链接下划线的 120ms 颜色过渡），无 JS |
| 虚构统计与评价 | 全站唯一数字来自 release：v1.2.0、2026-10-19 |
| 每区块同构 | 首页四种节奏：散文化首屏 → 图版 + 规格表 → 行列表 → 三栏行列表 |
| 过度营销英文 | 无形容词堆叠；限制与失败处照写 |
| 牺牲可读性换高级感 | 正文 17px / 1.66，行宽 66ch，对比度全部 AA+ |

---

## 7. 技术选型

| 选项 | 决定 | 理由 |
| --- | --- | --- |
| 静态 HTML/CSS | ✅ | 6 个页面，无需构建，五年后可维护 |
| Astro + Markdown | ❌（现阶段） | 文章数为 1。等内容到 10 篇以上再迁移，迁移成本低（页面结构已经是模板化的） |
| React / 框架 | ❌ | 无交互需求，纯负担 |
| JavaScript | ❌ 0 字节 | 导航只有 4 个链接，不需要汉堡菜单 |
| 字体 | 自托管 2 个 woff2（Newsreader roman/italic，latin 子集，共 273 KB） | 无第三方请求、无 FOUT 抖动、无隐私外泄 |
| 图片 | 真实截图 PNG，长边压到 1100/760 | 有 `width/height`、`loading="lazy"`、`decoding="async"` |
| 分析 | 无 | 与项目官网的 GA 明确区分；个人站不采集 |
| 部署 | GitHub Pages，`main` 分支根目录 | 用户站仓库 `oliver804.github.io`，与项目仓库完全独立 |

---

## 8. 上线前置条件（阻塞项）

1. ~~SSH 公钥未被 GitHub 接受~~ → 已解决，`ssh -T git@github.com` 返回 `Hi oliver804!`。
2. **仓库尚不存在** → `oliver804.github.io` 远端仍是 404。推送前需要先在 GitHub 上建空仓库（不勾 README / .gitignore / license），否则 `git push` 会报 `Repository not found`。绝不对已有内容 `push --force`。
3. **发布后校验** → 推送后等 Pages 构建，实测 `/`、`/projects/`、`/projects/local-route-launcher/`、`/writing/`、`/writing/one-behaviour-two-builds/`、`/404.html` 的 200 与内容，再确认项目站 `/ChatGPT-Proxy-Launcher/` 未被影响（两个仓库互不影响，但仍需实测）。

---

## 9. 后续扩展操作（写给自己）

- **加一个项目**：复制 `projects/local-route-launcher/index.html` → 改标题、规格表、图注 → 在 `projects/index.html` 和首页 `#work` 增加一条 → `sitemap.xml` 加一行。
- **加一篇笔记**：复制 `writing/one-behaviour-two-builds/index.html` → 改 `<title>`/描述/日期/主题/正文 → 在 `writing/index.html` 顶部加一行并更新主题计数 → 首页三篇列表换一篇 → `sitemap.xml` 与 `feed.xml` 各加一条 → 把上一篇的 *Read next* 指过来。完整步骤见 `README.md`。
- **改名**：`assets/css/style.css` 不需要动；改每页 `.brand-name`、`<title>` 后缀、`README.md`。

---

## 10. 定位修正（第二轮）

第一轮交付后复核定位，结论是**部分符合**"个人技术品牌 + 开源项目展示 + 技术博客"的组合目标，但三根支柱的配重失衡：

| 问题 | 表现 | 处理 |
| --- | --- | --- |
| 博客只有 1 篇 | `/notes/` 更像"给项目页配的说明"，不像可长期积累的栏目；没有分类，也没有主题体系 | 栏目改为 `Writing`（URL 同步改为 `/writing/`），补 3 篇基于公开仓库事实的长文，建立 5 个主题的分类和计数，未写的两个主题明确标为 Planned |
| 项目展示只有一条入口 | 首页与项目页都在讲同一个项目，没有"开源工作面"的整体观感 | 项目页拆成 Public / Facts / In progress 三段，加入第二个真实仓库（本站源码），事实表列出发布、语言、许可证、分发方式、测试 |
| 首页偏"长篇随笔" | 首屏之后是一段产品长文，写作与技术方向被压在最后 | 段落顺序改为 01 序 / 02 Selected work / 03 Writing / 04 Focus，写作升到项目之后 |
| 项目页与文章不互链 | 读完项目页没有下一步，读完文章也回不到项目 | 项目页加"Notes about this project"列表；每篇文章底部加 *Read next* 与"这一组笔记来自哪个项目" |

没有为此编造第二个产品或虚构文章主题：新增的第二个仓库就是本站源码，四篇文章的事实全部来自 `ChatGPT-Proxy-Launcher` 的 README、CHANGELOG、RELEASE_NOTES、ARCHITECTURE、构建与测试脚本。Data engineering 与 AI-assisted development 两个主题保持 Planned 状态，等有草稿再上线。

公开邮箱 `oliver804x@gmail.com` 按你的决定保留，它已经出现在项目 README 与 LICENSE 中，也与项目自带 `scripts/privacy-check.py` 的 `APPROVED_EMAIL` 白名单一致。

---

## 11. 定位修正（第三轮）：从"个人刊物"改为"工作记录"

第三轮反馈：**"风格太像博客，而我很少写博客"**。复核后结论是：内容没问题，**结构错了**。

### 11.1 诊断

旧版把"个人技术品牌 + 开源项目展示 + 技术博客"三件事做成了三个等重的栏目，还给整页加了 01–04 编号和统一留白。这个做法的隐含承诺是"这里是按期连载的刊物"，而实际更新节律是"项目完成时才更新"。

命中 2026 年"AI 模板感"审计表的条目（详见 `docs/research-personal-sites.md` 第 2 节）：

- 每个标题上方一条全大写等宽 eyebrow
- 给不是序列的内容编 01 / 02 / 03
- 每个区块相同的上下留白

三条叠加，就是"杂志/博客"的观感来源；与配色和字体无关。

### 11.2 结构变化

| | 旧 | 新 |
| --- | --- | --- |
| 首页段落 | 01 Index / 02 Selected work / 03 Writing / 04 Focus | 开场（短）→ Work → Notes → 页脚 title block |
| 首屏 | 巨型标题 + 三个链接按钮 | 一句话立场 + 两段自述 + 状态行 |
| 项目 | 一个精选项目 + 一段长文 | 两个真实仓库，各自：编号、名称、数据行、两段、三个出口、一张图 |
| 写作 | 三条摘要 + 阅读时长 + 分类 | 四条一行式链接，只有标题和日期 |
| 重点 | 三个栏目等重 | 作品占全页约 60%，笔记约 12% |

字号层级也反过来了：**作品名是全站最大的字**（2.7rem），姓名退到页眉（1.2rem）。排版层级即优先级声明。

### 11.3 视觉变化

- 纸色 `#FAF8F3` → `#F2F0E9`（灰纸，不是奶油纸）
- 强调色 松绿 `#1D5940` → 标注红 `#9B3A25`（只用于链接下划线、图号、状态词）
- 圆角 2px → 0；去掉了所有"柔和"处理
- 新增页脚 **title block**（File / Set / Build / Edited），借工程图纸的图签：既是个人化元素，也把"没有构建步骤、最后编辑日期"写进版面
- 字体不变：Newsreader 是唯一已经建立的识别度，模板感来自结构和配色，不来自标题衬线

对比度实测：ink 15.6:1、ink-2 7.0:1、ink-3 5.1:1、标注红 6.1:1，均过 WCAG AA。

### 11.4 保护旧站与内容

- 改版前打了标签 `pre-project-first`，可整体回滚：`git checkout pre-project-first -- .`
- 四篇笔记的正文**一字未改**，仅重写外壳（由脚本抽取 `article-body` 原样嵌入，避免手抄误差）
- 所有 URL 不变：`/projects/`、`/projects/local-route-launcher/`、`/writing/*`、`/about/` 全部保留，已收录的外部链接不会断
- 四个搜索引擎验证文件、`sitemap.xml`、`feed.xml`、`robots.txt` 未动

### 11.5 明确没做的

- 不加 `/now` 页：多一个会陈旧的页面
- 不加暗色模式：多一个需要维护的状态
- 不加"最近更新"组件或任何 JavaScript
- 不编造第三个项目来填版式；"In progress" 段继续空着并说明原因

---

## 12. 统计代码（第四轮）：一次被记录的倒退

要求：装上 Google Analytics 4 与 Microsoft Clarity。

这与本站此前公开声明的一条原则直接冲突——`about` 页原本写着 "no JavaScript,
no analytics, no cookies, and no third-party requests"。站点本身的价值恰恰建立在
"这些句子都可验证" 上，所以处理方式不是把那句话悄悄删掉。

### 12.1 做法

- 两段代码原样放在 10 个页面的 `</head>` 之前，`async` 加载，不阻塞渲染。
- 三个此前声明"无统计"的位置全部改写，不是删除：
  - 首页 "This site" 条目
  - `/projects/` 的 "This site" 条目
  - `about` 的 Colophon 段与每页页脚的 colophon 行
- 页脚图签的 `Build` 值从 "None — hand-written, no JavaScript" 改为
  "None — hand-written, no framework"（仍为真）。
- `about` 新增 `#analytics` 一节，写清：跑的是哪两个、由谁提供、会记录什么、
  以及为什么这一页此前说过相反的话。`head` 里的注释指向该锚点。

### 12.2 验证

本地 headless 实测：`gtag/js` 200、GA4 `g/collect` 204、`clarity.ms/tag` 200、
`scripts.clarity.ms/clarity.js` 200；`window.dataLayer` 4 条、`gtag` 与 `clarity`
均为函数；cookie `_ga`、`_ga_472VKF5Y95`、`_clck` 均已写入；无页面报错。

### 12.3 已知代价与未做的

- **性能**：第三方脚本约 150 KB，`async` 不阻塞首屏，但会进入 TBT。这是这次
  改动的实测代价，不是猜测。
- **合规**：GA4 与 Clarity 默认在首次访问即写 cookie，欧盟/英国访客需要先取得
  同意。本站没有同意横幅。要么接受现状（个人站、低流量），要么加一个需要 JS
  的横幅——后者与"页面不依赖脚本"的原则冲突。当前选择是前者，并且写在明处。
- 未加 `preconnect`：多两个 DNS/TLS 握手换来的是几十毫秒，但会多两条第三方
  连接，收益不稳定，先不加。
