# ASCII 隐写器

> 把密码藏进 ASCII 画里 —— 表面是一幅画或大字，里面用零宽字符逐比特隐藏真正的密码，肉眼完全不可见。

## 功能

- **画系统**：内置 13 幅 ASCII 画（猫、狗、机器人、龙、猫头鹰...），选一幅把密码藏进去
- **字系统**：把文字渲染成 5 行高块字母大字，密码藏在大字里
- **自定义画**：用你自己的 ASCII 画文件作为载体
- **零宽隐写**：用 `U+200B`(bit 0) / `U+200C`(bit 1) 逐比特编码，肉眼不可见
- **统一解码**：`decode` 不区分来源，丢进去就能取出密码
- **纯标准库**：不依赖任何第三方包，`python3 stego.py` 直接运行

## 快速开始

```bash
# 列出内置画
python3 stego.py pics

# 画系统：把密码藏进猫画
python3 stego.py encode --pic cat --secret "MySecret998" -o cat.txt

# 字系统：把密码藏进大字
python3 stego.py encode --text "HELLO" --secret "Pass123" -o txt.txt

# 自定义：用你自己的画
python3 stego.py encode --art-file my_drawing.txt --secret "密码" -o out.txt

# 解码（三种方式生成的文件都能解）
python3 stego.py decode cat.txt
```

## 效果演示

### 画系统

```
$ python3 stego.py encode --pic cat --secret "MySecret998" -o cat.txt
已生成 ASCII 隐写文件: cat.txt
  载体: 画: cat (12 行)
  隐藏秘密: MySecret998  (零宽字符 120 个)

$ python3 stego.py decode cat.txt
隐藏的秘密: MySecret998
```

别人打开 `cat.txt` 看到的就是一只猫：

```
      /\      /\
     /  \____/  \
    /            \
   (  o      o   )
   (      ==      )
    \            /
     \          /
      \________/
       |      |
       |      |
      /        \
     /          \
```

### 字系统

```
$ python3 stego.py encode --text "HELLO" --secret "Pass123" -o txt.txt

$ python3 stego.py decode txt.txt
隐藏的秘密: Pass123
```

别人看到的是大字艺术：

```
#  #  ####  #     #      ###
#  #  #     #     #     #   #
####  ###   #     #     #   #
#  #  #     #     #     #   #
#  #  ####  ####  ####   ###
```

## 原理

1. **载体生成**：根据 `--pic` / `--text` / `--art-file` 生成可见的 ASCII 艺术作为掩护
2. **秘密编码**：将秘密消息转为 UTF-8 字节，加 32 位长度头，转成二进制比特流
3. **零宽嵌入**：每个比特映射为一个零宽 Unicode 字符（`U+200B` = 0, `U+200C` = 1），均匀分散到每行末尾
4. **解码还原**：扫描文件中所有零宽字符，还原比特流，读长度头，重建原始字节

零宽字符在终端和编辑器中完全不占宽度、不可见，所以载体艺术看起来和普通 ASCII 画一模一样。

## 内置画库

| 名称 | 说明 | 名称 | 说明 |
|------|------|------|------|
| cat | 猫 | dog | 狗 |
| heart | 爱心 | face | 笑脸 |
| robot | 机器人 | owl | 猫头鹰 |
| penguin | 企鹅 | coffee | 咖啡杯 |
| skull | 骷髅 | fish | 鱼 |
| dragon | 龙 | bunny | 兔子 |
| sword | 剑 | | |

## 命令一览

```
python3 stego.py pics                                    # 列出内置画
python3 stego.py encode --pic <画名> --secret <密码>     # 画系统
python3 stego.py encode --text <文字> --secret <密码>    # 字系统
python3 stego.py encode --art-file <文件> --secret <密码> # 自定义画
python3 stego.py decode <文件>                           # 解码
python3 stego.py decode                                  # 从 stdin 粘贴解码
```

## 环境要求

- Python 3.6+
- 无第三方依赖

## License

MIT
