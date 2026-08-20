import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Penggunaan: python ytmusic.py \"LINK_PLAYLIST_YOUTUBE_MUSIC\"")
        sys.exit(1)

    url = sys.argv[1]

    cmd = [
        "yt-dlp",
        "--extractor-args", "youtube:player_client=android_music,web",
        "--force-ipv4",
        "-x",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "--embed-thumbnail",
        "--add-metadata",
        "-o", "/sdcard/Download/YTMusic/%(title)s.%(ext)s",
        url
    ]

    subprocess.run(cmd)

if __name__ == "__main__":
    main()
