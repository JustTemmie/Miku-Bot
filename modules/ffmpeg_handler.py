import os
from ffmpeg import FFmpeg


async def apply_ffmpeg_audio_filter(input_file, output_file, codec, map, filter):
    if codec == map == filter == None:
        ffmpeg = (
            FFmpeg(os.getenv("FFMPEG_PATH", "/usr/bin/env ffmpeg"))
            .option("y")
            .input(input_file)
            .output(output_file)
        )
    else:
        ffmpeg = (
            FFmpeg(os.getenv("FFMPEG_PATH", "/usr/bin/env ffmpeg"))
            .option("y")
            .input(input_file)
            .output(output_file,
                codec,
                map=map,
                filter=filter
            )
        )

    try:
        ffmpeg.execute()
        return True
    except Exception as e:
        print(f"ffmpeg failed to convert {input_file}\n{e.message}, {e.arguments}")
        return False

def get_duration(file):
    return float(
        FFmpeg(os.getenv("FFPROBE_PATH", "/usr/bin/env ffprobe"))
        .input(
            file,
            show_entries="format=duration",
            of="compact=p=0:nk=1",
            loglevel="error"
        )
        .execute()
        .strip()
    )