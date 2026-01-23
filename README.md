# 🎥 YouTube MP3/MP4 Downloader

A lightweight, local Python tool for extracting high-quality video (MP4) or audio (MP3) from YouTube URLs. It automatically saves files directly to your Windows **Downloads** folder.

## ✨ Features
- **One-Click Download:** Simple terminal interface.
- **High Quality:** Uses `yt-dlp` to fetch the best available streams.
- **Smart Conversion:** Automatically merges video and audio or converts to 192kbps MP3.
- **No Manual File Management:** Automatically detects your system's download path.

## 🛠️ Requirements

Before running the tool, you need to have the following installed on your system:

1. **Python 3.10+**: [Download Python](https://www.python.org/downloads/) (Ensure "Add to PATH" is checked).
2. **FFmpeg**: Required for merging video/audio and MP3 conversion.
   - Run this in PowerShell: `winget install ffmpeg`
3. **yt-dlp**: The core engine.
   - Run this in PowerShell: `pip install yt-dlp`

## 🚀 Installation & Usage

1. **Clone or Download** this repository to your desktop.
2. **Open a Terminal** (PowerShell or CMD) in the project folder.
3. **Run the script**:
   ```powershell
   python download.py

## Virus Total Results
https://www.virustotal.com/gui/file/0e834b82365f160ee803c41e0819f608633e9c9245b1e2911b06395ef12ba87a?nocache=1
