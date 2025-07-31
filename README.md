# Just-try

This project contains a simple Discord music bot that plays audio from a given URL.

## Setup
1. Make sure you have Python 3.11+ installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure [FFmpeg](https://ffmpeg.org/) is available on your system as it is required for audio playback.
4. Create a Discord bot and obtain its token. Set it as an environment variable named `DISCORD_TOKEN`.
   ```bash
   export DISCORD_TOKEN=YOUR_TOKEN_HERE
   ```

## Usage
Run the bot with Python:
```bash
python bot.py
```

In your Discord server, invite the bot and use the commands:
- `!join` &mdash; Bot joins your current voice channel.
- `!play <url>` &mdash; Plays audio from the specified URL.
- `!leave` &mdash; Disconnects the bot from the voice channel.

The URL can be any direct link to an audio file or stream.
