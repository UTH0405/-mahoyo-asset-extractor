#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mahoyo-asset-extractor — HW Audio Converter
=============================================
Converts .hw (HuneX audio container) files to standard .ogg (Ogg Vorbis).

Usage:  python hw_to_ogg.py [audio_directory]

Format: .hw = 64-byte HuneX header + standard Ogg Vorbis stream.
Multi-stream HW files (e.g., BGM containers) are auto-split.

IMPORTANT: This tool does NOT include any copyrighted audio assets.
You MUST own a legal Steam copy of Witch on the Holy Night to use it.
Redistribution of extracted audio is PROHIBITED.

Witch on the Holy Night © TYPE-MOON. All rights reserved.
"""

import os
import sys
import struct

def hw_to_ogg(hw_path, ogg_path=None, split_streams=True):
    """
    Convert a .hw file to .ogg file(s).
    Returns list of output files.
    """
    if ogg_path is None:
        ogg_path = hw_path[:-3] + ".ogg"

    with open(hw_path, "rb") as f:
        data = f.read()

    # Find the first OggS marker
    ogg_start = data.find(b"OggS")
    if ogg_start == -1:
        print(f"  WARNING: No OggS found in {hw_path}")
        return []

    # Skip the HuneX header (everything before first OggS)
    ogg_data = data[ogg_start:]

    if not split_streams:
        with open(ogg_path, "wb") as f:
            f.write(ogg_data)
        return [ogg_path]

    # Split into individual Ogg streams by detecting stream serial numbers
    # Each Ogg page: "OggS" (4) + version (1) + flags (1) + granule (8) + serial (4) + page_num (4) + checksum (4) + segments (1) + segment_table (N) + data
    # Multiple streams have different serial numbers and restart page numbering
    streams = []
    pos = 0
    current_serial = None
    current_stream_start = 0

    while pos < len(ogg_data):
        if ogg_data[pos:pos+4] != b"OggS":
            pos += 1
            continue

        # Extract serial number at offset +14 from OggS
        page_start = pos
        serial = struct.unpack_from("<I", ogg_data, page_start + 14)[0]

        if current_serial is None:
            current_serial = serial
            current_stream_start = page_start
        elif serial != current_serial:
            # New stream detected
            stream_data = ogg_data[current_stream_start:page_start]
            streams.append((current_serial, stream_data))
            current_serial = serial
            current_stream_start = page_start

        # Move to next page (skip segment table)
        if page_start + 26 > len(ogg_data):
            break
        num_segments = ogg_data[page_start + 26]
        page_size = 27 + num_segments
        # Data size is sum of segment sizes
        data_size = sum(ogg_data[page_start+27+i] for i in range(num_segments))
        page_size += data_size
        pos = page_start + page_size

    # Save last stream
    if current_stream_start < len(ogg_data):
        stream_data = ogg_data[current_stream_start:]
        streams.append((current_serial, stream_data))

    if len(streams) <= 1:
        # Single stream - just strip header
        with open(ogg_path, "wb") as f:
            f.write(ogg_data)
        return [ogg_path]
    else:
        # Multiple streams - save as separate files
        base = ogg_path[:-4] if ogg_path.endswith(".ogg") else ogg_path
        outputs = []
        for i, (serial, sdata) in enumerate(streams):
            if i == 0:
                spath = ogg_path
            else:
                spath = f"{base}_{i}.ogg"
            with open(spath, "wb") as f:
                f.write(sdata)
            outputs.append(spath)
        print(f"  Split into {len(outputs)} streams: {os.path.basename(hw_path)}")
        return outputs


def batch_convert(audio_dir, output_dir=None):
    """Convert all .hw files in a directory to .ogg."""
    if output_dir is None:
        output_dir = audio_dir

    os.makedirs(output_dir, exist_ok=True)

    hw_files = []
    for root, dirs, files in os.walk(audio_dir):
        for f in files:
            if f.endswith(".hw"):
                hw_files.append(os.path.join(root, f))

    if not hw_files:
        print("No .hw files found.")
        return

    print(f"Found {len(hw_files)} .hw files\n")
    total = len(hw_files)
    converted = 0
    failed = 0

    for i, hw_path in enumerate(hw_files):
        fname = os.path.basename(hw_path)
        size = os.path.getsize(hw_path)
        ogg_path = os.path.join(output_dir, fname[:-3] + ".ogg")

        print(f"[{i+1}/{total}] {fname} ({size/1024:.1f} KB)")

        try:
            results = hw_to_ogg(hw_path, ogg_path)
            if results:
                converted += 1
                for r in results:
                    rsize = os.path.getsize(r)
                    print(f"  -> {os.path.basename(r)} ({rsize/1024:.1f} KB)")
            else:
                failed += 1
                print(f"  -> FAILED")
        except Exception as e:
            failed += 1
            print(f"  -> ERROR: {e}")

    print(f"\nConverted: {converted}/{total}, Failed: {failed}")


if __name__ == "__main__":
    audio_dir = "./extracted_assets/audio"
    if len(sys.argv) > 1:
        audio_dir = sys.argv[1]

    print("=" * 50)
    print("  HW -> OGG Audio Converter")
    print("=" * 50)
    batch_convert(audio_dir)
