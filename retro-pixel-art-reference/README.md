# Kimi Careers (careers.kimi.com/about-us) 源码存档

从 https://careers.kimi.com/about-us 爬取的源码，用于研究其 **复古像素艺术（Retro Pixel Art）** 设计风格。

## 文件说明

```
kimi-careers-source/
├── html/
│   └── about-us.html          # 页面 HTML（Next.js SSR 输出）
├── css/
│   ├── main.css               # 主样式（52KB）— Tailwind v4 + RetroCursor 主题 + 像素字体
│   └── components.css         # 组件样式（2KB）— 文字扰动动画 + 招聘地图射线动画
├── js/
│   ├── pixel-flow.js          # 像素流视频处理（6KB）— Canvas 降采样 + Bayer 抖动
│   ├── scene-shared.js        # 场景共享逻辑（16KB）— 打字机效果 + 场景状态
│   ├── next-image.js          # Next.js Image 组件（26KB）
│   ├── framer-motion.js       # Framer Motion 动画库（147KB）
│   ├── gsap.js                # GSAP 动画引擎（70KB）
│   └── moon-eclipse.js        # 月球日食核心动画（87KB）— 程序化月球 + 抖动渲染
├── 如何制作复古像素风网站.md    # 完整制作指南
└── README.md                  # 本文件
```

## 关键技术点速览

| 特性 | 实现方式 |
|------|----------|
| 像素字体 | `Fusion Pixel 12px Mono zh_hans` (.otf) |
| 复古光标 | `/assets/cursors/retrosmart/*.png` 全套像素光标 |
| 像素视频 | Canvas 降采样 + Bayer 有序抖动，6 级灰度 |
| 程序化月球 | Perlin 噪声纹理 + 随机陨石坑 + 光照模拟 + 抖动 |
| 文字扰动 | ASCII 字符随机跳动后逐字归位 |
| 打字机效果 | 逐字显示 + 闪烁光标 `_` |
| 场景叙事 | 滚动驱动，月球经历 接近→日食→着陆 |
| 硬阴影 | `text-shadow` 无 blur，纯偏移 |
| 动画引擎 | GSAP + Framer Motion |
| 框架 | Next.js (App Router + Turbopack) + React + Tailwind v4 |
