import os
from datetime import datetime

start = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>一派胡言收藏夹</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
<div class="header">
    <h1>一派胡言收藏夹</h1>
    <p class="go-back" style="margin: 0 auto;text-align: center;"><a href="https://yipai.me" style="color: #cfcfcf;">返回一派胡言博客</a></p>
</div>
<div class="post-list">
    <ul>
'''

end = '''
    </ul>
</div>
</div>
</body>
</html>
<!doctype html>
'''

html_li_tags = ''
with os.scandir('./htmls') as it:
    files = list(it)
    files.sort(key=lambda x: x.name, reverse=True)
    for entry in files:
        if not entry.name.startswith('.') and entry.is_file() and entry.name.endswith('.html'):
            entry_keep_date = entry.name.split('.')[0]
            entry_keep_date = entry_keep_date[:4] + '-' + entry_keep_date[4:6] + '-' + entry_keep_date[6:8]
            entry_title = entry.name[16:][:-5]
            html_li_tags += '<li><span class="gray">' + entry_keep_date + '</span>&nbsp;&nbsp;<a href="./htmls/' + entry.name + '">' + entry_title + '</a></li>\n'

html_index = start + html_li_tags + end

with open('index.html', 'w') as f:
    f.write(html_index)
