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

# Font URLs - Multiple sources for reliability
# Using jsDelivr CDN (more reliable than raw GitHub)
FONTS = {
    "NotoSansDevanagari-Bold.ttf": "https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/notosansdevanagari/NotoSansDevanagari%5Bwght%5D.ttf",
    "NotoSansDevanagari-Regular.ttf": "https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/notosansdevanagari/NotoSansDevanagari%5Bwght%5D.ttf",
}

# Alternative fallback URLs
FALLBACK_URLS = {
    "NotoSansDevanagari-Bold.ttf": [
        "https://raw.githubusercontent.com/google/fonts/main/ofl/notosansdevanagari/NotoSansDevanagari%5Bwght%5D.ttf",
        "https://fonts.cdnfonts.com/download/Noto-Sans-Devanagari",
    ]
}

def download_font_with_retry(name, url, fallback_urls=None, max_retries=3):
    """Download a font file with retries and fallback URLs"""
    font_path = FONTS_DIR / name
    
    if font_path.exists() and font_path.stat().st_size > 1000:
        print(f"✓ Font already exists: {name}")
        return str(font_path)
    
    # Try primary URL
    urls_to_try = [url]
    if fallback_urls:
        urls_to_try.extend(fallback_urls)
    
    for try_url in urls_to_try:
        for attempt in range(max_retries):
            try:
                print(f"Downloading {name} from {try_url[:50]}... (attempt {attempt + 1})")
                urllib.request.urlretrieve(try_url, str(font_path))
                
                # Verify download
                if font_path.exists() and font_path.stat().st_size > 1000:
                    print(f"✓ Downloaded: {name} ({font_path.stat().st_size / 1024:.1f} KB)")
                    return str(font_path)
                else:
                    print(f"⚠ Downloaded file too small, retrying...")
                    font_path.unlink()
            except Exception as e:
                print(f"✗ Attempt {attempt + 1} failed: {e}")
                if font_path.exists():
                    font_path.unlink()
    
    print(f"✗ Failed to download {name} after all attempts")
    return None

def setup():
    """Download all required fonts"""
    print("="*60)
    print("🔧 Setting up fonts for Velocity Hindi")
    print("="*60)
    
    downloaded = {}
    for name, url in FONTS.items():
        fallbacks = FALLBACK_URLS.get(name, [])
        path = download_font_with_retry(name, url, fallbacks)
        if path:
            downloaded[name] = path
    
    print("\n" + "="*60)
    if len(downloaded) == len(FONTS):
        print("✅ All fonts downloaded successfully!")
        print(f"📁 Fonts directory: {FONTS_DIR}")
        print(f"\n📝 Font files:")
        for name, path in downloaded.items():
            size = Path(path).stat().st_size / 1024
            print(f"   • {name} ({size:.1f} KB)")
    else:
        print("⚠️  Some fonts failed to download")
        print("💡 The script will use system fonts as fallback")
        print("💡 You can manually download fonts from Google Fonts")
    print("="*60)
    
    return downloaded

if __name__ == "__main__":
    setup()
