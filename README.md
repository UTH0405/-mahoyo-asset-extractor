# mahoyo-asset-extractor

> **Extract and prepare assets from Witch on the Holy Night for visual novel engines like Ren'Py.**
>
> ⚠️ **This repository contains NO copyrighted game assets. You must own a legal copy of the game.**

[English](#english) | [中文](#chinese) | [日本語](#japanese)

---

## English

### What This Is

A set of Python tools to **extract assets from your legally purchased copy** of *Witch on the Holy Night* (魔法使いの夜 / Mahoutsukai no Yoru) and prepare them for use in fan-made visual novels built with Ren'Py or similar engines.

Supports the **Steam version** (HuneX Gengine / `HUNEXGGEFA10` format). If you own the game on another platform, please check your installation directory for the same `data*.hfa` archive files.

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
- **A legal copy of** *Witch on the Holy Night* (purchased on [Steam](https://store.steampowered.com/app/2052410/) or other platforms)

### Quick Start

```bash
# 1. Clone this repo
git clone https://github.com/UTH0405/-mahoyo-asset-extractor.git
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

### Customizing Game Path

If your game is installed in a non-default location, edit the top of **`extract_batch.py`**:

```python
# In extract_batch.py, around line 40 — change these two variables:
GAME_DIR = "D:/Program Files (x86)/Steam/steamapps/common/WITCH ON THE HOLY NIGHT"
OUT_BASE = "./extracted_assets"
```

| Variable | What to set | Example (Steam on another drive) |
|----------|-------------|----------------------------------|
| `GAME_DIR` | Your game's root folder — the one containing `data*.hfa` files | `"E:/SteamLibrary/steamapps/common/WITCH ON THE HOLY NIGHT"` |
| `OUT_BASE` | Where extracted assets go (relative or absolute path) | `"./my_assets"` or `"C:/mahoyo_output"` |

For the audio converter, edit the default path at the bottom of **`hw_to_ogg.py`**:

```python
# In hw_to_ogg.py, main block:
audio_dir = "./extracted_assets/audio"   # Change this to match your OUT_BASE
```

### Output Structure

```
extracted_assets/
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
Game Directory
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
- This tool ONLY works with assets **you already own** through a legal purchase.
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

## 中文

### 这是什么

一套 Python 工具，用于**从你合法购买的正版**《魔法使之夜》中提取素材，并准备用于 Ren'Py 等引擎开发的同人视觉小说。

支持 **Steam 版**（HuneX Gengine / `HUNEXGGEFA10` 格式）。如果你在其他平台购买了游戏，请检查安装目录中是否包含同样的 `data*.hfa` 归档文件。

### 功能

- **批量 HFA 解包** — 一条命令提取全部 52 个 `.hfa` 归档文件
- **格式转换** — 自动将 `.mzp` → PNG、`.cbg` → PNG、`.ctd` → 文本
- **音频转换** — 将 `.hw`（HuneX音频格式）转为标准 `.ogg`
- **分类输出** — 自动按类型整理到 `images/`、`audio/`、`scripts/` 等目录
- **全剧本提取** — 解压全部4种语言剧本（英/日/简中/繁中）
- **Ren'Py 就绪** — 立绘命名规则直接兼容 `show` 命令

### 环境要求

- **Python ≥ 3.11**
- **pip 包**: `numpy`、`Pillow`
- **正版**《魔法使之夜》（在 [Steam](https://store.steampowered.com/app/2052410/) 或其他平台购买）

### 快速开始

```bash
# 1. 克隆本仓库
git clone https://github.com/UTH0405/-mahoyo-asset-extractor.git
cd mahoyo-asset-extractor

# 2. 安装依赖
pip install numpy Pillow

# 3. 克隆 mahoyo_tools（核心提取库）
git clone https://github.com/loicfrance/mahoyo_tools.git

# 4. 运行提取
python extract_batch.py

# 5. 转换音频
python hw_to_ogg.py
```

### 自定义游戏路径

如果你的游戏安装在其他位置，编辑 **`extract_batch.py`** 文件顶部的变量：

```python
# 在 extract_batch.py 约第40行 — 修改这两个变量：
GAME_DIR = "D:/Program Files (x86)/Steam/steamapps/common/WITCH ON THE HOLY NIGHT"
OUT_BASE = "./extracted_assets"
```

| 变量 | 含义 | 示例（Steam 在其他盘） |
|------|------|------------------------|
| `GAME_DIR` | 游戏根目录 — 包含 `data*.hfa` 文件的文件夹 | `"E:/SteamLibrary/steamapps/common/WITCH ON THE HOLY NIGHT"` |
| `OUT_BASE` | 提取输出目录（相对或绝对路径均可） | `"./my_assets"` 或 `"C:/mahoyo_output"` |

音频转换脚本同理，编辑 **`hw_to_ogg.py`** 底部的默认路径：

```python
# 在 hw_to_ogg.py 的主程序块中：
audio_dir = "./extracted_assets/audio"   # 改为与你的 OUT_BASE 匹配的路径
```

### 输出目录结构

```
extracted_assets/
├── images/              # 角色立绘、事件CG、UI (PNG)
├── backgrounds/         # 转场规则贴图 (PNG)
├── audio/               # BGM、音效、场景音频 (OGG)
├── videos/              # 开场动画 (MP4)
├── scripts_decompressed/# 四语言完整剧本 (TXT)
├── scripts_compiled/    # 编译后的游戏脚本 (CHS)
├── scripts_raw/         # 原始压缩脚本 (CTD)
└── fonts/               # 字体定义文件 (CCIT)
```

### 提取成果概要

| 素材类型 | 格式 | 数量 | Ren'Py 可用 |
|----------|:---:|:---:|:----------:|
| 角色立绘 | PNG | 14名角色, 6,200+差分 | ✅ |
| 事件CG | PNG | 5,980 | ✅ |
| UI 元素 | PNG | 6,080+ | ✅ |
| BGM 原声 | OGG | 81 首 | ✅ |
| 音效 | OGG | 3,800+ | ✅ |
| 英文剧本 | TXT | 24,134 行 | ✅ 参考用 |
| 开场动画 | MP4 | 2~5 个 | ✅ |

### 工作原理

```
游戏安装目录
  └── data*.hfa  (HuneX Gengine 归档)
        │
        ▼  extract_batch.py + mahoyo_tools
        │
  ┌─────┼──────────────────────────────┐
  ▼     ▼         ▼         ▼          ▼
PNG   OGG       TXT       MP4        Fonts
(立绘) (BGM)   (剧本)   (视频)     (字体)
```

### 法律声明

- **本仓库不包含任何游戏版权素材。**
- 此工具仅用于从你**合法购买的正版**中提取素材。
- 提取的所有素材版权均归 **TYPE-MOON / Aniplex / 奈須きのこ** 所有。
- 本工具仅供**个人学习、研究、非商业同人创作**使用。
- **严禁**在未经版权方授权的情况下二次分发游戏素材。
- 《魔法使之夜》© TYPE-MOON。保留所有权利。

### 致谢

- **mahoyo_tools** by [loicfrance](https://github.com/loicfrance/mahoyo_tools) — 核心 HFA 提取库
- **HunexFileArchiveTool** by [LinkOFF7](https://github.com/LinkOFF7/HunexFileArchiveTool) — 原始 C# 提取工具
- **nrvnqsr.com 社区** — 文件格式逆向工程研究
- Witch on the Holy Night / 魔法使いの夜 © TYPE-MOON

### 许可证

本项目的代码采用 **MIT 许可证**。详见 [LICENSE](LICENSE)。

提取的游戏素材版权归 TYPE-MOON 所有，**不在**本许可证的涵盖范围内。

---

## 日本語

### 概要

『魔法使いの夜』（魔法使いの夜 / Mahoutsukai no Yoru）を**合法的に購入された方**のためのPythonツールです。ゲームアセットを抽出し、Ren'Pyなどのビジュアルノベルエンジンで使用できる形式に変換します。

**Steam版**（HuneX Gengine / `HUNEXGGEFA10` 形式）に対応しています。他のプラットフォームで購入された場合も、インストールディレクトリに同じ `data*.hfa` アーカイブファイルが含まれていれば使用可能です。

### 機能

- **バッチHFA抽出** — 52個の`.hfa`アーカイブを1コマンドで一括抽出
- **フォーマット変換** — `.mzp`→PNG、`.cbg`→PNG、`.ctd`→テキストに自動変換
- **音声変換** — `.hw`（HuneX音声形式）を標準`.ogg`（Ogg Vorbis）に変換
- **整理出力** — `images/`、`audio/`、`scripts/`などに自動分類
- **全スクリプト抽出** — 4言語（英/日/簡体字/繁体字）の台本を解凍
- **Ren'Py対応** — 抽出された立ち絵はそのまま`show`コマンドで使用可能

### 必要条件

- **Python ≥ 3.11**
- **pipパッケージ**: `numpy`, `Pillow`
- **正規版**『魔法使いの夜』（[Steam](https://store.steampowered.com/app/2052410/)または他のプラットフォームで購入）

### クイックスタート

```bash
# 1. リポジトリをクローン
git clone https://github.com/UTH0405/-mahoyo-asset-extractor.git
cd mahoyo-asset-extractor

# 2. 依存関係のインストール
pip install numpy Pillow

# 3. mahoyo_tools（コア抽出ライブラリ）をクローン
git clone https://github.com/loicfrance/mahoyo_tools.git

# 4. 抽出を実行
python extract_batch.py

# 5. 音声を変換
python hw_to_ogg.py
```

### ゲームパスのカスタマイズ

ゲームがデフォルト以外の場所にインストールされている場合は、**`extract_batch.py`** の先頭付近を編集してください：

```python
# extract_batch.py の約40行目 — この2つの変数を変更：
GAME_DIR = "D:/Program Files (x86)/Steam/steamapps/common/WITCH ON THE HOLY NIGHT"
OUT_BASE = "./extracted_assets"
```

| 変数 | 説明 | 例（Steamが別ドライブの場合） |
|------|------|-------------------------------|
| `GAME_DIR` | ゲームのルートフォルダ — `data*.hfa` ファイルが含まれる場所 | `"E:/SteamLibrary/steamapps/common/WITCH ON THE HOLY NIGHT"` |
| `OUT_BASE` | 抽出先ディレクトリ（相対パスまたは絶対パス） | `"./my_assets"` または `"C:/mahoyo_output"` |

音声変換ツールも同様に、**`hw_to_ogg.py`** の下部にあるデフォルトパスを編集します：

```python
# hw_to_ogg.py のメインブロック内：
audio_dir = "./extracted_assets/audio"   # OUT_BASEに合わせて変更
```

### 出力構成

```
extracted_assets/
├── images/              # キャラクター立ち絵、CG、UI (PNG)
├── backgrounds/         # トランジション/ルール画像 (PNG)
├── audio/               # BGM、効果音、シーン音声 (OGG)
├── videos/              # オープニングムービー (MP4)
├── scripts_decompressed/# 4言語フルスクリプト (TXT)
├── scripts_compiled/    # コンパイル済みスクリプト (CHS)
├── scripts_raw/         # 生圧縮スクリプト (CTD)
└── fonts/               # フォント定義ファイル (CCIT)
```

### 抽出アセット概要

| アセット | 形式 | 数量 | Ren'Py対応 |
|----------|:---:|:---:|:--------:|
| キャラクター立ち絵 | PNG | 14名, 6,200+バリエーション | ✅ |
| シーンCG | PNG | 5,980 | ✅ |
| UI要素 | PNG | 6,080+ | ✅ |
| BGMサウンドトラック | OGG | 81曲 | ✅ |
| 効果音 | OGG | 3,800+ | ✅ |
| 英語スクリプト | TXT | 24,134行 | ✅ 参考用 |
| オープニングムービー | MP4 | 2~5 | ✅ |

### 仕組み

```
ゲームディレクトリ
  └── data*.hfa  (HuneX Gengineアーカイブ)
        │
        ▼  extract_batch.py + mahoyo_tools
        │
  ┌─────┼──────────────────────────────┐
  ▼     ▼         ▼         ▼          ▼
PNG   OGG       TXT       MP4        Fonts
(立ち絵)(BGM)  (台本)   (動画)     (フォント)
```

### 法的注意事項

- **このリポジトリには著作権で保護されたゲームアセットは一切含まれていません。**
- このツールは、**合法的に購入したゲーム**からのみアセットを抽出します。
- 抽出されたすべてのアセットの著作権は **TYPE-MOON / Aniplex / 奈須きのこ** に帰属します。
- このツールは**個人的・非商用の利用**（同人ビジュアルノベル制作、学習、研究など）のみを想定しています。
- 著作権者の許可なく抽出したアセットを再配布することは**固く禁じられています**。
- 『魔法使いの夜』© TYPE-MOON. All Rights Reserved.

### クレジット

- **mahoyo_tools** by [loicfrance](https://github.com/loicfrance/mahoyo_tools) — コアHFA抽出ライブラリ
- **HunexFileArchiveTool** by [LinkOFF7](https://github.com/LinkOFF7/HunexFileArchiveTool) — オリジナルC#抽出ツール
- **nrvnqsr.comコミュニティ** — ファイル形式リバースエンジニアリング研究
- 『魔法使いの夜』© TYPE-MOON

### ライセンス

本プロジェクトのコードは **MITライセンス** の下で公開されています。[LICENSE](LICENSE)を参照してください。

抽出されたゲームアセットの著作権はTYPE-MOONに帰属し、本ライセンスの対象**外**です。
