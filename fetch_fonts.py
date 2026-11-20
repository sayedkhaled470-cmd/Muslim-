"""Download the Google Fonts used by the app at BUILD time so fonts work offline inside the APK.
Reads the Google Fonts <link> from index.html, downloads CSS + font files into <out>/ and writes <out>/fonts.css
(with relative urls). Safe to fail: the app falls back to online fonts / system fonts."""
import hashlib, os, re, sys, urllib.request
OUT = sys.argv[1] if len(sys.argv) > 1 else 'fonts-data'
UA = 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36'
html = open('index.html', encoding='utf-8').read()
m = re.search(r'https://fonts\.googleapis\.com/css2\?[^"\']+', html)
if not m:
    raise SystemExit('no google fonts link')
def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()
os.makedirs(OUT, exist_ok=True)
css = get(m.group(0).replace('&amp;', '&')).decode('utf-8')
def sub(mm):
    url = mm.group(1)
    name = hashlib.sha1(url.encode()).hexdigest()[:16] + '.woff2'
    path = os.path.join(OUT, name)
    if not os.path.exists(path):
        open(path, 'wb').write(get(url))
    return 'url(' + name + ')'
css = re.sub(r'url\((https://fonts\.gstatic\.com/[^)]+)\)', sub, css)
open(os.path.join(OUT, 'fonts.css'), 'w', encoding='utf-8').write(css)
print('fonts ok', len(os.listdir(OUT)) - 1, 'files')
