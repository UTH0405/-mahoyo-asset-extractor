# Asset Structure Reference

> Complete documentation of Witch on the Holy Night (Steam) asset formats and extraction output.

---

## HFA Archive Format

**Magic**: `HUNEXGGEFA10` (HuneX Global Game Engine File Archive 1.0)

### Header Structure

```
Offset  Size  Description
0x00    12    Magic bytes "HUNEXGGEFA10"
0x0C    4     Entry count (uint32 LE)
0x10    0x60  Entry 0: filename (UTF-8, null-padded to 96 bytes)
0x70    32    Entry 0: data_offset, size + 6 reserved (8 × uint32 LE)
0x90    ...   Entry 1... (0x80 bytes per entry)
```

### Archive Listing

| Archive | Size | Contents |
|---------|------|----------|
| data00000.hfa | 150 MB | alphagradation*.cbg (background gradients) |
| data00010.hfa | 18 MB | rule_*.cbg (transition rules) |
| data00100.hfa | 26 MB | Font*.ccit (font definitions) |
| data00200.hfa | 3.1 MB | script_text_*.ctd (4-language scripts) |
| data00300.hfa | 0.1 MB | SSE*.hw (system sound effects) |
| data00400.hfa | 3.6 MB | logo.mp4 |
| data01000~data01400 | various | *.chs (compiled chapter scripts) |
| data02000~data02052 | 1.5-1.6 GB each | img*.mzp (scene CGs, backgrounds) |
| data02020 | 147 MB | Character sprite batch 1 |
| data02100~data02235 | 8-840 MB | Character sprites (individual .mzp) |
| data02300~data02400 | 0.2-7 MB | UI elements, color cards |
| data02900 | 1.5 GB | opening_*.mp4 |
| data03000 | 250 MB | m*.hw (BGM soundtrack, 81 tracks) |
| data03100 | 94 MB | editse_*.hw (scene audio cues) |
| data04000 | 525 MB | a10_*.hw (scene/action audio, 2902 clips) |

---

## File Format Reference

### `.mzp` → PNG (Images)

MZP is a compressed+tiled image format. `mahoyo_tools` handles:

- Tile-based compression (literal / RLE / back-reference)
- Palette-based images (≤256 colors)
- Alpha channel preservation
- Automatic PNG conversion

**Sprite naming convention**:
```
{char}_{pose}_{costume}_{expression}_{variant}_{scale}.png

Examples:
  aok_a_02_02_00.png       Aoko, pose A, costume 02, expression 02, variant 00
  ari_n_01_03_02_02.png    Alice, neutral, costume 01, expression 03, variant 02 (2x scale)
  sou_a_01_02_08_03_03.png Soujuurou, pose A, costume 01, expression 02, variant 08 (3x scale)
```

**Pose codes**:
| Code | Meaning |
|:----:|---------|
| `a` | Standard/Active |
| `n` | Neutral/Default |
| `l` | Laughing/Light |
| `m` | Medium |
| `s` | Sad/Surprised |

### `.hw` → OGG (Audio)

HuneX audio container: **64-byte header** + standard **Ogg Vorbis** stream.

```
Offset  Size  Description
0x00    4     Header size (always 0x40 = 64)
0x04    4     Magic "hw  "
0x08    4     Page count
0x0C    4     Total samples
0x10    4     Sample rate (e.g., 0xBB80 = 48000)
0x14    4     Channels (e.g., 0x02 = stereo)
0x40    ...   OggS... (standard Ogg Vorbis data)
```

To convert: strip first 64 bytes (or find first `OggS` marker) → save as `.ogg`.

### `.ctd` → TXT (Compiled Scripts)

LenZuCompressor format. Magic: `LenZuCompressor\0` at offset 0x00.

- LZ77 variant with Huffman coding
- Decompresses to UTF-8 text (game script with markup)

### `.cbg` → PNG (Compressed Backgrounds)

Custom compressed background format. Can be decoded into PNG by `mahoyo_tools`.

### `.chs` (Compiled Scripts)

HuneX compiled script format — not yet fully reverse-engineered for the PC version. Extracted as-is (binary).

### `.ccit` (Font Definitions)

Character position/size mapping files — used with MZP font texture atlases.

---

## Extracted Audio Categories

| Prefix | Count | Description |
|--------|:-----:|-------------|
| `m*.hw` | 81 | **BGM Soundtrack** (m01~m63, some with -s variants) |
| `se*.hw` | 878 | **Sound Effects** (environmental, combat, UI) |
| `a10_*_*.hw` | 2,902 | **Scene Audio Cues** (chapter-scene-action indexed) |
| `editse_*.hw` | 10 | **Edit Scene Effects** (transition/mixing cues) |
| `mixse_*.hw` | 18 | **Mixed Scene Audio** |
| `SSE*.hw` | 7 | **System Sound Effects** (confirm/cancel/page-turn) |

---

## Chapter Structure (from .chs files)

```
Chapter 1:    1_0 ~ 1_5 (main), 1dot5_1 ~ 1dot5_4 (interlude)
Chapter 2:    2_1 ~ 2_5
Chapter 3:    3_1 (single scene)
Chapter 4:    4_1 ~ 4_4
Chapter 5:    5a_1~12 + 5b_1~16 (split route)
Chapter 6:    6_1 ~ 6_9
Chapter 7:    7_1 ~ 7_8 + 7_ex
Chapter 8:    8_1 ~ 8_6 + 8_ex + 8dot5
Chapter 9:    9_0 ~ 9_8
Chapter 10:   a_0 ~ a_8
Chapter 11:   b_1 ~ b_9
Chapter 12:   c_0 ~ c_15
Chapter 13:   d_1 ~ d_9
Extra:        nz1~nz6, sp1~sp2, opening, staffroll
Bonus:        teatime1~teatimec (13 tea time side stories)
Wiki:         200+ terminology entries
```

---

## Character Code Reference

| Code | Full Name | JP | Role |
|:----:|-----------|----|------|
| `aok` | Aoko Aozaki | 蒼崎青子 | Protagonist |
| `ari` | Alice Kuonji | 久遠寺有珠 | Heroine |
| `sou` | Soujuurou Shizuki | 静希草十郎 | Protagonist |
| `tou` | Touko Aozaki | 蒼崎橙子 | Major supporting |
| `beo` | Beowulf | ベオウルフ | Supporting |
| `yui` | Yui | ゆい | Supporting |
| `eir` | Eiri | エイリ | Supporting |
| `koj` | Kojirou? | ? | Supporting |
| `rid` | Riddell? | ? | Supporting |
| `rit` | Ritsuka? | ? | Supporting |
| `tob` | Tobimaru? | ? | Supporting |
| `tok` | Tokitsu? | ? | Supporting |
| `yam` | Yamashiro? | ? | Supporting |
| `kin` | Kin? | ? | Supporting |
