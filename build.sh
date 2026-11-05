#!/usr/bin/env bash
set -e

INPUT=${1:-examples/hello.fuck}
BASE=$(basename "$INPUT" .fuck)
SWIFT_OUT="build/${BASE}.swift"
BIN_OUT="build/${BASE}"

mkdir -p build

echo "[1/3] Transpiling $INPUT"
python3 fuckc.py "$INPUT" "$SWIFT_OUT"

echo "[2/3] Compiling with swiftc"
swiftc -O "$SWIFT_OUT" -o "$BIN_OUT"

echo "[3/3] Running"
"./$BIN_OUT"