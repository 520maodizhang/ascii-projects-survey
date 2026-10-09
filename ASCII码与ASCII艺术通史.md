# ASCII 码与 ASCII 艺术通史

> 撰写日期：2026-10-10
> 本文档详细梳理 ASCII 编码的起源、演变，ASCII 艺术的历史脉络，以及与之密切相关的文字游戏、BBS/ANSI 艺术、Roguelike 游戏等领域的完整发展史。

---

## 目录

- [第一章：ASCII 编码的起源与标准化](#第一章ascii-编码的起源与标准化)
- [第二章：ASCII 编码之前的文字编码史](#第二章ascii-编码之前的文字编码史)
- [第三章：ASCII 艺术的史前史——打字机艺术](#第三章ascii-艺术的史前史打字机艺术)
- [第四章：无线电电传打字（RTTY）艺术](#第四章无线电电传打字rtty艺术)
- [第五章：计算机 ASCII 艺术的诞生（1960s–1970s）](#第五章计算机-ascii-艺术的诞生1960s1970s)
- [第六章：BBS 时代与 ANSI 艺术的黄金年代](#第六章bbs-时代与-ansi-艺术的黄金年代)
- [第七章：ASCII 艺术团体与 Artpack 文化](#第七章ascii-艺术团体与-artpack-文化)
- [第八章：FIGlet——ASCII 大字艺术的诞生](#第八章figletascii-大字艺术的诞生)
- [第九章：文字冒险游戏的起源](#第九章文字冒险游戏的起源)
- [第十章：Roguelike 游戏的诞生与演变](#第十章roguelike-游戏的诞生与演变)
- [第十一章：ASCII 艺术工具的演进史](#第十一章ascii-艺术工具的演进史)
- [第十二章：Demoscene 与 Textmode 艺术](#第十二章demoscene-与-textmode-艺术)
- [第十三章：PETSCII 与 Commodore 64 文本艺术](#第十三章petscii-与-commodore-64-文本艺术)
- [第十四章：互联网时代的 ASCII 艺术](#第十四章互联网时代的-ascii-艺术)
- [第十五章：AI 时代的 ASCII 艺术](#第十五章ai-时代的-ascii-艺术)
- [第十六章：ASCII 艺术的时间线总览](#第十六章ascii-艺术的时间线总览)
- [第十七章：关键人物名录](#第十七章关键人物名录)

---

## 第一章：ASCII 编码的起源与标准化

### 1.1 混乱的前 ASCII 时代

在 1963 年之前，计算机世界是一场编码的巴别塔。超过 **60 种**不同的字符编码方案在各家厂商的机器上使用——IBM 有 EBCDIC 和 BCD，CDC 有自己的编码，UNIVAC 也有自己的，各家互不兼容。一台 IBM 机器上写的文本传到另一台 CDC 机器上就是乱码。

这个问题严重到 **Bob Bemer**（IBM 的工程师）在 1960 年 12 月的《Communications of the ACM》上发表了一篇题为"A Proposal for Character Code Compatibility"的论文，呼吁建立一个统一的字符编码标准。这是 ASCII 故事的起点。

### 1.2 Bob Bemer——"ASCII 之父"

**Robert William Bemer**（1920–2008），昵称 Bob，是 20 世纪计算机科学最具影响力的人物之一。他在 IBM 工作期间：

- **1960 年 12 月**：在 CACM 发表提案，呼吁建立统一编码
- **1961 年 5 月**：正式向美国标准协会（ASA，后改组为 ANSI）的 X3.2 小组委员会提交提案
- 引入了 **转义字符（Escape Character，ESC）** 的概念，这一概念后来成为 ANSI 转义序列的基础，也是今天终端彩色输出、光标控制的基础
- 与英国同事 **Hugh McGregor Ross** 合作推广，在欧洲该编码一度被称为 **"Bemer–Ross Code"**

Bemer 后来被称为 **"ASCII 之父"**。他不仅推动了 ASCII 的诞生，还开发了让计算机在不同字母表之间切换的方法，催生了 150 多种"扩展 ASCII"字母表。

### 1.3 标准化历程

| 时间 | 事件 |
|------|------|
| 1960.10.06 | ASA X3.2 小组委员会首次会议，ASCII 制定工作正式启动 |
| 1961.05 | Bob Bemer 提交提案 |
| 1963.06.17 | **第一版 ASCII 标准发布**（ASA X3.4-1963），7 位编码，128 个字符，但留有 28 个未定义位置 |
| 1963.05 | CCITT 提议将小写字母放入第 6、7 列（"sticks"），使大小写仅差一个比特位，简化键盘和打印机设计 |
| 1965 | ASA X3.4-1965（已批准但未发表，IBM 2260/2265 显示终端使用） |
| 1967 | **重大修订版** USAS X3.4-1967 发布，加入小写字母 |
| 1968.03.11 | **美国总统林登·约翰逊** 签署备忘录，强制所有联邦政府计算机支持 ASCII（1969 年 7 月 1 日起生效） |
| 1968 | USAS X3.4-1968 |
| 1969 | RFC 20 描述了 ASCII 用于网络交换的格式 |
| 1977 | ANSI X3.4-1977 |
| 1981 | IBM PC 采用 ASCII 作为字符集，ASCII 终于成为 PC 标准 |
| 1986 | ANSI X3.4-1986（最终版） |
| 2015 | RFC 20 正式升格为互联网标准 |

### 1.4 ASCII 的设计哲学

ASCII 的设计体现了几个关键决策：

1. **7 位编码**：128 个字符（0–127），在当时是最小的能容纳大小写字母+数字+标点+控制字符的编码
2. **大小写仅差一位**：`A`(65) 和 `a`(97) 的二进制仅第 6 位不同，极大简化了大小写转换和键盘设计
3. **便于排序**：字母按字母表顺序排列（不像 EBCDIC 那样字母顺序混乱），方便列表排序
4. **控制字符在前**：0–31 为控制字符，32–126 为可打印字符，分离清晰
5. **转义字符**：ESC（27）为扩展提供了无限可能

### 1.5 ASCII 的第一个商业应用

ASCII 于 1963 年首次商用，作为 AT&T 的 **TWX（TeletypeWriter eXchange）** 网络的 7 位电传打字机编码。TWX 原先使用 5 位 ITA2 编码（与 Telex 竞争系统相同）。

最影响 ASCII 字符解释的单一设备是 **ASR-33 Teletype**（1963 年发布），它定义了 Ctrl-Q（XON）、Ctrl-S（XOFF）等事实标准，这些控制码至今仍在使用。

### 1.6 ASCII 的对手——EBCDIC

1964 年，IBM 发布了划时代的 **System/360**，但开发团队负责人 Frederick Brooks 决定使用 **EBCDIC**（8 位编码，256 字符）而非 ASCII——因为当时的穿孔卡片和打印机还不支持 ASCII。这导致 ASCII 花了 **18 年**才在 IBM PC（1981）上成为标准。EBCDIC 至今仍在某些 IBM 大型机上使用。

---

## 第二章：ASCII 编码之前的文字编码史

### 2.1 摩尔斯码（1844）

Samuel Morse 发明的电报编码，用点和划表示字母。这是最早的"字符编码"概念，但不是数字编码。

### 2.2 Baudot 码（1870）

Émile Baudot 发明的 5 位编码，32 个字符。使用 ITA2 国际标准版本。不支持小写字母，只有大写字母、数字和少量标点。是 RTTY（无线电电传打字）的标准编码，直到 1980 年 FCC 才授权美国业余无线电操作员使用 ASCII。

### 2.3 IBM BCD / EBCDIC（1962）

IBM 的 6 位 BCD 和 8 位 EBCDIC 编码。EBCDIC 是 ASCII 最大的竞争对手，最终在 PC 市场败给 ASCII，但在大型机领域存活至今。

### 2.4 编码统一的必要性

到 1960 年，超过 60 种编码并存。Bemer 在 1960 年的调查中记录了这一混乱局面，这是推动 ASCII 诞生的直接动力。

---

## 第三章：ASCII 艺术的史前史——打字机艺术

### 3.1 打字机的发明（1867）

1867 年，Christopher Latham Sholes 发明了实用打字机。人们很快发现，打字机不仅能打印文稿，还能创作视觉艺术。

### 3.2 最早的打字机艺术（1898）

**目前已知最早的打字机艺术作品**由一位名叫 **Flora Stacey** 的女性于 **1898 年**创作。她可能是一位秘书。她的作品——一只用键盘字符拼成的蝴蝶——发表在 1898 年 10 月 15 日的 *Pitman's Phonetic Journal* 上。

### 3.3 打字机艺术的黄金年代（1950s–1970s）

打字机艺术在 1950–1970 年代成为一种流行的艺术媒介。**Alan Riddell** 的书 *Typewriter Art*（伦敦，1975）收录了 100+ 件作品，来自 60 多位打字机艺术家，包括：

- 肖像作品：伊丽莎白女王、爱丁堡公爵、甘地、丘吉尔、Henri Chopin
- 抽象作品
- 彩色作品（使用着色色带）

值得注意的是，**Vaclav Havel**（捷克共和国总统）也是打字机艺术家之一。

### 3.4 打字机艺术与 ASCII 艺术的关键区别

打字机艺术没有存储介质——成品就是纸上的图片。而 ASCII 艺术有根本不同：
- 可以存储在穿孔纸带、穿孔卡片上
- 可以通过电子网络传输
- 可以被程序处理和变换
- 可以被精确复制和分发

---

## 第四章：无线电电传打字（RTTY）艺术

### 4.1 电传打字机的发明（1900s）

电传打字机（teleprinter / teletypewriter）发明于 20 世纪初。美国最大的制造商是 **Teletype Corporation**（AT&T 子公司）。"teletype"一词实际上是 AT&T Teletype Corporation 的商标。

二战后， surplus 电传打字机以低价流入民间，业余无线电操作员（ham）开始使用它们进行数字通信。

### 4.2 RTTY 艺术的最早记录（1923）

根据 *RTTY Handbook* 的记载，**文字图片通过电传打字机发送的最早记录可追溯到 1923 年**。然而，由于早期纸带不耐酸、会随时间黄化，目前尚未发现任何 1923 年的 RTTY 艺术实物。

### 4.3 RTTY 艺术的繁荣（1960s–1970s）

已知的 RTTY 文字图片在 **1960 年代和 1970 年代**频繁出现在无线电电传打字中。这些图片由业余无线电操作员（ham）通过无线电传输互相发送。

关键特点：
- 使用 **5 位 Baudot 码**，而非 ASCII（ASCII 直到 1968 年才标准化）
- 只有大写字母、数字和少量标点
- 传输速度极慢：45 波特（约 60–100 WPM），一张大型 RTTY 艺术图片可能需要 **一小时** 传输
- 存储在穿孔纸带上
- 早期有关于 RTTY 艺术的文章发表在 *73 Magazine*（RTTY 爱好者刊物）上

### 4.4 RTTY 与 ASCII 的交汇（1980）

1980 年 3 月，FCC 授权美国业余无线电操作员使用 ASCII（除 Baudot 码外）进行 RTTY 通信。这标志着 RTTY 艺术开始向 ASCII 艺术过渡。

### 4.5 Jefferson Computer Museum 的收藏

Jefferson Computer Museum 的 "Ancient Alphabetic Art" 项目收藏了 Ken Simpson 捐赠的一盒无线电电传打字 ASCII 艺术，展示了计算机世界与 RTTY 世界之间的交叉传播。其中一张图片是 **艾森豪威尔总统**的肖像。这些作品似乎来自 1970 年代早期。

---

## 第五章：计算机 ASCII 艺术的诞生（1960s–1970s）

### 5.1 Kenneth Knowlton 与 Bell Labs（1966）

**目前已知最早的计算机 ASCII 艺术作品**由计算机艺术先驱 **Kenneth Knowlton** 于 **1966 年**左右在 Bell Labs 创作。他与 **Leon Harmon** 合作的 "Studies in Perception I"（1966）展示了早期的 ASCII 艺术例子。

他们的方法：将照片降采样为灰度网格，每个灰度值映射到一个字符，在行式打印机上输出。

### 5.2 Computer Nude（1966）

一个著名的早期作品 **Computer Nude** 在 Bell Labs 的 IBM 7094 上制作（当时价值 200 万美元）。舞者和编舞家 Deborah Hay 的黑白照片被缩减为灰度方格，然后用电话电路图符号填充灰度值。这是最早用计算机生成的"照片级"ASCII 艺术之一。

### 5.3 Andries van Dam 与 IBM 1403（1960s）

1960 年代，**Andries van Dam** 在 IBM 1403 行式打印机上发布了一幅电子电路图。这是最早的行式打印机艺术之一。IBM 1403 使用 EBCDIC 而非 ASCII，但技术原理相同。

### 5.4 行式打印机艺术的繁荣（1970s）

1970 年代，行式打印机艺术在整个计算机界繁荣。**Kenneth Knowlton** 以在行式打印机上通过**叠印**（overprinting）多个字符来创建逼真图像而闻名。

> "Everybody learned how to print a Snoopy banner."
> ——每个在计算机实验室工作过的人都学会了打印 Snoopy 横幅。

行式打印机艺术的常见主题：
- **Snoopy**（史努比）——最流行的主题，无数变体
- **圣诞树**——计算机实验室的圣诞传统
- **Mona Lisa**——Peterson 的 "Mona by the Numbers"
- 肖像（华盛顿、林肯、杜鲁门等）

### 5.5 叠印技术（Overprinting）

1970–1980 年代流行一种依赖**叠印**的文字艺术：在打印机上输入一个字符，退格，再输入另一个字符——就像在打字机上一样。这在 **PLATO 系统**（约 1973）中发展得尤为成熟，上标和下标允许各种图形效果。一个常见用途是制作表情符号，WOBTAX 和 VICTORY 都能产生令人信服的笑脸。

叠印在打字机上已有先例，但视频终端上字符的低分辨率像素化意味着叠印在这里产生了无缝像素图形，而非可见的重叠字母组合。

### 5.6 穿孔卡片艺术的分发

ASCII 艺术通过**穿孔卡片组**在大学计算机中心的学生和工程师之间传递：

> "There were some prized card decks that got passed around for producing the art and periodically you would see an example in the computer room or someone's dorm room."
> ——一位 1970 年代中期的女工程师回忆

由于大量 ASCII 艺术具有色情性质，这些卡片组并不总是对所有人开放分享。

### 5.7 1970 年代的 ASCII 艺术商业应用

- **美国购物中心**：1970 年代，美国各大购物中心设有自动亭，用计算机将照片转为 ASCII 艺术印在 T 恤上
- **伦敦科学博物馆**：提供类似服务，打印 ASCII 肖像
- **Control Data**：将 Mona Lisa 的 ASCII 版本作为促销材料赠送给客户

### 5.8 最早的互联网 ASCII 艺术

ARPANET（1969 年开始）上的电子邮件最初是纯文本——没有图片，更没有动画。ASCII 艺术被用来创建图表和示意图，也用于"好玩"和美化纯文本邮件。

已知最早的互联网 ASCII 艺术作品包括：
- **"Spy at the Wall"** 系列
- **"Silly Cows"** 系列——David Bader 编辑的完整原版奶牛集，这些奶牛遍布互联网，被视为"经典"ASCII 艺术

---

## 第六章：BBS 时代与 ANSI 艺术的黄金年代

### 6.1 BBS 的兴起（1978–1980s）

1978 年，Ward Christensen 和 Randy Suess 创建了第一个 BBS——**CBBS**。随着调制解调器的普及，BBS 在 1980 年代爆发式增长。

BBS 是纯文本环境——早期终端不支持图形显示。系统操作员（SysOp）需要用文本来装饰 BBS 界面：欢迎画面、菜单、登录提示等。这创造了巨大的 ASCII/ANSI 艺术需求。

### 6.2 ANSI 艺术与 ASCII 艺术的区别

**ASCII 艺术**：仅使用 ASCII 标准的 95 个可打印字符（32–126），单色。

**ANSI 艺术**：使用 IBM CP437 字符集（包含框线字符、块字符等扩展字符）+ ANSI X3.64 转义序列（16 色前景/背景、闪烁、粗体等）。效果远比纯 ASCII 丰富，是 BBS 时代的主流形式。

### 6.3 CP437——IBM PC 的字符集

1981 年 IBM PC 采用的 **Code Page 437** 包含 256 个字符：
- 0–127：标准 ASCII
- 128–255：扩展字符，包括框线绘制字符（╔═╗║╚╝等）、块字符（█▓▒░）、数学符号、希腊字母等

这些扩展字符为 ANSI 艺术家提供了远超 95 个 ASCII 字符的表现力，特别是块字符可以实现"亚像素"级别的明暗渐变。

### 6.4 TheDraw——定义时代的工具（1986）

**1986 年，Ian E. Davis 开发了 TheDraw**——一个共享ware ANSI 艺术编辑器。TheDraw 的影响怎么高估都不为过：

- 大大简化了从零创建 ANSI 艺术屏幕的过程
- 内置多种"字体"——用框线和块字符构成的大字母
- 包含过渡动画效果（dissolve、clock 等）
- 几乎所有 1990 年代的 BBS ANSI 艺术都是用 TheDraw 创建的

### 6.5 ANSI 艺术的黄金年代（1990–1996）

1990 年代初期是 ANSI 艺术的黄金年代：

- **国际 ANSI 艺术"场景"（scene）** 崛起——一个由艺术家组成的亚文化群体，形成竞争性团体
- 艺术团体定期将最佳作品汇编成 **"artpacks"**（艺术包），以 ZIP 格式在 BBS 上分发
- 团体之间激烈竞争，推动了艺术质量的飞速提升
- Artpack 通常包含：ANSI 艺术文件、补充文本文件（团体新闻、成员名单）、有时还有显示软件和 MOD 格式音乐

### 6.6 衰落与转型（1996–2000s）

1990 年代中期，互联网的崛起导致 BBS 用户流失，ANSI 艺术的观众急剧减少。Windows 取代 DOS 成为主流 OS，传统 ANSI 艺术软件难以运行。

> 到 1990 年代末，地下 ANSI 艺术场景"正在稳步崩溃"。

但 ANSI 艺术没有死亡：
- 开发了 Windows 兼容的绘图工具（ACiDDraw、TundraDraw）
- 21 世纪继续有新团体出现（如 **Blocktronics**）
- 老团体复兴（Mistigris、Fire、Lazarus）
- Demoscene 派对定期举办 ANSI 艺术比赛
- 新工具持续开发（PabloDraw、Moebius、DurDraw）

---

## 第七章：ASCII 艺术团体与 Artpack 文化

### 7.1 ACiD Productions（1990–）

**ACiD** 成立于 **1990 年**，是最早也是最有影响力的 ANSI 艺术团体之一。最初专注于 BBS 的 ANSI 艺术创作。第一个 artpack *The Acquisition* 在 1990 年代早期发布。

ACiD 的最大竞争对手是 **iCE Advertisements**。

### 7.2 iCE Advertisements（1991–）

**iCE**（Insane Creators Enterprise）于 **1991 年**在加拿大由 Many Axe 创立。与 ACiD 并列为地下计算机艺术场景最突出、最成功的两个团体。

### 7.3 其他重要团体

| 团体 | 成立 | 说明 |
|------|------|------|
| ACiD | 1990 | ANSI 艺术先驱 |
| iCE | 1991 | 加拿大，ACiD 最大对手 |
| Fire | 1990s | 黄金时代重要团体 |
| Dark | 1990s | 重要团体 |
| CIA | 1990s | 重要团体 |
| Mistigris | 1990s | 长寿团体，至今仍在发布 |
| Blocktronics | 2008 | 21 世纪新团体，至今活跃 |
| Lazarus | — | 复兴团体 |

### 7.4 Artpack 的意义

Artpack 被认为是早期计算机艺术场景保存如此完好的主要原因之一——每月的 artpack 发布形成了一种归档机制，大量作品因此得以保存。

### 7.5 16colo.rs——存档使命

**16colo.rs**（Sixteen Colors）是最大的在线 ANSI/ASCII artpack 存档，托管数千个发布包，从 1990 年至今。对于许多团体，16colo.rs 上的存档是他们作品唯一幸存的副本。

2004 年，*Dark Domain: The Artpacks.acid.org Collection* 发布——一张 DVD-ROM，包含 ACiD 和其他团体 14 年的 artpack。

2005 年，**Jason Scott** 在 *BBS: The Documentary* 中专门用一集 "Artscene" 讲述 ANSI 艺术场景的历史，主要覆盖 ACiD 和 iCE。

---

## 第八章：FIGlet——ASCII 大字艺术的诞生

### 8.1 FIGlet 的起源（1991）

**FIGlet** 由 **Frank Sheeran** 和 **Christiaan Keeman** 于 **1991 年**创建。它将普通文本转换为用 ASCII 字符绘制的大字艺术——例如将 "Hello" 变成 5 行高的 ASCII 字母。

FIGlet 引入了 **FIGfont** 格式——一种描述 ASCII 字体形状的标准文件格式（.flf），使得字体可以被独立创建和分享。这催生了数百种 FIGlet 字体的创作。

### 8.2 FIGlet 的影响

FIGlet 成为几乎所有终端工具显示 Banner 的标准方式。它的实现被移植到几乎所有编程语言：
- C（原始实现）
- JavaScript（figlet.js）
- Python（pyfiglet）
- Go（go-figure）
- Rust 等

### 8.3 toilet——FIGlet 的增强版

**toilet**（The Other Letter Engine）是 FIGlet 的现代替代品，支持彩色输出和更多字体选项，在 Debian/Ubuntu 中可通过 `apt install toilet` 安装。

### 8.4 cowsay——最著名的 FIGlet 衍生品（1999）

**cowsay** 由 Tony Monroe 于 1999 年创建，让 ASCII 艺术牛"说出"你输入的文字。配合 `fortune` 和 `lolcat` 管道使用——`fortune | cowsay | lolcat`——成为 Linux 终端最经典的彩蛋之一。

---

## 第九章：文字冒险游戏的起源

### 9.1 Will Crowther 与 Mammoth Cave（1972–1975）

**William Crowther** 是 BBN（Bolt, Beranek and Newman，建造早期互联网的公司）的程序员，也是一名洞穴探险者。他和妻子 **Patricia Crowther** 作为 Cave Research Foundation 成员，在 1970 年代早期 extensively 探索了肯塔基州的 **Mammoth Cave**（世界上最长的洞穴系统）。

1972 年，Patricia 领导的探险队发现了 Mammoth Cave 与更大的 Flint Ridge Cave System 之间的连接。夫妇俩将洞穴测量数据从"泥泞的小本子"转录到连接在 BBN 的 PDP-1 上的电传打字终端，生成了一些最早的计算机绘制洞穴地图。

### 9.2 Colossal Cave Adventure 的诞生（1975–1976）

1975 年，与 Patricia 离婚后，Crowther 停止了洞穴探险。出于想念两个女儿和有了更多空闲时间，他开始在 BBN 的 **PDP-10** 大型机上用 **FORTRAN** 编写一个文字游戏——让女儿们可以通过电传打字机探索洞穴。

他将 Mammoth Cave 的 Bedquilt 区域的真实地图与 Dungeons & Dragons 游戏元素结合，设计了一个探索洞穴寻找宝藏的游戏。他开发了自然语言输入系统，让非技术玩家也能用英语命令控制游戏。

原始版本：
- 约 700 行代码 + 700 行数据
- 66 个房间
- 193 个词汇
- 5 个宝藏
- 少量奇幻元素：水晶桥、魔法词（**XYZZY**）、斧头矮人
- 文件名：ADVENT

### 9.3 Don Woods 的扩展（1977）

**Don Woods**，斯坦福大学研究生，在斯坦福医学院的 PDP-10 上发现了 Adventure。他通过向 ARPANET 上所有域名的 "crowther" 发邮件来联系 Crowther 获得源码许可。

Woods 大幅扩展了游戏：
- 加入更多奇幻元素：龙、魔法、巨魔
- 140 个地图位置、293 个词汇、53 个物品
- 15 个宝藏（Crowther 原版 5 个 + 10 个新的）
- 计分系统（满分 350 分）
- 盗贼 NPC 在地图上漫游偷窃宝藏
- 约 3000 行代码 + 1800 行数据
- 添加了运行时间限制（防止管理员上班时间玩游戏）

1977 年 5 月发布后，游戏在美国各地引起轰动。据 Dave Lebling 回忆：

> "For a couple of weeks, dozens of people were playing the game and feeding each other clues. Everyone was asking you in the hallway if you had gotten past the snake yet."

### 9.4 Zork 的诞生（1977–1979）

**1977 年底**，MIT 的四名学生——**Marc Blank、Dave Lebling、Tim Anderson 和 Bruce Daniels**——在玩到 Adventure 后一个月内开始开发自己的版本。

他们的游戏 **Zork**（最初叫 Dungeon）比 Adventure 有重大突破：
- **更先进的解析器**：理解完整句子（"hit the troll with the Elvish sword"），而非 Adventure 的双词命令
- 更丰富的世界观：大地下帝国（Great Underground Empire）
- 幽默感和个性鲜明的写作
- 110 个房间、122 个物品、~40 个动词

### 9.5 Infocom 与商业文字冒险（1979–）

1979 年，Zork 的创作者们成立了 **Infocom** 公司，将文字冒险游戏商业化。Infocom 发明了 **Z-Machine**——一种虚拟机，让同一游戏可以在不同家用电脑上运行。ZIL（Zork Implementation Language）是他们的开发语言。

Infocom 的成功定义了整个文字冒险游戏 genre。2019 年，Microsoft 将 Zork I 的原始 ZIL 源码开源。

### 9.6 文字冒险的遗产

Colossal Cave Adventure 直接催生了：
- **Zork**（1977）→ Infocom → 整个商业文字冒险产业
- **Adventureland**（1978）by Scott Adams
- **Mystery House**（1980）by Roberta & Ken Williams → Sierra On-Line
- **Rogue**（1980）→ Roguelike genre
- **MUD**（1978）by Roy Trubshaw → MMORPG genre

2019 年，Colossal Cave Adventure 被选入 **World Video Game Hall of Fame**。

---

## 第十章：Roguelike 游戏的诞生与演变

### 10.1 Rogue 的诞生（1980）

**Rogue** 由 **Glenn Wichman** 和 **Michael Toy** 于 **1980 年**在 UC Santa Cruz 创建。灵感来自 *Adventure* 和 *Star Trek* 文字游戏。他们发现了 Ken Arnold 的 **curses** 库，可以在终端上操作字符位置，于是创建了一个"图形化的随机冒险游戏"。

核心特征：
- **ASCII 图形**：用字符表示怪物、物品、墙壁、门
- **程序化生成**：每次游戏地牢布局不同
- **永久死亡（permadeath）**：死了就死了，没有存档复活
- **回合制**：玩家移动一步，怪物也移动一步
- **`@` 代表玩家**：意为"where you're at"

Rogue 被包含在 **BSD UNIX v4.2**（1984）中，传播到全美各大学。Dennis Ritchie 曾戏称 Rogue 是"历史上最大的 CPU 周期浪费"。

### 10.2 Hack（1982）

Jay Fenlason 和高中同学们因无法再访问 Rogue，从记忆中重建了一个类似的游戏——**Hack**。1982 年，源代码通过 USENIX 磁带分发。

### 10.3 NetHack（1987）

1987 年 7 月，Mike Stephenson 在 Hack 基础上创建了 **NetHack**——名字中的"Net"反映通过 USENET 协作开发。NetHack 引入了：
- 更多怪物（借鉴多种神话体系）
- 预定义关卡 + 程序化元素
- 分支路径和角色任务
- 荒诞的死法——NetHack 以此闻名

NetHack DevTeam 至今仍在维护，以开发保密性著称。

### 10.4 Moria / UMoria / Angband（1985–）

- **Moria**（1985）by Robert Koeneke：以 Lord of the Rings 为主题，50 层地牢，怪物有不同速度
- **UMoria**（1987）：Moria 的移植
- **Angband**（1990）：以 Morgoth 的铁堡垒为名，可玩数百小时

### 10.5 ADOM（1994）

**Ancient Domains of Mystery** by Thomas Biskup，结合 NetHack 的深度和更故事驱动的体验。多个地牢通过大地图连接，混沌势力影响系统。

### 10.6 现代 Roguelike 与 Roguelite

- **Dungeon Crawl Stone Soup**（2006）
- **Brogue**（2009）：保留 ASCII 图形但用彩色着色
- **Tales of Maj'Eyal**（2010）
- **Spelunky**（2008）：平台跳跃 + Roguelike
- **The Binding of Isaac**（2011）
- **FTL**（2012）
- **Slay the Spire**（2019）
- **Hades**（2020）：将 Roguelike 带入主流

"Roguelike"一词于 1993 年在 Usenet 新闻组上被创造，用于统一讨论 Rogue、Hack、Moria、Angband 等游戏。

---

## 第十一章：ASCII 艺术工具的演进史

| 年份 | 工具 | 说明 |
|------|------|------|
| 1966 | Knowlton 的 BEFLIX | Bell Labs 的最早 ASCII 艺术生成程序 |
| 1986 | **TheDraw** | Ian E. Davis，定义了 BBS ANSI 艺术创作 |
| 1991 | **FIGlet** | Frank Sheeran & Christiaan Keeman，ASCII 大字生成 |
| 1994 | ACiDDraw | ACiD Productions，基于 TheDraw |
| 1995 | TundraDraw | 支持 24-bit 色彩 |
| 1999 | **cowsay** | Tony Monroe，ASCII 牛说话 |
| 2010s | **PabloDraw** | 现代 ANSI/ASCII 编辑器，支持多用户协作 |
| 2010s | **Moebius** | Andy Herbert，现代 ANSI 编辑器 |
| 2014 | **DurDraw** | Python，终端 ASCII/ANSI 绘画编辑器 |
| 2015 | **Monodraw** | macOS 原生 ASCII 艺术编辑器 |
| 2025 | **textmode.js** | WebGL2 实时 ASCII/textmode 创意编程库 |
| 2026 | **ansimon** | AI 生成 ANSI 艺术（SDXL + LoRA） |

---

## 第十二章：Demoscene 与 Textmode 艺术

### 12.1 Demoscene 概述

Demoscene 是一种计算机艺术亚文化，程序员创作称为"demos"的实时计算机程序，展示图形和音频效果。Textmode 艺术是 demoscene 的一个子领域。

### 12.2 Textmode 竞赛

至今，Revision、Evoke、RSync 等 demoscene 派对仍定期举办 **textmode graphics compos**（竞赛）。Blocktronics 等团体每月发布 artpack，延续 BBS 时代的传统。

### 12.3 重要存档与社区

| 名称 | 说明 |
|------|------|
| **16colo.rs** | 最大 ANSI/ASCII artpack 存档 |
| **Demozoo** | 62,000+ 作品数据库 |
| **CSDb** | Commodore 64 场景数据库，250,000+ 发布 |
| **pouët.net** | Demoscene 门户，100,000+ 作品 |
| **Lospec** | Textmode 画廊 |
| **text-mode.org** | 文本图形存档 |
| **ascii.gallery** | ANSI 艺术历史/艺术家/BBS 画廊 |

---

## 第十三章：PETSCII 与 Commodore 64 文本艺术

### 13.1 PETSCII 字符集

**PETSCII**（PET Standard Code of Information Interchange）是 Commodore 机器使用的字符集，包含 PET、CBM、VIC-20 和 C64 的特有字符。与 ASCII 不同，PETSCII 的图形字符集包含大量块字符和符号，适合创建图形效果。

### 13.2 C64 Textmode 艺术

Commodore 64 的 VIC-II 图形芯片提供 16 色和 40×25 文本模式。C64 艺术家使用 PETSCII 字符在文本模式下创建图像，形成了与 IBM PC ANSI 艺术平行但风格不同的艺术传统。

### 13.3 C64 场景

**CSDb**（Commodore 64 Scene Database）自 2001 年活跃至今，收录 250,000+ 发布，包含大量 PETSCII 艺术、C64 图形、团体历史、场景人物和 BBS 列表。**C64GFX** 展示 33,000+ C64 图形。

---

## 第十四章：互联网时代的 ASCII 艺术

### 14.1 从 BBS 到 Web

1990 年代中期，互联网取代 BBS 成为主要的数字通信平台。ASCII 艺术从 BBS 转移到：
- **Usenet 新闻组**：`alt.ascii-art` 等
- **电子邮件**：签名档中的 ASCII 艺术
- **IRC**：mIRC pop-ups 和 MACRO art
- **Web**：`<pre>` 标签中的 ASCII 艺术

### 14.2 表情符号的发明

ASCII 艺术家发明了**表情符号（emoticons）**——用少量字符组合表示情感状态：`:)` `:>` `:(` 等。电子邮件和 Usenet 充斥着这些符号。这是 1990 年代 ASCII 艺术黄金时代的一部分。

### 14.3 Joan Stark——ASCII 艺术大师

**Joan G. Stark**（署名 jgs）是最著名的 ASCII 艺术家之一。她的作品广泛流传，许多 ASCII 艺术作品角落都能看到她的署名 "jgs"。她的历史文章 *The History of ASCII (Text) Art* 是研究 ASCII 艺术史的重要参考文献。

### 14.4 ASCII 艺术的"经典"作品

- **Spy at the Wall** 系列
- **Silly Cows** 系列（David Bader 编辑）
- **Snoopy** 各种变体
- **Mona Lisa** 各种版本
- **ASCIIquarium**（ASCII 水族箱）

---

## 第十五章：AI 时代的 ASCII 艺术

### 15.1 AI 理解 ASCII 艺术——困难与突破

研究表明，LLM（GPT-4、Claude、Gemini 等）几乎无法识别 ASCII 艺术中的文字。arXiv:2602.15867（2026）的评估显示：所有模型平均完成度 <10%，最强 Claude Opus 4.5 仅得 75/350 分。

### 15.2 ASCII-Art-Identifier（2025）

DavidHua04 开发了推理时管道：检测 ASCII 艺术 → 转图片 → 送入 GPT-4V 生成描述 → 注入 LLM 提示词，无需重新训练即可提升 LLM 对 ASCII 艺术的理解。

### 15.3 ArtPerception——ASCII 艺术越狱（2025）

ianyang66 发现 LLM 无法识别 ASCII 艺术中的文字，利用这一点将敏感关键词编码为 ASCII 艺术绕过安全过滤。

### 15.4 SVE-ASCII——训练 LLM 生成和理解 ASCII 艺术（2026）

清华/复旦/阿里/NUS 合作，构建 ASCIIArt-7K 数据集，联合优化 Text→ASCII 和 ASCII→Text。核心发现："相互强化的循环"——学会生成 ASCII 艺术的模型也更擅长理解它。

### 15.5 ansimon——AI 生成真实 ANSI 艺术（2026）

grymmjack 的 ansimon 使用 SDXL + ANSI Art Style XL LoRA 生成图片，再通过 CP437 字符网格量化转为真实 .ANS 文件。训练数据来自 16colo.rs 自 1990 年以来的全部 artpack。

### 15.6 ZorkGPT——AI 玩文字冒险游戏（2025）

stickystyle 的 ZorkGPT 让 LLM 自主玩 Zork I——纯靠推理探索世界、解谜、收集宝藏。可在 zorkgpt.com 实时观看 AI 游玩。

---

## 第十六章：ASCII 艺术的时间线总览

| 年份 | 事件 |
|------|------|
| **1867** | 打字机发明 |
| **1898** | Flora Stacey 创作已知最早的打字机艺术（蝴蝶） |
| **1923** | RTTY Handbook 记载的最早文字图片传输（无实物留存） |
| **1945** | 二战后 surplus 电传打字机流入民间 |
| **1960** | Bob Bemer 发表统一编码提案 |
| **1961** | Bemer 向 ASA X3.2 提交 ASCII 提案 |
| **1963** | **ASCII 标准发布**（ASA X3.4-1963）；ASR-33 Teletype 发布 |
| **1966** | **Kenneth Knowlton 在 Bell Labs 创作最早计算机 ASCII 艺术** |
| **1967** | ASCII 修订版加入小写字母 |
| **1968** | 美国总统约翰逊强制联邦政府采用 ASCII |
| **1969** | ARPANET 启动；RFC 20 描述 ASCII 网络交换 |
| **1975** | **Will Crowther 创建 Colossal Cave Adventure** |
| **1977** | Don Woods 扩展 Adventure；**Zork 开发开始** |
| **1978** | 第一个 BBS（CBBS）创建；MUD 创建 |
| **1979** | Infocom 成立 |
| **1980** | **Rogue 发布**——Roguelike genre 诞生；FCC 授权 RTTY 使用 ASCII |
| **1981** | IBM PC 采用 ASCII/CP437 |
| **1982** | Hack 发布 |
| **1986** | **TheDraw 发布**——定义 BBS ANSI 艺术创作；BSD 4.3 包含 Rogue 源码 |
| **1987** | **NetHack 发布** |
| **1990** | **ACiD Productions 成立**——ANSI 艺术团体文化开始 |
| **1991** | **FIGlet 创建**；iCE Advertisements 成立 |
| **1993** | "Roguelike" 一词在 Usenet 上被创造 |
| **1994** | ADOM 开发开始；ACiDDraw 发布 |
| **1995** | NetHack 3.4.3 发布 |
| **1996** | 互联网开始取代 BBS，ANSI 艺术场景开始衰落 |
| **1999** | cowsay 创建 |
| **2004** | Dark Domain DVD-ROM 发布（14 年 artpack 合集） |
| **2005** | BBS: The Documentary "Artscene" 集 |
| **2008** | Blocktronics 成立；Spelunky 发布 |
| **2009** | Brogue 发布 |
| **2014** | DurDraw 发布 |
| **2015** | Monodraw 发布；RFC 20 升格为互联网标准 |
| **2019** | Microsoft 开源 Zork I 源码；Colossal Cave Adventure 入选 World Video Game Hall of Fame |
| **2025** | ZorkGPT、ASCII-Art-Identifier、ArtPerception、textmode.js |
| **2026** | SVE-ASCII、ansimon（AI 生成 ANSI 艺术） |

---

## 第十七章：关键人物名录

| 人物 | 贡献 |
|------|------|
| **Bob Bemer**（1920–2008） | "ASCII 之父"，推动 ASCII 标准化，引入转义字符 |
| **Hugh McGregor Ross** | Bemer 的英国同事，在欧洲推广 ASCII（"Bemer-Ross Code"） |
| **Kenneth Knowlton** | 1966 年 Bell Labs 最早计算机 ASCII 艺术 |
| **Leon Harmon** | 与 Knowlton 合著 "Studies in Perception I" |
| **Andries van Dam** | 1960s 最早 IBM 1403 行式打印机艺术 |
| **Flora Stacey** | 1898 年已知最早打字机艺术（蝴蝶） |
| **Will Crowther** | 1975 年创建 Colossal Cave Adventure，Mammoth Cave 探险者 |
| **Patricia Crowther** | Will 的妻子，洞穴探险家，发现 Mammoth-Flint Ridge 连接 |
| **Don Woods** | 1977 年扩展 Adventure，加入奇幻元素 |
| **Dave Lebling** | Zork 共同创建者，Infocom 联合创始人 |
| **Marc Blank** | Zork 共同创建者，Infocom 联合创始人 |
| **Tim Anderson** | Zork 共同创建者 |
| **Bruce Daniels** | Zork 共同创建者 |
| **Glenn Wichman** | Rogue 共同创建者 |
| **Michael Toy** | Rogue 共同创建者 |
| **Ken Arnold** | curses 库作者，帮助优化 Rogue |
| **Jay Fenlason** | Hack 创建者 |
| **Mike Stephenson** | NetHack 创建者 |
| **Robert Koeneke** | Moria 创建者 |
| **Thomas Biskup** | ADOM 创建者 |
| **Ian E. Davis** | TheDraw 创建者（1986），定义 BBS ANSI 艺术创作 |
| **Frank Sheeran** | FIGlet 共同创建者（1991） |
| **Christiaan Keeman** | FIGlet 共同创建者 |
| **Tony Monroe** | cowsay 创建者（1999） |
| **Joan G. Stark** | 著名 ASCII 艺术家（jgs），历史文献作者 |
| **Christian Wirth (RaD Man)** | ACiD Productions 成员，计算机艺术家和历史学家 |
| **Jason Scott** | BBS: The Documentary 制作人，存档 ASCII 艺术场景历史 |
| **Andy Herbert** | Moebius（现代 ANSI 编辑器）开发者 |
| **Bob Bemer** | ASCII 之父（再次致敬） |

---

## 参考文献

### 编码标准与历史

1. **Wikipedia: ASCII** — https://en.wikipedia.org/wiki/ASCII
2. **Wikipedia: ASCII art** — https://en.wikipedia.org/wiki/ASCII_art
3. **Wikipedia: ANSI art** — https://en.wikipedia.org/wiki/ANSI_art
4. **Wikipedia: Code Page 437** — https://en.wikipedia.org/wiki/Code_page_437
5. **Wikipedia: Baudot code** — https://en.wikipedia.org/wiki/Baudot_code
6. **Wikipedia: EBCDIC** — https://en.wikipedia.org/wiki/EBCDIC
7. **Engineering and Technology History Wiki: ASCII** — https://ethw.org/ASCII
8. **Britannica: ASCII** — https://www.britannica.com/topic/ASCII
9. **History of Information: ASCII** — https://www.historyofinformation.com/detail.php?id=803
10. **ASCII Code: History of ASCII 1963** — https://www.ascii-code.com/articles/ASCII-1963
11. **Adobe: What is ASCII** — https://www.adobe.com/acrobat/resources/document-files/what-is-ascii.html
12. **RFC 20 (ASCII for Network Interchange, 1969)** — https://datatracker.ietf.org/doc/html/rfc20

### ASCII 艺术历史

13. **Joan G. Stark: "The History of ASCII (Text) Art"** — https://roysac.com/asciiarthistory.html
14. **The Atlantic: "The Lost Ancestors of ASCII Art"** — https://www.theatlantic.com/technology/archive/2014/01/the-lost-ancestors-of-ascii-art/283445/
15. **Jefferson Computer Museum: "Ancient Alphabetic Art"** — https://gojefferson.com/jcm/aaa/index.html
16. **"Computer Pictures before Computer Graphics: The Practice of ASCII Art"** (Exa Library) — https://exa.ai/library/publication/nz7t6ssb4fg
17. **"ASCII Art and Its Antecedents"** (Exa Library) — https://exa.ai/library/publication/7bh35k75bht
18. **Asciiville: "Ascii Art History"** — https://asciiville.dev/posts/Ascii-Art-History/
19. **Text art history** — https://more.devils.gay/main-content/library/eng/text-art-history.html
20. **khrome/ascii-art-docs: History.md** — https://github.com/khrome/ascii-art-docs/blob/master/History.md
21. **Wikipedia: Typewriter art** — https://en.wikipedia.org/wiki/Typewriter_art
22. **Wikipedia: Artpack** — https://en.wikipedia.org/wiki/Artpack

### BBS / ANSI 艺术场景

23. **16colo.rs — ANSI/ASCII art archive** — https://16colo.rs/
24. **16colo.rs FAQ** — https://16colo.rs/faq
25. **ascii.gallery — ANSI Art Gallery** — https://ascii.gallery/ansi-art
26. **Wikipedia: ACiD Productions** — https://en.wikipedia.org/wiki/ACiD_Productions
27. **Wikipedia: TheDraw** — https://en.wikipedia.org/wiki/TheDraw
28. **bbsfiles.org: ANSI Editors** — https://bbsfiles.org/browse/ansi-editors
29. **bbsfiles.org: ACiDDRAW** — https://bbsfiles.org/browse/aciddraw
30. **Blocktronics on 16colo.rs** — https://16colo.rs/group/blocktronics
31. **Textmode and ANSI Art in the Demoscene (2026)** — https://mattcurrent.org/blog/textmode-ansi-art-demoscene-guide-2026

### 文字冒险游戏历史

32. **Wikipedia: Colossal Cave Adventure** — https://en.wikipedia.org/wiki/Colossal_Cave_Adventure
33. **Wikipedia: Zork** — https://en.wikipedia.org/wiki/Zork
34. **Wikipedia: Interactive fiction** — https://en.wikipedia.org/wiki/Interactive_fiction
35. **Wikipedia: Infocom** — https://en.wikipedia.org/wiki/Infocom
36. **Questner: "From Zork to AI: The History of Text Adventure Games"** — https://questner.ai/blog/history-of-text-adventures
37. **Smart Monsters: "A Partial History of Dungeon and Zork"** — https://smartmonsters.com/Dungeon/history.jsp
38. **Shapes: Colossal Cave Adventure Timeline** — https://shapes.inc/fandom/colossal-cave-adventure/timeline
39. **AI-Qwest: "Text Quests: From Zork to AI Game Masters"** — https://ai-qwest.com/en/blog/text-quest-history-zork-to-ai
40. **Colossal Cave Archaeology (academic paper)** — https://journals.uchicago.edu/doi/10.1086/713375
41. **historicalsource/zork1 (Microsoft open-sourced Zork I source)** — https://github.com/historicalsource/zork1

### Roguelike 游戏历史

42. **Wikipedia: Roguelike** — https://en.wikipedia.org/wiki/Roguelike
43. **Wikipedia: Rogue (video game)** — https://en.wikipedia.org/wiki/Rogue_(video_game)
44. **Wikipedia: NetHack** — https://en.wikipedia.org/wiki/NetHack
45. **Ars Technica: "ASCII art + permadeath: The history of roguelike games"** — https://arstechnica.com/gaming/2020/03/ascii-art-permadeath-the-history-of-roguelike-games/
46. **RogueBasin: List of roguelikes by year** — https://www.roguebasin.com/index.php/List_of_roguelikes_by_year
47. **NetHack in the Family Tree of Roguelikes** — https://nethackmonsters.art/texts/nethackinthefamilytreeofroguelikes/

### FIGlet 与终端工具

48. **Wikipedia: FIGlet** — https://en.wikipedia.org/wiki/FIGlet
49. **Wikipedia: cowsay** — https://en.wikipedia.org/wiki/Cowsay
50. **FIGlet 官方网站** — http://www.figlet.org/
51. **GitHub Topics: figlet** — https://github.com/topics/figlet

### Demoscene / Textmode

52. **Wikipedia: Demoscene** — https://en.wikipedia.org/wiki/Demoscene
53. **Demozoo** — https://demozoo.org
54. **pouët.net** — https://www.pouet.net
55. **Lospec: Textmode gallery** — https://lospec.com/gallery/medium:textmode-art
56. **text-mode.org** — https://text-mode.org
57. **humanbydefinition/awesome-textmode** — https://github.com<EMAIL_ADDRESS>
58. **humanbydefinition/textmode.js** — https1s://github.com/humanbydefinition/textmode.js
59. **code.textmode.art (textmode.js 文档)** — https://code.textmode.art

### PETSCII / Commodore 64

60. **Wikipedia: PETSCII** — https://en.wikipedia.org/wiki/PETSCII
61. **CSDb (Commodore 64 Scene Database)** — https://csdb.dk
62. **C64GFX (C64 pixel art gallery)** — https://c64gfx.com
63* **Petmate (PETSCII editor)** — https://nurpax.github.io/petmate
64. **EgonOlsen71/petsciiator** — https://github.com/EgonOlsen71/petsciiator

### AI 与 ASCII 艺术

65. **arXiv:2602.15867 — "Playing With AI: LLMs Perform in Zork"** — https://arxiv.org/abs/2602.15867v1
66. **arXiv:2603.14505 — "Unlocking the Latent Canvas: SVE-ASCII"** — https://arxiv.org/html/2603.14505v1
67. **arXiv:2402.11753 — "ArtPrompt: ASCII Art-based Jailbreak Attacks"** — https://arxiv.org/html/2402.11753v3
68. **arXiv:2510.10281 — "ArtPerception: ASCII Art-based Jailbreak"** — https://arxiv.org/html/2510.10281v1
69. **DavidHua04/ASCII-Art-Identifier** — https://github.com/DavidHua04/ASCII-Art-Identifier
70. **stickystyle/ZorkGPT** — https://github.com/stickystyle/ZorkGPT
71. **ZorkGPT Live Viewer** — https://zorkgpt.com
72. **arsindelve/ZorkAI** — https://github.com/arsindelve/ZorkAI

### 其他关键资源

73. **IOCCC (International Obfuscated C Code Contest)** — https://www.ioccc.org/
74. **IOCCC Winners (GitHub)** — https://github.com/ioc$cc-src/winner
75. **IOCCC ASCII Art 视觉索引** — https://dgopstein.github.io/articles/ioccc-ascii-art/
76. **BBS: The Documentary (Jason Scott)** — https://en.wikipedia.org/wiki/BBS:_The_Documentary
77. **Bob Bemer 个人页面** — https://en.wikipedia.org/wiki/Robert_William_Bemer
78. **Hugh McGregor Ross** — https://en.wikipedia.org/wiki/Hugh_McGregor_Ross
79. **Kenneth Knowlton** — https://en.wikipedia.org/wiki/Kenneth_Knowlton
80. **Andries van Dam** — https://en.wikipedia.org/wiki/Andries_van_Dam
81. **Will Crowther** — https://en.wikipedia.org/wiki/William_Crowther_(programmer)
82. **Don Woods** — https://en.wikipedia.org/wiki/Don_Woods_(programmer)
83. **textmode.js editor** — https://editor.textmode.art
84. **Blocktronics 官网** — http://blocktronics.org/
85. **The Interactive Fiction Archive (IF Archive)** — https://ifarchive.org/
    - 按日期索引（近三个月）: https://ukrestrict.ifarchive.org/indexes/datev_3.html
    - 完整存档入口: https://ukrestrict.ifarchive.org/indexes/if-archive
    - RSS 订阅: https://ukrestrict.ifarchive.org/indexes/archive.rss
    - 内容涵盖: 文字冒险游戏文件（.z3/.z5/.z8/.gblorb）、Z-Machine 解释器（Frotz/Glulxe/Bocfel）、Inform 编译器源码、游戏攻略、IFWiki 快照、IFDB 数据导出、Twine 游戏、Competition 作品集
86. **IFDB (Interactive Fiction Database)** — https://ifdb.org/
    - 互动小说游戏数据库，含评分、评论、标签、推荐
87. **IFWiki (Interactive Fiction Wiki)** — https://www.ifwiki.org/
    - 互动小说百科全书，涵盖游戏、工具、历史、人物
