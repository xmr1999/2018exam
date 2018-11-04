mport requests
url = 'https://blog.snowstar.org'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
title = re.findall(r'<snowstar.org/2018/06/30/="og:title" context="(.*?)"/>'html)[0]
fb = open('%s.txt' % title, 'w',encoding='utf-8')
dl = re.findall(r'<dl id="list">.*?</dl>',html,re.S)[0]
chapter_info_list = refindall(r'href="(.*?)">(.*?)<',dl)
for chapter_info in chapter_info_list:
    chapter_url,chapter_title=chapter_info
    chapter_url = "https://snowstar.org/2018/06/30/" % chapter_url
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'utf-8'
    chaspter_html = chapter_response.text
    chapter_content = re.findall(r'</div>a1\(\);<div class="entry-content">(.*?)</div>a2\(\);<div class="entry-content">')
    chapter_content = chapter_content.replace(' ','')
    chapter_content = chapter_content.replace('<code>','')
    chapter_content = chapter_content.replace('<p> ','')
    chapter_content = chapter_content.replace('<h> ','')
    fb.write(chapter_title)
    fb.write(chapter_content)
    fb.write('\n')
    print(chapter_url)
    
