#!/usr/bin/env python3
"""F-kLang -> Swift 转译器"""
import sys
import re

KEYWORDS = {
    r'\bfuck\b': 'func',
    r'\bdamn\b': 'let',
    r'\bshit\b': 'var',
    r'\bscrew\b': 'print',
    r'\bwhatever\b': 'if',
    r'\botherwise\b': 'else',
    r'\bagain\b': 'while',
    r'\bbullshit\b': 'return',
    r'\bassf\b': 'Double',
    r'\bass\b': 'Int',
    r'\bwords\b': 'String',
    r'\btruth\b': 'Bool',
}

def transpile(source: str) -> str:
    lines = []
    for line in source.splitlines():
        parts = line.split('"')
        for i in range(len(parts)):
            if i % 2 == 0:
                for pat, repl in KEYWORDS.items():
                    parts[i] = re.sub(pat, repl, parts[i])
        lines.append('"'.join(parts))
    return '\n'.join(lines) + '\n'

def main():
    if len(sys.argv) != 3:
        print("usage: fuckc <input.fuck> <output.swift>")
        sys.exit(1)
    src_path, dst_path = sys.argv[1], sys.argv[2]
    with open(src_path, encoding='utf-8') as f:
        src = f.read()
    swift = transpile(src)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(swift)
    print(f"[fuckc] {src_path} -> {dst_path}")

if __name__ == '__main__':
    main()