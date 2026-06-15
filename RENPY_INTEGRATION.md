# Ren'Py Integration Guide

> How to use extracted Witch on the Holy Night assets in your Ren'Py visual novel.

---

## Quick Setup

### 1. Directory Layout

Copy extracted assets into your Ren'Py project:

```
your_vn_project/
├── game/
│   ├── script.rpy
│   ├── images/
│   │   ├── sprites/       # Character sprites (from extracted images/)
│   │   ├── bg/            # Backgrounds (from extracted images/ + backgrounds/)
│   │   ├── cg/            # Event CGs (from extracted images/)
│   │   └── ui/            # UI elements (from extracted images/)
│   ├── audio/
│   │   ├── bgm/           # BGM (from extracted audio/m*.ogg)
│   │   ├── sfx/           # Sound effects (from extracted audio/se*.ogg)
│   │   └── voice/         # Voice (if using AI-generated voice)
│   └── fonts/             # Font files
```

### 2. Ren'Py Image Definitions

```renpy
# Character sprites — the extracted naming convention maps directly
# Format: {char}_{pose}_{costume}_{expression}_{variant}.png

# Aoko - standard pose
image aoko default = "sprites/aok_n_01_01_00.png"
image aoko smile = "sprites/aok_n_01_02_00.png"
image aoko angry = "sprites/aok_n_01_03_00.png"

# Aoko - active pose
image aoko active neutral = "sprites/aok_a_02_01_00.png"
image aoko active smile = "sprites/aok_a_02_02_00.png"

# Alice - neutral pose
image alice default = "sprites/ari_n_01_01_00.png"
image alice smirk = "sprites/ari_n_01_02_00.png"

# Soujuurou
image soujuurou default = "sprites/sou_n_01_01_00.png"
image soujuurou surprised = "sprites/sou_n_01_02_00.png"

# Backgrounds
image bg mansion day = "bg/img0100.png"
image bg mansion night = "bg/img0101.png"
image bg school = "bg/img0200.png"
```

### 3. Using Sprites with Transforms

```renpy
# Position transforms matching the original game layout
transform left:
    xalign 0.25
    yalign 1.0

transform center:
    xalign 0.5
    yalign 1.0

transform right:
    xalign 0.75
    yalign 1.0

# Usage in script
show aoko default at left
show alice smirk at right
with dissolve

aoko "...So you're here too."
alice "Obviously."
```

### 4. Audio Setup

```renpy
# BGM
define audio.bgm_daily = "audio/bgm/m01.ogg"
define audio.bgm_tense = "audio/bgm/m06.ogg"
define audio.bgm_battle = "audio/bgm/m08.ogg"

# Sound effects
define audio.sfx_confirm = "audio/sfx/SSEDecided.ogg"
define audio.sfx_page = "audio/sfx/SSETurnedPage.ogg"

# Usage
play music bgm_daily fadein 1.0
play sound sfx_page
```

### 5. BGM Reference (Partial Track List)

```
m01   — 星が瞬くこんな夜に (Main Theme)
m02   — (Daily/Calm)
m03   — (Mystery/Tension)
m06   — (Action/Tension)
m08   — Five (Battle Theme)
m17   — (Climax)
... (81 tracks total)
```

---

## Sprite Variant Guide

### Understanding the Naming Convention

```
aok_n_01_02_00.png
 │   │  │  │  └─ Scale variant (00=1x, 01=1x alt, 02=2x, 03=3x)
 │   │  │  └──── Expression (01=default, 02=smile, 03=angry, etc.)
 │   │  └─────── Costume/Outfit
 │   └────────── Pose (n=neutral, a=active, l=laughing, s=sad, m=medium)
 └────────────── Character code
```

### Expression Mapping

Each character has different available expressions. Common patterns:

| Code | Expression | Usage |
|:----:|------------|-------|
| 01 | Default/Neutral | Standard scenes |
| 02 | Smile/Happy | Light-hearted moments |
| 03 | Angry/Annoyed | Conflict/Tsundere moments |
| 04 | Surprised/Shocked | Reveal scenes |
| 05 | Sad/Wistful | Emotional scenes |
| 06 | Blushing/Embarrassed | Romantic scenes |
| 07 | Serious/Determined | Action scenes |
| 08+ | Special variants | Character-specific |

### Scale Variants

- `00` or no suffix = 1x (standard size)
- `01` = 1x alternate
- `02_02` = 2x scale (larger, for close-up scenes)
- `03_03` = 3x scale (very large, for dramatic close-ups)

---

## Scene Audio Cue Integration

The extracted `a10_*` audio files are indexed by chapter-scene:

```
a10_1_1_0000.ogg  → Chapter 1, Scene 1, Cue 0000
a10_5a_11_0001.ogg → Chapter 5a, Scene 11, Cue 0001
```

These are pre-mixed audio cues that combine BGM + ambience for specific scenes. You can:

1. **Use directly** — Drop them into scenes for authentic audio
2. **Reference** — Study the cue timing for your own scenes
3. **Remix** — Extract BGM and SFX separately for custom combinations

---

## Performance Tips

### Image Optimization

```bash
# The extracted PNGs are high-resolution. For Ren'Py, consider:
# 1. Downscaling to your target resolution
# 2. Using Ren'Py's image cache
# 3. Converting large BGs to WebP

# Batch resize to 1920px width (ImageMagick)
mogrify -resize 1920x *.png

# Or in Ren'Py config:
define config.image_cache_size = 400  # Increase cache for large sprites
```

### Audio Optimization

```bash
# The .ogg files are already compressed. For voice lines, use mono:
ffmpeg -i input.ogg -ac 1 -b:a 64k output.ogg
```

---

## Legal Notes for Your Project

When using these assets in a Ren'Py project:

1. **Do NOT redistribute the assets** — Your project should only contain your original content
2. **Require users to own the game** — Use a launcher that checks for Steam installation
3. **Add proper credits** — Include TYPE-MOON copyright notice
4. **Non-commercial only** — Fan works using these assets must be free

### Example Credit Screen

```renpy
label credits:
    "This fan work uses assets from:"
    "Witch on the Holy Night"
    "© TYPE-MOON"
    "Original BGM by Hideyuki Fukasawa"
    ""
    "This is a non-commercial fan project."
    "Please support the original work on Steam."
```
