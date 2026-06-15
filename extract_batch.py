#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mahoyo-asset-extractor — Batch HFA Archive Extractor
=====================================================
Extracts all assets from a legally purchased Steam copy of
Witch on the Holy Night (魔法使いの夜).

Usage:  python extract_batch.py
Requires: Python >= 3.11, numpy, Pillow, mahoyo_tools

The script expects the game to be installed at Steam's default path:
  D:/Program Files (x86)/Steam/steamapps/common/WITCH ON THE HOLY NIGHT
Edit GAME_DIR below if your installation differs.

Supported conversions:
  .mzp → .png   (character sprites, CGs, UI elements)
  .cbg → .png   (background gradients, transition rules)
  .ctd → .txt   (LenZu-compressed game scripts)
  .chs, .hw, .mp4, .ccit → raw extraction

IMPORTANT: This tool does NOT include any copyrighted game assets.
You MUST own a legal Steam copy of Witch on the Holy Night to use it.
Redistribution of extracted assets is PROHIBITED.

Witch on the Holy Night © TYPE-MOON. All rights reserved.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mahoyo_tools import hfa
from mahoyo_tools.mzp import MzpImage
from mahoyo_tools.cbg import CompressedBG
from mahoyo_tools.lenzu import lenzu_decompress
from io import BytesIO

# ===================================================================
# CONFIGURATION — Edit these paths if your setup differs
# ===================================================================

# Path to your Steam installation of Witch on the Holy Night
GAME_DIR = "D:/Program Files (x86)/Steam/steamapps/common/WITCH ON THE HOLY NIGHT"
# Alternative common paths (uncomment the one that matches):
# GAME_DIR = "C:/Program Files (x86)/Steam/steamapps/common/WITCH ON THE HOLY NIGHT"
# GAME_DIR = "E:/SteamLibrary/steamapps/common/WITCH ON THE HOLY NIGHT"

# Output directory for extracted assets
OUT_BASE = "./extracted_assets"

CATEGORIES = {
    "mzp": "images",
    "cbg": "backgrounds",
    "ctd": "scripts_decompressed",
    "chs": "scripts_compiled",
    "hw":  "audio",
    "mp4": "videos",
    "ccit":"fonts",
    "c":   "scripts_raw",
}

def main():
    for d in list(CATEGORIES.values()) + ["other"]:
        os.makedirs(os.path.join(OUT_BASE, d), exist_ok=True)

    files = []
    for f in os.listdir(GAME_DIR):
        if f.endswith(".hfa"):
            fp = os.path.join(GAME_DIR, f)
            files.append((os.path.getsize(fp), f, fp))
    files.sort()

    total = len(files)
    ok = fail = 0
    total_raw = 0

    for idx, (size, name, path) in enumerate(files):
        print(f"\n[{idx+1}/{total}] {name} ({size/1048576:.1f} MB)")

        try:
            archive = hfa.HfaArchive(path)
            archive.open()

            for entry in archive:
                fname = entry.name
                if "." in fname:
                    ext = fname.rsplit(".", 1)[1].lower()
                else:
                    ext = ""

                cat = CATEGORIES.get(ext, "other")

                if ext == "mzp":
                    oname = fname[:-4] + ".png"
                elif ext == "cbg":
                    oname = fname[:-4] + ".png"
                elif ext == "ctd":
                    oname = fname[:-4] + ".txt"
                else:
                    oname = fname

                opath = os.path.join(OUT_BASE, cat, oname)

                if os.path.exists(opath):
                    continue

                entry.seek(0)

                try:
                    if ext == "mzp":
                        MzpImage(entry.data).img_write(opath)
                    elif ext == "cbg":
                        CompressedBG(entry.data).img_write(opath)
                    elif ext == "ctd" and entry.data[:16] == b"LenZuCompressor\0":
                        lenzu_decompress(BytesIO(entry.data), entry.size, opath)
                    else:
                        entry.to_file(opath)
                    total_raw += entry.size
                except Exception as conv_err:
                    # Fallback: extract raw
                    raw_path = opath
                    if ext in ("mzp", "cbg"):
                        raw_path = opath[:-4] + "." + ext
                    elif ext == "ctd":
                        raw_path = opath[:-4] + ".ctd"
                    try:
                        entry.to_file(raw_path)
                        total_raw += entry.size
                    except:
                        pass

            archive.close()
            ok += 1
            print(f"  [OK]")

        except Exception as e:
            fail += 1
            print(f"  [FAIL] {e}")

    print(f"\n===== EXTRACTION COMPLETE =====")
    print(f"Archives processed: {ok}/{total} (failed: {fail})")
    print(f"Raw data extracted: {total_raw/1048576:.0f} MB")

    print(f"\nAssets by category:")
    for cat in sorted(set(CATEGORIES.values()) | {"other"}):
        dp = os.path.join(OUT_BASE, cat)
        if os.path.isdir(dp):
            fs = os.listdir(dp)
            sz = sum(os.path.getsize(os.path.join(dp, x)) for x in fs)
            print(f"  {cat:25s}: {len(fs):5d} files, {sz/1048576:8.1f} MB")

if __name__ == "__main__":
    main()
