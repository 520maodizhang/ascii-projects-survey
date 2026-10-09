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

### 1.4 委员会政治——6 位 vs 7 位 vs 8 位之争

ASCII 的诞生远非一帆风顺。X3.2.4 工作组的成员们围绕编码位数展开了激烈的辩论：

**6 位方案的诱惑**：ITA2 使用 shift function（移位功能）允许 6 位编码表示超过 64 个字符——某些字符码决定后续字符的选择。这种编码紧凑，但致命弱点是**传输可靠性**：如果移位码在传输中出错，后续大量数据将全部不可读。委员会最终否决了移位方案。

**8 位方案的吸引力**：8 位（一个字节）可以高效地用两个 4 位模式以 BCD 编码两个数字。但问题在于——所有数据传输都必须发送 8 位，而 7 位就足够了。在 1960 年代，传输带宽极其昂贵，每多传一位都是真金白银的成本。委员会投票决定使用 **7 位编码**以最小化传输成本。

**第 8 位的巧妙利用**：穿孔纸带当时可以在一个位置记录 8 位，因此第 8 位可以用作 **parity bit（奇偶校验位）**进行错误检查。不使用奇偶校验的 8 位机器通常将第 8 位设为 0——这就是后来"扩展 ASCII"（128–255）得以存在的技术基础。

### 1.5 ASCII 的设计哲学——每个位置都有理由

ASCII 的布局绝非随意，每个字符的位置都经过精心设计：

1. **控制字符在前 32 位**：0–31 为控制字符，32–126 为可打印字符，分离清晰。控制字符的位模式之间**最大化了 Hamming distance**，减少传输错误导致的歧义。

2. **大小写仅差一位**：`A`(65, 1000001) 和 `a`(97, 1100001) 的二进制仅第 6 位不同。这是 CCITT 在 1963 年 5 月提议将小写字母放入第 6、7 列（"sticks"）的结果——简化了大小写不敏感匹配、键盘和打印机的构造。

3. **字母按字母表顺序排列**：不像 EBCDIC 那样字母顺序混乱，ASCII 的字母排列方便列表排序（collation）。

4. **数字 0–9 前缀 011**：后 4 位直接对应二进制值（如 5 = 0110101，其中 0101 = 5），使 BCD 转换极其简单。

5. **字母 A 放在 0x41**：为了匹配英国标准草案中的对应位置。

6. **非字母数字字符对应机械打字机**：符号位置基于 **Remington No. 2**（1878 年，第一台有 shift 键的打字机）的 shift 位置，而非电动打字机。早期打字机甚至省略了 0 和 1，用大写 O 和小写 l 代替。

7. **@ 符号放在 0x40**：委员会认为 @ 在欧洲大陆不使用，预期会被国际变体中的重音字母 À 替换。事实证明这个判断完全错误——@ 后来成为了电子邮件的核心符号。

8. **ESC（27）转义字符**：Bemer 引入的转义字符为编码扩展提供了无限可能，后来成为 ANSI 转义序列的基础——今天终端彩色输出和光标控制全部依赖它。

### 1.6 SHARE 事件——IBM 用户组的最后通牒

就在 ASCII 标准即将发布的最后关头，一场政治风暴突然降临。**SHARE**（IBM 用户组）主席向 X3.2.4 工作组发来了一封措辞激烈的信件（vitriolic letter），威胁说如果不修改标准草案，程序员们将创建自己的竞争标准，ASCII 将因缺乏采用而面临 peril。

面对这一威胁，委员会做出了妥协：移动了一些字符的位置，在 `|`（竖线）字符中间加了断点（看看你的键盘上的 `|`——它中间有个缝隙，这就是 1967 年妥协的遗产）。

1967 年，ASCII 与 **ECMA**（欧洲计算机制造商协会）和 **ISO** 联合发布。ECMA 发布为 **ECMA-6**，ISO 发布为 **ISO-646**——ISO 版用国际货币符号 ¤ 替换了美元符号 $。

### 1.7 ASCII 的第一个商业应用

ASCII 于 1963 年首次商用，作为 AT&T 的 **TWX（TeletypeWriter eXchange）** 网络的 7 位电传打字机编码。TWX 原先使用 5 位 ITA2 编码（与 Telex 竞争系统相同）。

最影响 ASCII 字符解释的单一设备是 **ASR-33 Teletype**（1963 年发布），它定义了 Ctrl-Q（XON，码 17）、Ctrl-S（XOFF，码 19）和 DEL（码 127）等事实标准。ASR-33 的 O 键帽上还显示了一个左箭头符号（来自 ASCII-1963，当时这个位置是左箭头而非下划线），导致很多早期分时系统非标准地将 Ctrl-O 解释为"删除前一个字符"。

Ctrl-S/Ctrl-Q 的流控协议至今仍在使用——当发送方收到 XOFF 时停止传输以防溢出，收到 XON 时恢复发送。

### 1.8 ASCII 的对手——EBCDIC

1964 年，IBM 发布了划时代的 **System/360**，但开发团队负责人 **Frederick Brooks** 决定使用 **EBCDIC**（8 位编码，256 字符）而非 ASCII——因为当时的穿孔卡片和打印机还不支持 ASCII。EBCDIC 由 IBM 的 **Charles E. McKenzie** 从 6 位 BCDIC 扩展而来。

X3.2.4 委员会**断然拒绝了** IBM 的 EBCDIC 方案。但 IBM 的市场影响力意味着 EBCDIC 在大型机领域存活至今——这导致 ASCII 花了 **18 年**才在 IBM PC（1981）上成为 PC 标准。

直到 1981 年 IBM PC 发布，ASCII 才真正成为主流——IBM PC 的 ROM 中烧录了 **Code Page 437**，前 128 个字符是标准 ASCII，后 128 个是扩展字符（框线、块字符、希腊字母等）。CP437 的扩展字符后来为 ANSI 艺术提供了关键的表现力。

### 1.9 约翰逊总统令——ASCII 成为联邦标准

1968 年 3 月 11 日，美国总统**林登·B·约翰逊**签署备忘录，强制所有联邦政府计算机支持 ASCII：

> "All computers and related equipment configurations brought into the Federal Government inventory on and after July 1, 1969, must have the capability to use the Standard Code for Information Interchange..."

这是 ASCII 走向普遍采用的关键一步。但即便有总统令，ASCII 的全面普及仍花了十多年——直到 1981 年 IBM PC 才真正让 ASCII 成为事实标准。

---

## 第二章：ASCII 编码之前的文字编码史

### 2.1 摩尔斯码（1844）

Samuel Morse 发明的电报编码，用点和划表示字母。这是最早的"字符编码"概念，但不是数字编码。有趣的是，摩尔斯码中已经包含了"表情符号"的雏形——1857 年的 *National Telegraphic Review and Operators Guide* 记录了用数字 73 表示"爱与吻"（后来缩减为更正式的"致以敬意"）。

### 2.2 Baudot 码（1870/1874）

**Émile Baudot**（法国工程师）于 1870 年发明、1874 年获得专利的 5 位编码，32 个字符。使用 ITA2 国际标准版本（1932 年 CCITT 发布）。Baudot 码不支持小写字母，只有大写字母、数字和少量标点。它使用 shift function 在字母和数字/标点之间切换——正是这一机制后来被 ASCII 委员会讨论并否决。

Baudot 码是 RTTY（无线电电传打字）的标准编码，直到 1980 年 3 月 FCC 才授权美国业余无线电操作员使用 ASCII 替代 Baudot 码。

### 2.3 FIELDATA（1956）

美国陆军信号研究与发展实验室的 **Captain William F. Luebbert** 发明的 6 位编码，被美国陆军广泛用于通信。FIELDATA 在历史上很重要——它直接启发了后来发明 ASCII 的委员会。

### 2.4 IBM BCD / EBCDIC（1962）

IBM 的 6 位 BCD（Binary-Coded Decimal）用于穿孔卡片机器。当穿孔卡片被 System/360 大型机取代时，IBM 的 **Charles E. McKenzie** 将其扩展为 8 位 **EBCDIC**（Extended BCD Interchange Code）。EBCDIC 是 ASCII 最大的竞争对手，最终在 PC 市场败给 ASCII，但在大型机领域存活至今。

### 2.5 编码统一的必要性

到 1960 年，超过 60 种编码并存。Bemer 在 1960 年 12 月的 *Communications of the ACM* 上发表了一篇编码调查，记录了这一混乱局面。他在论文"A Proposal for Character Code Compatibility"中呼吁建立统一标准——这是推动 ASCII 诞生的直接动力。

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

### 5.1 Kenneth Knowlton 与 Bell Labs——一切开始的地方

**Kenneth C. Knowlton**（1931–2022），MIT 电气工程博士，1963 年加入 Bell Labs（位于新泽西州 Murray Hill），一直工作到 1982 年。他是计算机图形学和计算机艺术的真正先驱。

1963 年，Knowlton 发明了 **BEFLIX**（"Bell Flicks"的缩写）——**第一个用于计算机动画的领域专用编程语言**。BEFLIX 运行在 IBM 7094 大型机上，通过 **Stromberg-Carlson SC-4020 微缩胶片绘图仪** 输出图像。每帧包含 8 级灰度，分辨率为 252×184 像素。

1963–1964 年，Knowlton 用 BEFLIX 制作了一部 10 分钟的 16mm 无声电影 **"A Computer Technique for the Production of Animated Movies"**——这部电影本身就是关于如何制作这部电影的教程，充满了自引用的幽默。1964 年 4 月，他在 AFIPS Spring Joint Computer Conference 上发表了同名论文。

Knowlton 在 Bell Labs 期间开发了多个图形编程语言：
- **BEFLIX**（1963）——位图动画
- **EXPLOR**——用于 Lillian Schwartz 的动画作品（1968–1974）
- **SPHERES**——用于 Emmanuel Ghent 的 *Baobab*（1978）
- **L6**（Laboratories Low-Level Linked List Language）——链表处理语言

### 5.2 "Studies in Perception I"——Computer Nude（1967）

Knowlton 与 Bell Labs 同事 **Leon Harmon**（一位科学家，但自称是"掷硬币决定的"艺术家）合作创作了 **"Studies in Perception I"**（1967），后来被称为 **Computer Nude**——这是最早、也最著名的计算机生成 ASCII 艺术作品之一。

创作过程：
1. 扫描舞者和编舞家 **Deborah Hay** 的黑白照片
2. 将照片降采样为灰度网格
3. 将每个灰度值映射到电话电路图中的微缩符号
4. 在 IBM 7094（当时价值 200 万美元）上处理
5. 通过 SC-4020 微缩胶片绘图仪输出

原始打印件 **12 英尺宽**，被 Harmon 和 Knowlton 挂在 Bell Labs 分部执行主任 **Edward E. David Jr.** 的办公室墙上——作为一场恶作剧（prank）。David 外出回来后发现了这个"惊喜"。

这件作品随后在 **Robert Rauschenberg** 的 loft 的一场新闻发布会上展出，并于 **1967 年 10 月 11 日**出现在 *The New York Times* 上。Bell Labs 的公关人员显然决定这不是色情作品，而是"艺术"，并建议 Harmon 和 Knowlton 在任何展示场合都要注明这是 Bell Labs 制作的作品。

1968 年，该作品被收入 **MoMA**（纽约现代艺术博物馆）的展览 **"The Machine as Seen at the End of the Mechanical Age"**，以及伦敦 ICA 的 **"Cybernetic Serendipity"** 展览。

Knowlton 自己在 2005 年将这件作品称为一个 **"sophomoric prank"（幼稚的恶作剧）**。

### 5.3 "Gargoyle"——Studies in Perception III（1967）

同年，Harmon 和 Knowlton 还创作了 **"Gargoyle – Studies in Perception III"**——将巴黎圣母院的一张石像鬼照片数字化为灰度级别，然后为每个灰度值分配不同的 15×15 微缩图像。每张微缩图像本身都是一个小物体——这种"图像中的图像"技术远超同时代的其他作品。

### 5.4 Bell Labs 的艺术合作生态

Bell Labs 在 1960 年代成为计算机艺术的温床，这绝非偶然：

- **Max Mathews** 1961 年在 Bell Labs 合成了 **"Daisy Bell"**（Bicycle Built for Two）——第一首由计算机演唱的歌曲。这首歌后来被 Arthur C. Clarke 引用到 *2001: A Space Odyssey* 中 HAL 9000 的死亡场景。
- **Stan VanDerBeek** 与 Knowlton 合作 **Poemfields 1–10**（1966–1969）系列计算机动画电影。
- **Lillian Schwartz** 使用 Knowlton 的 EXPLOR 语言创作了 10 部动画电影（1968–1974）。
- 电子音乐作曲家 **Laurie Spiegel** 最初是通过 Bell Labs 的窗户看到 Knowlton 和 Schwartz 的作品后，被引入了计算机艺术的世界。

Knowlton 的合作理念：最好的结果是艺术家 **"become their own programmers, getting the whole creative process into one head"**（成为自己的程序员，将整个创作过程放在一个脑袋里）。而工程师则 **"become more complete humans"**（变得更完整的人）。

### 5.5 Andries van Dam 与 IBM 1403（1960s）

1960 年代，**Andries van Dam** 在 IBM 1403 行式打印机上发布了一幅电子电路图——这是最早的行式打印机艺术之一。IBM 1403 使用 EBCDIC 而非 ASCII，但技术原理相同：将图像降采样为字符网格，用不同密度的字符表示不同灰度。

### 5.6 行式打印机艺术的繁荣（1970s）

1970 年代，行式打印机艺术在整个计算机界繁荣。Knowlton 以在行式打印机上通过**叠印**（overprinting）多个字符来创建逼真图像而闻名——这种方法通过在同一位置打印多个字符来叠加灰度效果。

> "Everybody learned how to print a Snoopy banner."
> ——每个在计算机实验室工作过的人都学会了打印 Snoopy 横幅。

行式打印机艺术的常见主题：
- **Snoopy**（史努比）——最流行的主题，无数变体，是许多人进入编程的"入门礼"
- **圣诞树**——计算机实验室的圣诞传统，"圣诞树从全国各地的计算机实验室的电传打字机中喷出"
- **Mona Lisa**——Peterson 的 "Mona by the Numbers"，Ted Nelson 在 *Computer Lib / Dream Machines* 中称其为"Lizzie of the line printer"
- 肖像（华盛顿、林肯、杜鲁门等）

### 5.7 叠印技术（Overprinting）

1970–1980 年代流行一种依赖**叠印**的文字艺术：在打印机上输入一个字符，退格，再输入另一个字符——就像在打字机上一样。这在 **PLATO 系统**（约 1973）中发展得尤为成熟，上标和下标允许各种图形效果。一个常见用途是制作表情符号，WOBTAX 和 VICTORY 都能产生令人信服的笑脸。

叠印在打字机上已有先例，但视频终端上字符的低分辨率像素化意味着叠印在这里产生了**无缝像素图形**，而非可见的重叠字母组合——这是从打字机艺术到屏幕艺术的过渡技术。

### 5.8 穿孔卡片艺术的分发

ASCII 艺术通过**穿孔卡片组**在大学计算机中心的学生和工程师之间传递：

> "There were some prized card decks that got passed around for producing the art and periodically you would see an example in the computer room or someone's dorm room."
> ——一位 1970 年代中期的女工程师回忆

由于大量 ASCII 艺术具有色情性质（被称为"ASCII porn"），这些卡片组并不总是对所有人开放分享。一位女工程师回忆说，从来没有人主动与她分享过任何卡片组，可能正是因为作品的色情性质。

ASCII 艺术也常被赠送给参观计算机中心的儿童和员工家属。一位女性在 2013 年写信回忆：

> "In 1979, when I was 9 years old, he [her uncle, an IBM employee] gave me a banner for my birthday. It was from the old dot matrix printers. It had a silhouette of Snoopy on the top of his dog house and it said 'Happy Birthday Chimene'. I literally thought it was the coolest thing. This was before home computers and home printers for our family. The letters were made with x or o or maybe dashes. Because my brain had no conceptual framework for the world of computers, I literally wondered if it was created by magic."

### 5.9 1970 年代的 ASCII 艺术商业应用

- **美国购物中心**：1970 年代，美国各大购物中心设有自动亭，用计算机将照片转为 ASCII 艺术印在 T 恤上
- **伦敦科学博物馆**：提供类似服务，打印 ASCII 肖像
- **Control Data**：将 Mona Lisa 的 ASCII 版本作为促销材料赠送给客户

### 5.10 最早的互联网 ASCII 艺术

ARPANET（1969 年开始）上的电子邮件最初是纯文本——没有图片，更没有动画。ASCII 艺术被用来创建图表和示意图，也用于"好玩"和美化纯文本邮件。

已知最早的互联网 ASCII 艺术作品包括：
- **"Spy at the Wall"** 系列
- **"Silly Cows"** 系列——David Bader 编辑的完整原版奶牛集，这些奶牛遍布互联网，被视为"经典"ASCII 艺术

ARPANET 上的不同系统使用不同的行尾约定：TOPS-10/TENEX 用 CR-LF，Multics 用 LF，OS/360 用字符计数+字符且使用 EBCDIC。Telnet 协议为此定义了 **"Network Virtual Terminal"（NVT）**——以 ASCII + CR-LF 作为标准传输格式，每个系统在本地做转换。

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
- ANSI 艺术与 **warez**（盗版软件）文化紧密相连——ANSI 艺术家为海盗 BBS 创建欢迎画面和 .nfo 文件（信息文件），这些文件伴随着盗版软件发布，用华丽的 ASCII/ANSI 艺术标注破解者（cracker）和发布组（release group）的名称

> "Pirated software, known as 'warez,' was accompanied by ANSI art—a form of flashy hacker graffiti that credited the software crackers responsible."
> ——Vice, "The Lost Art of Warez"

### 6.6 衰落与转型（1996–2000s）

1990 年代中期，互联网的崛起导致 BBS 用户流失，ANSI 艺术的观众急剧减少。Windows 取代 DOS 成为主流 OS，传统 ANSI 艺术软件难以运行。

> 到 1990 年代末，地下 ANSI 艺术场景"正在稳步崩溃"。

一些大团体（如 ACiD）决定不再支持 ANSI，转向高分辨率图形。但 ANSI 艺术没有死亡：
- 开发了 Windows 兼容的绘图工具（ACiDDraw、TundraDraw）
- 21 世纪继续有新团体出现（如 **Blocktronics**，2008 年成立，至今活跃）
- 老团体复兴（Mistigris、Fire、Lazarus）
- Demoscene 派对定期举办 ANSI 艺术比赛
- 新工具持续开发（PabloDraw、Moebius、DurDraw）

---

## 第七章：ASCII 艺术团体与 Artpack 文化

### 7.1 ACiD Productions（1990–）

**ACiD** 成立于 **1990 年**，全称最初为 **"ANSI Creators in Demand"**（ANSI 创作者需求），由五位成员创立：**RaD Man**（Christian Wirth）、**Shadow Demon**、**Grimm**、**The Beholder** 和 **Phantom**。

ACiD 最初专注于为 **warez BBS** 创建 ANSI 艺术——海盗软件的欢迎画面、菜单和 .nfo 文件。第一个 artpack *The Acquisition* 在 1990 年代早期发布。成员从 1990 年的 5 人增长到 2003 年的 **700+**。

ACiD 的最大竞争对手是 **iCE Advertisements**。两大团体的竞争推动了 ANSI 艺术质量的飞速提升。

ACiD 后来扩展到其他艺术媒介：tracker 音乐、demo 编码和多媒体软件开发（如图像查看器）。后来决定不再支持 ANSI，转向更"专业"的高分辨率图形。

### 7.2 iCE Advertisements（1991–）

**iCE**（**Insane Creators Enterprise**）于 **1991 年**在加拿大由 **Many Axe** 创立。与 ACiD 并列为地下计算机艺术场景最突出、最成功的两个团体。iCE 的成员中有些是数字艺术和设计领域的专业人士。

### 7.3 第一个 ANSI 艺术团体——Aces of ANSI Art

在 ACiD 和 iCE 之前，第一个主要的 ANSI 艺术团体是 **Aces of ANSI Art（AAA）**。AAA 之后爆发了大量艺术团体，来自美国、加拿大、欧洲甚至中东。

### 7.4 其他重要团体

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

### 7.5 Artpack 的意义

Artpack 被认为是早期计算机艺术场景保存如此完好的主要原因之一——每月的 artpack 发布形成了一种归档机制，大量作品因此得以保存。相比之下，其他地下计算机场景（如早期黑客场景）的保存程度远不如 ANSI 艺术场景。

### 7.6 16colo.rs——存档使命

**16colo.rs**（Sixteen Colors）是最大的在线 ANSI/ASCII artpack 存档，托管数千个发布包，从 1990 年至今。对于许多团体，16colo.rs 上的存档是他们作品**唯一幸存的副本**。

2004 年，*Dark Domain: The Artpacks.acid.org Collection* 发布——一张 DVD-ROM，包含 ACiD 和其他团体 **14 年**的 artpack。

2005 年，**Jason Scott** 在 *BBS: The Documentary* 中专门用一集 **"Artscene"** 讲述 ANSI 艺术场景的历史，主要覆盖 ACiD 和 iCE，采访了两团体的成员及其他人士，讲述作品、发布和内部文化。

**"The Art of Warez"** 短片也记录了 ANSI 艺术场景的起源和历史。

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

**1977 年底**，MIT 的四名学生——**Marc Blank、Dave Lebling、Tim Anderson 和 Bruce Daniels**——在玩到 Adventure 后一个月内开始开发自己的版本。他们都是 MIT **Dynamic Modelling Group（DM）**的成员。

Lebling 之前已在 PDP-10 上创建了 *Spacewar!* 版本和 *Maze* 游戏（双人迷宫射击游戏），还写了一个 *Dungeons & Dragons* 辅助程序来自动化桌上游戏的书簿工作。他还与 Blank 和 Anderson 合作创建了一个包含 1000+ 问题的 trivia 游戏。

他们选择用 **MDL**（"Muddle"）编程——一种 MIT 开发的 LISP 基语言，提供强大的字符串处理能力。MDL 使 Zork 的解析器远超 Adventure 的双词命令——它理解完整句子，包括介词和形容词（"hit the troll with the Elvish sword"），这一系统后来被称为 **Interlogic**。

**"Zork"** 这个名字来自 MIT 黑客俚语——意为未完成的程序、占位符名称、或无脏话的感叹词。游戏最初正式叫 *Dungeon*，但 nickname Zork 已经 stuck 无法更改。

**Marc Blank 的通勤**：Blank 完成本科后去了纽约的 Albert Einstein 医学院，但每周末从纽约开车到波士顿帮忙开发 Zork。

他们的游戏 **Zork** 比 Adventure 有重大突破：
- **更先进的解析器**：理解完整句子（"hit the troll with the Elvish sword"），而非 Adventure 的双词命令
- 更丰富的世界观：大地下帝国（Great Underground Empire）
- 幽默感和个性鲜明的写作
- 110 个房间、122 个物品、~40 个动词

### 9.5 Infocom 与 Z-Machine（1979–）

**1979 年 6 月 22 日**，Infocom 正式成立。DM 实验室主任 **Al Vezza** 希望商业化实验室开发的技术，推动了公司的创建。初始资本仅 **$11,500**，由成员们凑钱。创始人包括：Blank、Lebling、Anderson、Joel Berez、Vezza、Chris Reeve、Stu Galley、Scott Cutler、Mike Broos 和 **J.C.R. Licklider**。

**技术挑战**：Zork 原始代码只在 PDP-10 上运行（MDL 语言），但家用电脑不支持 MDL，通常连 Fortran 编译器都没有，软盘只存 180KB，甚至用磁带存储。

**Z-Machine 的发明**：Joel Berez 和 Marc Blank 提出了一个天才方案——创建自己的编程语言 **ZIL**（Zork Implementation Language，MDL 的精简版），运行在自定义虚拟机 **Z-Machine** 上。只需将 Z-Machine 解释器（ZIP，Z-machine Interpreter Program）移植到新平台，而非移植每个游戏。这是 1979 年的"一次编写，到处运行"——与现代跨平台游戏引擎的理念相同。

1979 年，他们在租用的 DEC-20 上开发，实现了 **10:1 的数据压缩比**。第一个 ZIP 由 **Scott Cutler** 为 TRS-80 编写。

**1981 年 1 月**，MDL 版 Zork 做了最终更新——游戏达到了 1MB 的大小墙。此后 Zork 被分为三部曲：**Zork I、II、III**，分别于 1980、1981、1982 年商业发布。

Infocom 的成功定义了整个文字冒险游戏 genre。2019 年，Microsoft 将 Zork I 的原始 ZIL 源码开源（github.com/historicalsource/zork1）。

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

**Rogue** 由 **Glenn Wichman** 和 **Michael Toy** 于 **1980 年**在 UC Santa Cruz 创建。灵感来自 *Adventure* 和 *Star Trek* 文字游戏。他们发现了 Ken Arnold 的 **curses** 库——一个可以在终端上操作字符位置的库——于是创建了一个"图形化的随机冒险游戏"。

Toy 后来在 UC Berkeley 的计算实验室工作，遇到了 Arnold，Arnold 帮助优化了 curses 代码并在游戏中实现了更多功能。

核心特征：
- **ASCII 图形**：用字符表示怪物、物品、墙壁、门。`@` 代表玩家——意为 **"where you're at"**（你在哪里）。不同字母代表不同怪物，颜色编码增加信息密度
- **程序化生成**：每次游戏地牢布局不同——这是受限于 VAX-11/780 的内存而被迫采用的方案，却意外创造了极高的重玩价值
- **永久死亡（permadeath）**：死了就死了，没有存档复活
- **回合制**：玩家移动一步，怪物也移动一步

Rogue 被包含在 **BSD UNIX v4.2**（1984）中，传播到全美各大学。**Dennis Ritchie**（C 语言发明人）曾戏称 Rogue 是 **"the biggest waste of CPU cycles in history"**（历史上最大的 CPU 周期浪费）。

### 10.2 Beneath Apple Manor——真正的第一个 Roguelike（1978）

虽然 genre 以 Rogue 命名，但 **Beneath Apple Manor**（1978）by **Don Worth** 实际上早于 Rogue 两年。它在 Apple II 上运行，包含程序化生成、角色扮演元素、回合制战斗。但由于 Worth 是手工销售而非通过 ARPANET 分发，知名度远不如 Rogue。

### 10.3 Hack（1982）

**Jay Fenlason** 和高中同学们（Kenny Woodland、Mike Thome、Jonathan Payne）在 Lincoln-Sudbury Regional High School 的计算机实验室里，因无法再访问 Rogue，从记忆中重建了一个类似的游戏——**Hack**。名字既指"hack and slash"游戏，也指在没有源码的情况下重建 Rogue 的"programming hack"。

1982 年，Fenlason 将源代码通过 USENIX 磁带分发。

### 10.4 Andries Brouwer 的 Hack 扩展

荷兰数学家 **Andries Brouwer** 在 Centrum Wiskunde & Informatica（CWI）发现了 Hack 磁带，被深深吸引。他在几个月内发布了 4 个新版本，加入了：长虫（攻击中间会分裂成两条！）、宠物、幸运饼干、角色职业（战士/骑士/穴居人/巫师/游客/考古学家）、在地板上写字等。然后他失去了兴趣，停止了开发。

### 10.5 NetHack（1987）

1987 年 7 月，**Mike Stephenson** 在 Hack 基础上创建了 **NetHack**——名字中的"Net"反映通过 USENET 协作开发。他与宾夕法尼亚大学哲学教授 **Izchak Miller** 和 Janet Walz 组成了 **DevTeam**。

NetHack 引入了：
- 更多怪物（借鉴多种神话体系，包括 Terry Pratchett 的 *Discworld* 系列启发的"游客"职业配闪光灯相机）
- 预定义关卡 + 程序化元素
- 分支路径和角色任务
- **荒诞的死法**——NetHack 以此闻名，玩家可以死于各种离奇原因

NetHack DevTeam 至今仍在维护，以**开发保密性**著称——他们很少透露即将发布的改进内容，对代码贡献者也有严格筛选。

### 10.6 Moria / UMoria / Angband（1985–）

- **Moria**（1985）by **Robert Koeneke**，University of Oklahoma 学生。以 *Lord of the Rings* 为主题，50 层地牢（Rogue 的两倍），怪物有不同速度（越深越快），加入商店和角色职业。Koeneke 用 26 个字母的不同含义（如颜色编码的怪物）从 textmode 图形中挤出更多游戏深度。他还命名了一个怪物以第一个杀死 Balrog 的玩家命名。
- **UMoria**（1987）：Moria 的移植版
- **Angband**（1990）：以 Morgoth 的铁堡垒为名，可玩数百小时

### 10.7 ADOM（1994）

**Ancient Domains of Mystery** by **Thomas Biskup**，Technical University of Dortmund 学生。结合 NetHack 的深度和更故事驱动的体验。多个地牢通过大地图连接，混沌势力影响系统——受混沌影响的区域会导致角色变异，可能有益也可能有害。

### 10.8 现代 Roguelike 与 Roguelite

- **Dungeon Crawl Stone Soup**（2006）
- **Brogue**（2009）：保留 ASCII 图形但用彩色着色和动画使其生动，砍掉了角色职业、商店等非核心元素
- **Tales of Maj'Eyal**（2010）：开放世界、非线性故事、游戏内聊天
- **Spelunky**（2008）：平台跳跃 + Roguelike，将 genre 带入新方向
- **The Binding of Isaac**（2011）
- **FTL**（2012）
- **Slay the Spire**（2019）
- **Hades**（2020）：将 Roguelike 带入主流

**"Roguelike"一词的诞生**：1993 年，Usenet 用户们在讨论如何统一 Rogue、Hack、Moria、Angband 等游戏的讨论组时，经过三周辩论，从 `rec.games.dungeon.*` 改为 `rec.games.roguelike.*`——以 Rogue 命名，因为它被认为是这些游戏中最古老的。这一定名过程与"Doom clone"后来演变为"first-person shooter"类似。

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
- **Usenet 新闻组**：`alt.ascii-art` 成为创作者分享、批评和存档的中心
- **电子邮件**：签名档中的 ASCII 艺术——Usenet 有一条 netiquette 规定签名不超过 4 行，但很多人无视这条规则，用精心制作的 ASCII 艺术装饰签名。甚至有一个专门嘲笑违规者的新闻组 **`alt.fan.warlord`**——以一位特别热衷于制作超长 ASCII 签名的用户命名
- **IRC**：mIRC pop-ups 和 MACRO art
- **Web**：`<pre>` 标签中的 ASCII 艺术

### 14.2 表情符号的发明——Scott Fahlman 与 :-)（1982）

**1982 年 9 月 19 日**，Carnegie Mellon University 计算机科学家 **Scott Fahlman** 在 CMU 的 bboard（电子公告板）上提出了 `:-)` 和 `:-(`——这被公认为 ASCII 表情符号（emoticon）的诞生。

**起因**：一个关于电梯里水银泄漏的幽默警告被其他用户误解为严肃消息。这引发了一场关于如何在纯文本中标记"这不是严肃的"的讨论。

Fahlman 的原始帖子建议：
- `:-)` 标记"attempted humor"（试图幽默）
- `:-(` 标记严肃内容

其他建议包括 `*`（星号）和 `&`（代表笑弯腰的人），但 Fahlman 的方案胜出。几个月内，smiley 传到了 ARPANET 和 Usenet。

**鼻子的消失**：Stanford 大学的研究者调查了 400 万条 Twitter 消息，发现去掉鼻子的 `:)` 比原始的 `:-)` 更常见。1996 年 The Smiley Company 成立并商业化 smiley 商标，The Smiley Dictionary 网站编目了 500+ ASCII 表情符号。

### 14.3 Joan G. Stark——"The Queen of ASCII Art"

**Joan G. Stark**，又名 **Spunk** 或署名 **jgs**，是最著名的 ASCII 艺术家之一。许多 ASCII 艺术作品角落都能看到她的署名 "jgs"——她的作品广泛流传于整个互联网。

- **1995 年夏天**首次接触 ASCII 艺术
- **1996 年 7 月**开始创作 ASCII 艺术
- **1996–2003 年**创作数百件作品，主要发布在 Usenet `alt.ascii-art` 新闻组
- **1996–1998 年**网站每月更新，超过 **250,000 独立访客**
- 网站托管在 GeoCities（Soho/7373）
- 白底黑字为主，也创作彩色作品
- **民间艺术风格**，徒手创作，平均每件 **15–20 分钟**
- 至少有**四个孩子**
- 被称为 **"The Queen of ASCII Art"**

Stark 的参与被视为**女性在线参与增加**的例子，她的 imagery 被视为 ASCII 艺术 **"softer, more stereotypically feminine"**（更柔和、更刻板印象中的女性风格）的代表。

她的历史文章 *The History of ASCII (Text) Art* 是研究 ASCII 艺术史的重要参考文献，详细记录了从打字机艺术到 RTTY 到 BBS 的完整脉络。

### 14.4 Christopher Johnson 的 ASCII Art Collection（1994）

**1994 年 11 月**，**Christopher Johnson** 在早期万维网上发布了他的 ASCII Art Collection，托管在 **chris.com** 域名上（后来移到 asciiart.website）。这是最大、最知名的在线 ASCII 艺术存档之一。

- 按字母索引、主题分类、教程和链接
- 成为普通 Web 用户发现 ASCII 艺术的**中央门户**
- 从 1994 年运营至今（超过 30 年）
- 包含 Usenet `alt.ascii-art` 的存档

`alt.ascii-art` Usenet 新闻组是创作者分享、批评和存档的中心。Johnson 自己在 1994 年 11–12 月就在该组发布了大量请求（Snoopy、Garfield、Star Trek、Barney 等）。

另一个有趣的新闻组是 **`alt.fan.warlord`**——专门嘲笑违反 4 行签名限制的 Usenet 用户的过度精美 ASCII 签名档。

**"The Adventures of Nerd Boy"**（2001–2007）：在 `alt.ascii-art` 上发布了六年的 ASCII 艺术漫画，虽然" decidedly unambitious"（ decidedly 不太有野心），但代表了 ASCII 艺术在叙事领域的尝试。

### 14.5 ASCII 艺术的"经典"作品

- **Spy at the Wall** 系列——最早的互联网 ASCII 艺术之一
- **Silly Cows** 系列（David Bader 编辑）——遍布互联网的经典
- **Snoopy** 各种变体——从 1970 年代行式打印机到 1990 年代 Usenet
- **Mona Lisa** 各种版本——从 Knowlton 的 1966 年版到无数变体
- **ASCIIquarium**（ASCII 水族箱）——终端动画彩蛋

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
88. **Wikipedia: Emoticon** — https://en.wikipedia.org/wiki/Emoticon
89. **Scott Fahlman: Original Smiley Post** — https://www.cs.cmu.edu/~sef/Orig-Smiley.htm
90. **Scott Fahlman: "The Birth, Spread, and Evolution of the Smiley Emoticon" (PDF)** — https://www.cs.cmu.edu/~sef/Smiley2021.pdf
91. **Ars Technica: "In 1982, a physics joke gone wrong sparked the invention of the emoticon"** — https://arstechnica.com/gadgets/2025/11/in-1982-a-physics-joke-gone-wrong-sparked-the-invention-of-the-emoticon/
92. **Vice: "The Lost Art of Warez"** — https://www.vice.com/en/article/the-lost-art-of-warez
93. **The New Stack: "The Surprisingly Rich History of ASCII Art"** — https://thenewstack.io/surprisingly-rich-history-ascii-art/
94. **ASCII Art Archive: "The history of ASCII Art"** — https://www.asciiart.eu/history-of-ascii-art
95. **Christopher Johnson's ASCII Art Collection** — https://asciiart.website
96. **Wikipedia: Joan Stark** — https://en.wikipedia.org/wiki/Joan_Stark
97. **Joan Stark's ASCII Art Gallery (GeoCities archive)** — https://oldcompcz.github.io/jgs/joan_stark/
98. **Wikipedia: BEFLIX** — https://en.wikipedia.org/wiki/BEFLIX
99. **ETHW: "Early Digital Art At Bell Telephone Laboratories"** — https://ethw.org/First-Hand:Early_Digital_Art_At_Bell_Telephone_Laboratories,_Inc
100. **ETHW: "Harmon-Knowlton's 'The Nude' Overshadows All"** — https://ethw.org/First-Hand:Harmon-Knowlton's_%22The_Nude%22_Overshadows_All
101. **V&A Museum: Studies in Perception I** — https://collections.vam.ac.uk/item/O239963/studies-in-perception-i-print-harmon-leon/
102. **MoMA: "An Evening of Computer Films with Ken Knowlton"** — https://www.moma.org/calendar/events/4117
103. **NYT: "Ken Knowlton, a Father of Computer Art and Animation, Dies at 91"** — https://www.nytimes.com/2022/06/24/technology/ken-knowlton-dead.html
104. **Digital Art Museum: Ken Knowlton** — https://dam.org/museum/artists_ui/artists/knowlton-ken
105. **Filmmaker Magazine: "Engineers, Artists, Both? Bell Labs' Pioneering Ken Knowlton"** — https://filmmakermagazine.com/116836-joanne-mcneil-bell-labs-ken-knowlton
106. **History of Information: BEFLIX** — https://www.historyofinformation.com/detail.php?id=3467
107. **Wikipedia: Beneath Apple Manor** — https://en.wikipedia.org/wiki/Beneath_Apple_Manor
108. **The Dot Eaters: "Zork and Infocom"** — https://thedoteaters.com/?bitstory=computer/zork-and-infocom
109. **Timeweave Chronicles: "How Interactive Fiction Was Born"** — https://timeweavechronicles.blogspot.com/2026/07/how-interactive-fiction-was-born-and.html
110. **roysac.com: "An Abbreviated History of the Underground Computer Art Scene"** — https://www.roysac.com/learn/HistoryUndergroundComputerArtScene.html
111. **Wikipedia: ACiD Productions** — https://en.wikipedia.org/wiki/ACiD_Productions
