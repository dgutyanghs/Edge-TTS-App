import re

def clean_space(text):
  """"
  处理多余的空格
  """
  match_regex = re.compile(u'[\u4e00-\u9fa5。\.,，:：《》、\(\)（）]{1} +(?<![a-zA-Z])|\d+ +| +\d+|[a-z A-Z]+')
  should_replace_list = match_regex.findall(text)
  order_replace_list = sorted(should_replace_list,key=lambda i:len(i),reverse=True)
  for i in order_replace_list:
    if i == u' ':
      continue
    new_i = i.strip()
    text = text.replace(i,new_i)
  return text


with open('berich.txt.srt', 'r', encoding='utf-8') as file:
    content = file.read()
    content2 =clean_space(content)



with open('processed_berich.txt.srt', 'w', encoding='utf-8') as file:
    file.write(content2)
