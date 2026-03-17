#!/usr/bin/env bash
# Build script for convert_hf_to_gguf.py
#
# Packages convert_hf_to_gguf.py into a single self-contained executable
# using PyInstaller.  The resulting binary is written to:
#   dist/convert_hf_to_gguf   (Linux / macOS)
#   dist\convert_hf_to_gguf.exe  (Windows)
#
# Prerequisites:
#   pip install pyinstaller
#   pip install -r requirements/requirements-convert_hf_to_gguf.txt
#
# Usage:
#   ./scripts/build_convert_hf_to_gguf.sh [extra pyinstaller options]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

cd "${REPO_ROOT}"

# Ensure PyInstaller is available
if ! command -v pyinstaller &>/dev/null; then
    echo "PyInstaller not found. Installing..." >&2
    pip install pyinstaller
fi

echo "Building convert_hf_to_gguf executable with PyInstaller..."

pyinstaller \
    --noconfirm \
    "${REPO_ROOT}/convert_hf_to_gguf.spec" \
    "$@"

echo ""
echo "Build complete. Executable is located at:"
echo "  ${REPO_ROOT}/dist/convert_hf_to_gguf"
