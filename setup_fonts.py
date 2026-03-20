"""
Font Setup Script - Downloads Hindi-compatible fonts for Velocity Hindi
Run this once to download required fonts, or on GitHub Actions
"""

import os
from pathlib import Path
import urllib.request

BASE_DIR = Path(__file__).parent
FONTS_DIR = BASE_DIR / "fonts"
FONTS_DIR.mkdir(exist_ok=True)

# Font URLs (Google Fonts - Apache License 2.0)
FONTS = {
    "NotoSansDevanagari-Bold.ttf": "https://github.com/google/fonts/raw/main/ofl/notosansdevanagari/NotoSansDevanagari%5Bwght%5D.ttf",
    "NotoSansDevanagari-Regular.ttf": "https://github.com/google/fonts/raw/main/ofl/notosansdevanagari/NotoSansDevanagari%5Bwght%5D.ttf",
}

def download_font(name, url):
    """Download a font file"""
    font_path = FONTS_DIR / name
    if font_path.exists():
        print(f"✓ Font already exists: {name}")
        return str(font_path)
    
    try:
        print(f"Downloading {name}...")
        urllib.request.urlretrieve(url, str(font_path))
        print(f"✓ Downloaded: {name}")
        return str(font_path)
    except Exception as e:
        print(f"✗ Failed to download {name}: {e}")
        return None

def setup():
    """Download all required fonts"""
    print("="*60)
    print("🔧 Setting up fonts for Velocity Hindi")
    print("="*60)
    
    downloaded = {}
    for name, url in FONTS.items():
        path = download_font(name, url)
        if path:
            downloaded[name] = path
    
    print("\n" + "="*60)
    if len(downloaded) == len(FONTS):
        print("✅ All fonts downloaded successfully!")
        print(f"📁 Fonts directory: {FONTS_DIR}")
    else:
        print("⚠️  Some fonts failed to download")
        print("💡 You can manually download fonts from Google Fonts")
    print("="*60)
    
    return downloaded

if __name__ == "__main__":
    setup()
