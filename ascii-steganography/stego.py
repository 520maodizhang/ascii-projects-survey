#!/usr/bin/env python3
"""
ASCII 隐写器 (双系统)
  系统 A - 画: 把密码藏进 ASCII 画里 (猫/狗/机器人/...)
  系统 B - 字: 把密码藏进 ASCII 块字母里 (HELLO → 大字艺术)
两系统都用零宽字符 (U+200B / U+200C) 逐比特隐藏，肉眼完全不可见。

用法:
  列画:  python3 stego.py pics
  画系统: python3 stego.py encode --pic cat --secret "密码" -o cat.txt
  字系统: python3 stego.py encode --text "HELLO" --secret "密码" -o txt.txt
  自定义: python3 stego.py encode --art-file my.txt --secret "密码"
  解码:   python3 stego.py decode cat.txt
          python3 stego.py decode                    # 从 stdin 粘贴
"""

import argparse
import sys


# ============================================================
# 1. 内置 ASCII 画库
# ============================================================

PICTURES = {
    'cat': [
        r"      /\      /\      ",
        r"     /  \____/  \     ",
        r"    /            \    ",
        r"   (  o      o   )   ",
        r"   (      ==      )   ",
        r"    \            /    ",
        r"     \          /     ",
        r"      \________/      ",
        r"       |      |       ",
        r"       |      |       ",
        r"      /        \      ",
        r"     /          \     ",
    ],
    'dog': [
        r"    __      _        ",
        r" o'')}____//        ",
        r"  `_/      )        ",
        r"  (_(_/-(_/         ",
        r"                     ",
        r"   /|__|\           ",
        r"  / |  | \          ",
        r"    |  |            ",
        r"   /    \           ",
        r"  /      \          ",
    ],
    'heart': [
        r"   ***   ***   ",
        r"  ***** *****  ",
        r" ************* ",
        r"  ***********  ",
        r"   *********   ",
        r"    *******    ",
        r"     *****     ",
        r"      ***      ",
        r"       *       ",
    ],
    'face': [
        r"     *********     ",
        r"    *         *    ",
        r"   *  O     O  *   ",
        r"   *    \ /    *   ",
        r"   *     -     *   ",
        r"   *  \_____/  *   ",
        r"    *         *    ",
        r"     *********     ",
    ],
    'robot': [
        r"      +-------+      ",
        r"      | o   o |      ",
        r"      |  ===  |      ",
        r"      +-------+      ",
        r"       |     |       ",
        r"      /|     |\      ",
        r"     / |     | \     ",
        r"    /  |     |  \    ",
        r"       |     |       ",
        r"      /       \      ",
        r"     /         \     ",
    ],
    'owl': [
        r"      ___           ",
        r"     /o o\          ",
        r"    (  v  )         ",
        r"     \_-_/__        ",
        r"    __/   \__       ",
        r"   /         \      ",
        r"  /           \     ",
        r"  |    | |    |     ",
        r"  |___/   \___|     ",
    ],
    'penguin': [
        r"      .---.         ",
        r"     / o o \        ",
        r'    (  " v "  )       ',
        r"     \_-_/__        ",
        r"    __/   \__       ",
        r"   /         \      ",
        r"  |           |     ",
        r"  |   |   |   |     ",
        r"  |___|___|___|     ",
    ],
    'coffee': [
        r"      ( (     ",
        r"       ) )    ",
        r"     ------   ",
        r"    |      |] ",
        r"    |      |  ",
        r"    |______|  ",
        r"      \  /    ",
        r"       \/     ",
    ],
    'skull': [
        r"       ___        ",
        r"      /o o\       ",
        r"     (  v  )      ",
        r"      \___/       ",
        r"      / | \       ",
        r"     /  |  \      ",
        r"    /   |   \     ",
        r"        |         ",
    ],
    'fish': [
        r"            __     ",
        r"           /  \    ",
        r"  ___ ____/    \   ",
        r" /   o          >  ",
        r" \________ ____/   ",
        r"   V  V  V         ",
    ],
    'dragon': [
        r"         /\         ",
        r"        /  \        ",
        r"       /    \       ",
        r"      / o  o \      ",
        r"     /   ==   \     ",
        r"     \        /     ",
        r"      \______/      ",
        r"      /      \      ",
        r"     /        \     ",
        r"    /          \    ",
        r"   /            \   ",
    ],
    'bunny': [
        r"      (\(\   ",
        r"      ( -.-)  ",
        r'      o_(")(',
        r"        )    ",
        r"       (     ",
        r"        )    ",
        r"       (     ",
    ],
    'sword': [
        r"          /|",
        r"         / |",
        r"        /  |",
        r"       /   |",
        r"      /    |",
        r"     /     |",
        r"    /______|",
        r"       ||  ",
        r"       ||  ",
        r"       ||  ",
        r"      /__\ ",
    ],
}


# ============================================================
# 1b. 内置块字体 (5 行高) —— 字系统
# ============================================================

FONT = {
    'A': [" ##  ", "#  # ", "#### ", "#  # ", "#  # "],
    'B': ["###  ", "#  # ", "###  ", "#  # ", "###  "],
    'C': [" ####", "#    ", "#    ", "#    ", " ####"],
    'D': ["###  ", "#  # ", "#   #", "#  # ", "###  "],
    'E': ["#### ", "#    ", "###  ", "#    ", "#### "],
    'F': ["#### ", "#    ", "###  ", "#    ", "#    "],
    'G': [" ####", "#    ", "#  ##", "#  # ", " ####"],
    'H': ["#  # ", "#  # ", "#### ", "#  # ", "#  # "],
    'I': [" ### ", "  #  ", "  #  ", "  #  ", " ### "],
    'J': ["  ###", "   # ", "   # ", "#  # ", " ##  "],
    'K': ["#  # ", "# #  ", "##   ", "# #  ", "#  # "],
    'L': ["#    ", "#    ", "#    ", "#    ", "#### "],
    'M': ["#   #", "## ##", "# # #", "#   #", "#   #"],
    'N': ["#   #", "##  #", "# # #", "#  ##", "#   #"],
    'O': [" ### ", "#   #", "#   #", "#   #", " ### "],
    'P': ["###  ", "#  # ", "###  ", "#    ", "#    "],
    'Q': [" ### ", "#   #", "#   #", "#  ##", " ## #"],
    'R': ["###  ", "#  # ", "###  ", "# #  ", "#  # "],
    'S': [" ####", "#    ", " ### ", "    #", "#### "],
    'T': ["#####", "  #  ", "  #  ", "  #  ", "  #  "],
    'U': ["#   #", "#   #", "#   #", "#   #", " ### "],
    'V': ["#   #", "#   #", "#   #", " # # ", "  #  "],
    'W': ["#   #", "#   #", "# # #", "## ##", "#   #"],
    'X': ["#   #", " # # ", "  #  ", " # # ", "#   #"],
    'Y': ["#   #", " # # ", "  #  ", "  #  ", "  #  "],
    'Z': ["#####", "   # ", "  #  ", " #   ", "#####"],
    '0': [" ### ", "#   #", "#  ##", "#   #", " ### "],
    '1': ["  #  ", " ##  ", "  #  ", "  #  ", " ### "],
    '2': [" ### ", "#   #", "   # ", "  #  ", "#####"],
    '3': ["#### ", "   # ", " ### ", "   # ", "#### "],
    '4': ["#   #", "#   #", "#####", "    #", "    #"],
    '5': ["#####", "#    ", "#### ", "    #", "#### "],
    '6': [" ### ", "#    ", "#### ", "#   #", " ### "],
    '7': ["#####", "    #", "   # ", "  #  ", " #   "],
    '8': [" ### ", "#   #", " ### ", "#   #", " ### "],
    '9': [" ### ", "#   #", " ####", "    #", " ### "],
    ' ': ["     ", "     ", "     ", "     ", "     "],
    '!': ["  #  ", "  #  ", "  #  ", "     ", "  #  "],
    '?': [" ### ", "#   #", "   # ", "     ", "  #  "],
    '.': ["     ", "     ", "     ", "     ", "  #  "],
    ',': ["     ", "     ", "     ", "  #  ", " #   "],
    '-': ["     ", "     ", " ### ", "     ", "     "],
    '+': ["     ", "  #  ", " ### ", "  #  ", "     "],
    '@': [" ### ", "#   #", "# ###", "#    ", " ### "],
    '#': [" # # ", "#####", " # # ", "#####", " # # "],
    '/': ["    #", "   # ", "  #  ", " #   ", "#    "],
    ':': ["     ", "  #  ", "     ", "  #  ", "     "],
    '_': ["     ", "     ", "     ", "     ", "#####"],
}

FONT_HEIGHT = 5


def render_banner(text: str) -> list[str]:
    """把文本渲染成 5 行高的块字母艺术，返回行列表。"""
    chars = [FONT.get(c.upper(), FONT.get(c, FONT['_'])) for c in text]
    lines = []
    for row in range(FONT_HEIGHT):
        line = ' '.join(ch[row] for ch in chars)
        lines.append(line.rstrip())
    return lines


# ============================================================
# 2. 零宽字符隐写
# ============================================================

ZW_ZERO = '\u200b'   # Zero Width Space  → bit 0
ZW_ONE  = '\u200c'   # Zero Width Non-Joiner → bit 1
BIT_MAP = {ZW_ZERO: '0', ZW_ONE: '1'}
TO_ZW   = {'0': ZW_ZERO, '1': ZW_ONE}


def _to_bits(payload: str) -> str:
    """字符串 → 32 位长度头 + UTF-8 字节的二进制。"""
    data = payload.encode('utf-8')
    return format(len(data), '032b') + ''.join(format(b, '08b') for b in data)


def _from_bits(bits: str) -> str:
    """二进制 → 字符串（读 32 位长度头）。"""
    if len(bits) < 32:
        raise ValueError("隐写数据不完整")
    length = int(bits[:32], 2)
    body = bits[32:]
    if len(body) < length * 8:
        raise ValueError("隐写数据被截断")
    raw = bytes(int(body[i * 8:i * 8 + 8], 2) for i in range(length))
    return raw.decode('utf-8')


def hide(payload: str) -> str:
    """把秘密编码为零宽字符序列。"""
    return ''.join(TO_ZW[b] for b in _to_bits(payload))


def reveal(text: str) -> str:
    """从文本中提取所有零宽字符并还原秘密。"""
    bits = ''.join(BIT_MAP[c] for c in text if c in BIT_MAP)
    if not bits:
        raise ValueError("未发现隐写数据（没有零宽字符）")
    return _from_bits(bits)


def embed(art_lines: list[str], zw_payload: str) -> str:
    """把零宽字符均匀分散到每行末尾（肉眼不可见）。"""
    if not zw_payload:
        return '\n'.join(art_lines)
    n = len(art_lines)
    chunk = -(-len(zw_payload) // n)  # 向上取整
    out = []
    for i, line in enumerate(art_lines):
        part = zw_payload[i * chunk:(i + 1) * chunk]
        out.append(line + part)
    return '\n'.join(out)


# ============================================================
# 3. 命令行界面
# ============================================================

def cmd_pics(args):
    print(f"内置 {len(PICTURES)} 幅 ASCII 画:\n")
    for name, lines in PICTURES.items():
        preview = lines[0].rstrip()
        print(f"  {name:<10} ({len(lines)} 行)  {preview}")


def cmd_encode(args):
    if not args.secret:
        print("错误: 需要提供 --secret 秘密消息", file=sys.stderr)
        sys.exit(1)

    # 获取载体内容：优先级 text > pic > art-file
    if args.text is not None:
        art_lines = render_banner(args.text)
        carrier = f"字: {args.text}"
    elif args.art_file:
        with open(args.art_file, encoding='utf-8') as f:
            art_lines = [ln.rstrip('\n') for ln in f.readlines() if ln.strip()]
        carrier = args.art_file
    elif args.pic:
        if args.pic not in PICTURES:
            print(f"错误: 没有这幅画 '{args.pic}'", file=sys.stderr)
            print(f"可选: {', '.join(PICTURES)}", file=sys.stderr)
            sys.exit(1)
        art_lines = PICTURES[args.pic]
        carrier = f"画: {args.pic}"
    else:
        print("错误: 需要指定 --pic <画名> / --text <文字> / --art-file <文件>",
              file=sys.stderr)
        sys.exit(1)

    zw = hide(args.secret)
    result = embed(art_lines, zw)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result + '\n')
        print(f"已生成 ASCII 隐写文件: {args.output}")
        print(f"  载体: {carrier} ({len(art_lines)} 行)")
        print(f"  隐藏秘密: {args.secret}  (零宽字符 {len(zw)} 个)")
        print(f"  解码: python3 {sys.argv[0]} decode {args.output}")
    else:
        print(result)


def cmd_decode(args):
    if args.input:
        with open(args.input, encoding='utf-8') as f:
            text = f.read()
    else:
        print("请粘贴 ASCII 画内容，按 Ctrl+D 结束:", file=sys.stderr)
        text = sys.stdin.read()
    try:
        secret = reveal(text)
        print(f"隐藏的秘密: {secret}")
    except ValueError as e:
        print(f"解码失败: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='ASCII 画隐写器 —— 把密码藏进 ASCII 画里')
    sub = parser.add_subparsers(dest='command', required=True)

    sub.add_parser('pics', help='列出所有内置 ASCII 画').set_defaults(func=cmd_pics)

    p_enc = sub.add_parser('encode', help='把秘密藏进 ASCII 画或字')
    p_enc.add_argument('--pic', '-p', help='画系统: 内置画名 (cat/dog/heart/...)')
    p_enc.add_argument('--text', '-t', help='字系统: 渲染成块字母大字')
    p_enc.add_argument('--art-file', help='自定义: 用自己的 ASCII 画文件')
    p_enc.add_argument('--secret', '-s', required=True, help='要隐藏的秘密')
    p_enc.add_argument('--output', '-o', help='保存到文件')
    p_enc.set_defaults(func=cmd_encode)

    p_dec = sub.add_parser('decode', help='从 ASCII 画中提取秘密')
    p_dec.add_argument('input', nargs='?', help='含隐写的文件（默认读 stdin）')
    p_dec.set_defaults(func=cmd_decode)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
