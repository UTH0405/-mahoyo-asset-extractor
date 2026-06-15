# mahoyo-asset-extractor

> **Extract and prepare assets from Witch on the Holy Night (Steam) for visual novel engines like Ren'Py.**
>
> ⚠️ **This repository contains NO copyrighted game assets. You must own a legal copy of the game on Steam.**

[English](#english) | [中文](#chinese) | [日本語](#japanese)

---

## English

### What This Is

A set of Python tools to **extract assets from your legally purchased Steam copy** of *Witch on the Holy Night* (魔法使いの夜 / Mahoutsukai no Yoru) and prepare them for use in fan-made visual novels built with Ren'Py or similar engines.

### Features

- **Batch HFA Extraction** — Extract all 52 `.hfa` archives with a single command
- **Format Conversion** — Auto-converts `.mzp` → PNG, `.cbg` → PNG, `.ctd` → text
- **Audio Conversion** — Converts `.hw` (HuneX audio) to standard `.ogg` (Ogg Vorbis)
- **Organized Output** — Automatically sorts assets into `images/`, `audio/`, `scripts/`, etc.
- **Full Script Extraction** — Decompresses all 4 language scripts (EN / JA / ZH-CN / ZH-TW)
- **Ren'Py-Ready** — Extracted sprites follow naming conventions ready for `show` commands

### Requirements

- **Python ≥ 3.11**
- **pip packages**: `numpy`, `Pillow`
- **A Steam copy of** *Witch on the Holy Night* (purchased on [Steam](https://store.steampowered.com/app/2052410/))

### Quick Start

```bash
# 1. Clone this repo
git clone https://github.com/YOUR_USERNAME/mahoyo-asset-extractor.git
cd mahoyo-asset-extractor

# 2. Install dependencies
pip install numpy Pillow

# 3. Clone mahoyo_tools (the core extraction library)
git clone https://github.com/loicfrance/mahoyo_tools.git

# 4. Run extraction
python extract_batch.py

# 5. Convert audio
python hw_to_ogg.py
```

### Output Structure

```
D:\mahoyo_extracted\assets\
├── images/              # Character sprites, CGs, UI (PNG)
├── backgrounds/         # Transition/rule images (PNG)
├── audio/               # BGM, SFX, scene audio (OGG)
├── videos/              # Opening movies (MP4)
├── scripts_decompressed/# Full scripts in 4 languages (TXT)
├── scripts_compiled/    # Compiled game scripts (CHS)
├── scripts_raw/         # Raw compressed scripts (CTD)
└── fonts/               # Font definition files (CCIT)
```

### Extracted Assets Summary

| Asset | Format | Count | Ready for Ren'Py |
|-------|:------:|:-----:|:----------------:|
| Character Sprites | PNG | 14 chars, 6,200+ variants | ✅ |
| Scene CGs | PNG | 5,980 | ✅ |
| UI Elements | PNG | 6,080+ | ✅ |
| BGM Soundtrack | OGG | 81 tracks | ✅ |
| Sound Effects | OGG | 3,800+ | ✅ |
| English Script | TXT | 24,134 lines | ✅ Reference |
| Opening Movies | MP4 | 2~5 | ✅ |

### How It Works

```
Steam Game Directory
  └── data*.hfa  (HuneX Gengine Archives)
        │
        ▼  extract_batch.py + mahoyo_tools
        │
  ┌─────┼──────────────────────────────┐
  ▼     ▼         ▼         ▼          ▼
PNG   OGG       TXT       MP4        Fonts
(立绘) (BGM)   (剧本)   (视频)     (字体)
```

### Legal Disclaimer

- **This repository does NOT contain any copyrighted game assets.**
- This tool ONLY works with assets **you already own** through a legal Steam purchase.
- All extracted assets remain the intellectual property of **TYPE-MOON / Aniplex / Kinoko Nasu**.
- This tool is intended for **personal, non-commercial use only** (e.g., fan-made visual novels, learning, research).
- Redistribution of extracted game assets is **strictly prohibited** without authorization from the copyright holders.
- **Witch on the Holy Night** is © TYPE-MOON. All rights reserved.

### Credits

- **mahoyo_tools** by [loicfrance](https://github.com/loicfrance/mahoyo_tools) — The core HFA extraction library
- **HunexFileArchiveTool** by [LinkOFF7](https://github.com/LinkOFF7/HunexFileArchiveTool) — Original C# extraction tool
- **nrvnqsr.com community** — File format reverse engineering research
- Witch on the Holy Night / 魔法使いの夜 © TYPE-MOON

### License

This project's code is released under the **MIT License**. See [LICENSE](LICENSE).

The extracted game assets are © TYPE-MOON and are NOT covered by this license.

---

## Chinese

### 这是什么

一套 Python 工具，用于**从你合法购买的 Steam 正版**《魔法使之夜》中提取素材，并准备用于 Ren'Py 等引擎开发的同人视觉小说。

### 功能

- **批量 HFA 解包** — 一条命令提取全部 52 个 `.hfa` 归档文件
- **格式转换** — 自动将 `.mzp` → PNG、`.cbg` → PNG、`.ctd` → 文本
- **音频转换** — 将 `.hw`（HuneX音频格式）转为标准 `.ogg`
- **分类输出** — 自动按类型整理到 `images/`、`audio/`、`scripts/` 等目录
- **全剧本提取** — 解压全部4种语言剧本（英语/日语/简中/繁中）
- **Ren'Py 就绪** — 立绘命名规则直接兼容 `show` 命令

### 使用方法

```bash
# 1. 克隆本仓库
git clone https://github.com/YOUR_USERNAME/mahoyo-asset-extractor.git
cd mahoyo-asset-extractor

# 2. 安装依赖
pip install numpy Pillow

# 3. 克隆 mahoyo_tools（核心提取库）
git clone https://github.com/loicfrance/mahoyo_tools.git

# 4. 运行提取（确保游戏已安装在 Steam 默认路径）
python extract_batch.py

# 5. 转换音频
python hw_to_ogg.py
```

### 法律声明

- **本仓库不包含任何游戏版权素材。**
- 此工具仅用于从你**合法购买的 Steam 正版**中提取素材。
- 提取的所有素材版权均归 **TYPE-MOON / Aniplex / 奈須きのこ** 所有。
- 本工具仅供**个人学习、研究、非商业同人创作**使用。
- **严禁**在未经版权方授权的情况下二次分发游戏素材。
- 《魔法使之夜》© TYPE-MOON。保留所有权利。

---

## Japanese

### 概要

『魔法使いの夜』（Steam版）から合法的にアセットを抽出し、Ren'Pyなどのビジュアルノベルエンジンで使用できるようにするPythonツールです。

### 法的注意事項

- **このリポジトリには著作権で保護されたゲームアセットは一切含まれていません。**
- このツールは、**Steamで合法的に購入したゲーム**からのみアセットを抽出します。
- 抽出されたすべてのアセットの著作権は **TYPE-MOON / Aniplex / 奈須きのこ** に帰属します。
- このツールは**個人的・非商用の利用**（同人ビジュアルノベル制作、学習、研究など）のみを想定しています。
- 著作権者の許可なく抽出したアセットを再配布することは**固く禁じられています**。
- 『魔法使いの夜』© TYPE-MOON. All Rights Reserved.
