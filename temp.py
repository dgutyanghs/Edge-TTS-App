def rewrite():
    with open('processed_berich.txt.srt', 'r', encoding='gbk') as file:
        content = file.read()
        with open('p_berich2.srt', 'w', encoding='utf-8') as file:
            file.write(content)

rewrite()