# YT Music Playlist Downloader

Script Python sederhana berbasis Termux/CLI untuk mengunduh seluruh playlist dari YouTube Music ke MP3 tanpa error.

## Requirements
- Python 3
- FFmpeg
- yt-dlp

## Installation (Termux)
```bash
pkg update && pkg upgrade -y
pkg install python ffmpeg git -y
pip install -U --pre "yt-dlp[default]"
termux-setup-storage
```

## Cara penggunaan 
1.Clone repository ini
```bash
git clone [https://github.com/Skyzo34/ytmusic-playlist-downloader.git](https://github.com/Skyzo34/ytmusic-playlist-downloader.git)
```
2.Masuk ke foldernya
```bash
cd ytmusic-playlist-downloader
```
3.Jalankan script
```bash
python ytmusic.py "LINK_PLAYLIST_YOUTUBE_MUSIC"
