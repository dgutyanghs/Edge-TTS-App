import webvtt


def convert_vtt_to_srt(vtt_file, srt_file):
    vtt = webvtt.read(vtt_file)
    vtt.save_as_srt()

    # write to an opened file in SRT format
    with open(srt_file, 'w') as f:
        vtt.write(f, format='srt')


# Example usage
vtt_file = "./berich.txt.vtt"
srt_file = "./berich.txt.srt"
convert_vtt_to_srt(vtt_file, srt_file)

print(f"Converted {vtt_file} to {srt_file}")
