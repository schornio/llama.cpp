# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for convert_hf_to_gguf.py
#
# Usage:
#   pyinstaller convert_hf_to_gguf.spec
#
# Or use the provided build script:
#   ./scripts/build_convert_hf_to_gguf.sh

import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# Collect all submodules and data for transformers and torch
# so that model architectures loaded at runtime are available.
hidden_imports = (
    collect_submodules('gguf')
    + collect_submodules('transformers')
    + collect_submodules('sentencepiece')
    + [
        'torch',
        'numpy',
        # Ensure the resource_tracker helper process is bundled so that the
        # multiprocessing module can relaunch it inside the frozen executable.
        'multiprocessing.resource_tracker',
        'multiprocessing.spawn',
    ]
)

datas = (
    collect_data_files('transformers')
    + collect_data_files('torch')
    + collect_data_files('sentencepiece')
    + collect_data_files('gguf')
    # Include the local gguf-py package explicitly so PyInstaller can find it
    # even if it is not installed in the active environment.
    + [('gguf-py/gguf', 'gguf')]
)

a = Analysis(
    ['convert_hf_to_gguf.py'],
    pathex=[
        os.path.abspath('.'),
        os.path.abspath('gguf-py'),
    ],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=['pyinstaller_hooks/rthook_multiprocessing.py'],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='convert_hf_to_gguf',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
