# import webvtt

# for caption in webvtt.read('mulan.txt.vtt'):
#     print(caption.start)
#     print(caption.end)
#     print(caption.text)
import webvtt

# save in SRT format
vtt = webvtt.read('mulan.txt.vtt')
vtt.save_as_srt()

# write to an opened file in SRT format
with open('mulan.txt.srt', 'w') as f:
    vtt.write(f, format='srt')