# Edge-TTS example
## Tool for generating voices in your PC or Mac.
 * This project is base on [Edge-TTS](https://github.com/rany2/edge-tts) GPL-3.0 license
## These Audios in project are generate by Edge-TTS 
  
## Installation
### 1. create a virtual env
``` shell
python3 -m venv .venv 
```

### 2. activate venv
Linux && MacOS
```shell
source .venv/bin/activate
```
Windows
```shell
.\.venv\Scripts\activate
```

### 3. install dependence
``` shell
pip install -r requirement.txt
```

### 4. Show all suported voices
```shell
edge-tts --list-voices
```

### 5. Edit the text in 'mulan.txt' for converting.

### 6. Edit convert.py, choose your language voice, such as Mandarin, English etc.
### 7. Execute command in terminal.
```shell
python3 convert.py
```
### 8. Modify time in *.vtt by Edit timeshift.py
After modify, then execute in termianl
```shell
python3 timeshift.py
```
### 9. Use GUI mode
    for alternative, you can use GUI mode by execute command in terminal
    ```shell
    python3 main.py
    ```
## Generate Application
```shell
    pyinstaller --onefile main.py
```
after that, you can file execute file in folder 'build' or 'dist'.
the app work properly in ubuntu, but windows doesn't.
## Enjoy