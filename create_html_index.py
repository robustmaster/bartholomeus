import os
from datetime import datetime

start = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>uselessfrigid</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
<div class="header">
    <h1>uselessfrigid</h1>
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
sample = '<li><a href="./htmls/entry.name">entry.name</a>'

html_li_tags = ''
with os.scandir('./htmls') as it:
    files = list(it)
    files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    for entry in files:
        if not entry.name.startswith('.') and entry.is_file() and entry.name.endswith('.html'):
            entry_created_datetime = datetime.fromtimestamp(int(entry.stat().st_mtime))
            entry_created_time_string = entry_created_datetime.strftime('%Y-%m-%d')
            html_li_tags += '        <li><span class="gray">' + entry_created_time_string + '</span>&nbsp;&nbsp;<a href="./htmls/' + entry.name + '">' + entry.name[:-5] + '</a></li>\n'

html_index = start + html_li_tags + end

with open('index.html', 'w') as f:
    f.write(html_index)
