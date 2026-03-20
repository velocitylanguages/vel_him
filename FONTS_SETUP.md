# 🔤 Font Setup for Velocity Hindi

This document explains how Hindi (Devanagari) fonts are handled in Velocity Hindi.

---

## ✅ Automatic Font Handling

The project automatically finds and uses appropriate Hindi fonts on different platforms:

### GitHub Actions (Ubuntu Linux)
- **Font**: Noto Sans Devanagari
- **Installation**: Automatically installed via workflow (`fonts-noto-devanagari` package)
- **Path**: `/usr/share/fonts/truetype/noto/NotoSansDevanagari-Bold.ttf`

### Windows (Local Development)
- **Primary**: Nirmala.ttf (built-in Windows Hindi font)
- **Fallback**: Mangal.ttf (older Windows Hindi font)
- **Path**: `C:/Windows/Fonts/Nirmala.ttf`

### Custom Fonts (Optional)
- **Location**: `fonts/` directory in project root
- **Fonts**: NotoSansDevanagari-Bold.ttf, NotoSansDevanagari-Regular.ttf
- **Download**: Run `python setup_fonts.py` to download fonts

---

## 🖥️ Local Testing

### Windows
No setup required! Windows includes Hindi fonts by default.

### macOS
You may need to install a Hindi font:
```bash
# Using Homebrew
brew install --cask font-noto-sans-devanagari

# Or download from Google Fonts manually
```

### Linux (Non-Ubuntu)
Install Noto Sans Devanagari:
```bash
# Debian/Ubuntu
sudo apt-get install fonts-noto-devanagari

# Fedora/RHEL
sudo dnf install google-noto-sans-devanagari-fonts

# Arch Linux
sudo pacman -S noto-fonts
```

---

## ☁️ GitHub Actions Setup

The workflow automatically installs Hindi fonts. No additional setup needed!

```yaml
- name: 📦 Install system dependencies
  run: |
    sudo apt-get update
    sudo apt-get install -y ffmpeg fonts-noto-devanagari
```

---

## 🎨 Font Hierarchy

The code uses different fonts for different text elements:

| Element | Font Type | Size | Purpose |
|---------|-----------|------|---------|
| Category (English) | Any bold font | 60px | Top category label |
| English Text | Any bold font | 85px | English phrase |
| **Hindi Text** | **Devanagari font** | **85px** | **Hindi translation** |
| Pronunciation | Regular font | 42px | Phonetic guide |
| Branding | Any bold font | 52px | "VELOCITY HINDI" |

---

## 🔧 Troubleshooting

### Hindi Text Shows as Squares/Boxes
This means the font doesn't support Devanagari script.

**Solution:**
1. On GitHub Actions: Ensure `fonts-noto-devanagari` is installed
2. On Windows: Nirmala.ttf should be available by default
3. On macOS: Install Noto Sans Devanagari font

### Font Loading Errors
Check the logs for font path issues.

**Solution:**
```bash
# Verify font installation (Ubuntu)
fc-list | grep -i "noto\|devanagari"

# List available fonts (Windows PowerShell)
Get-Font | Where-Object {$_.Name -like "*Nirmala*" -or $_.Name -like "*Mangal*"}
```

---

## 📦 Font Files

If you want to manually download fonts:

1. **Noto Sans Devanagari** (Google Fonts - Free, Apache 2.0)
   - https://fonts.google.com/noto/specimen/Noto+Sans+Devanagari
   - Download and place in `fonts/` directory

2. **Mukti Narrow** (Alternative, Free)
   - https://github.com/bengali-fonts/MuktiFont
   - Good fallback option

---

## ✅ Verification

After setup, run a test generation:
```bash
python -c "from facebook_reels_automation import generate_reel; generate_reel('Love')"
```

Check the generated image in `output/video/[category]_[timestamp]/phrase_00.jpg`

Hindi text should display clearly in Devanagari script.

---

**Made with ❤️ for Hindi learners worldwide**
