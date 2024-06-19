import subprocess

# Read the contents of readme.txt into memory
# with open('readme.txt', 'r', encoding='utf-8') as file:
with open('mulan.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# Prepare the edge-tts command with the text from readme.txt
command = [
'edge-tts',
# '--voice', 'zh-HK-HiuMaanNeural',
# '--voice', 'zh-CN-shaanxi-XiaoniNeural',
# '--voice', 'zh-CN-XiaoxiaoNeural', #mandarin female
# '--voice', 'zh-HK-WanLungNeural',
'--voice', 'zh-CN-YunjianNeural', #Mandarin male
'--text', data,
'--write-media', 'mulanCN3.mp3',
'--write-subtitles', 'mulanCN3.vtt'
]

# Execute the command
subprocess.run(command, check=True)