"""Download the full Quran (Tajweed text) + Tafsir Muyassar at BUILD time so the APK ships them offline.
Output: <out>/t/N.json, <out>/m/N.json  (N = 1..604, rows = [ayahNumber, numberInSurah, surah, text])
        <out>/idx.json                  (rows = [ayahNumber, surah, numberInSurah, page, normalizedText, displayText])
"""
import json, os, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

OUT = sys.argv[1] if len(sys.argv) > 1 else 'quran-data'
BASE = 'https://api.alquran.cloud/v1/page/'
PAGES = range(1, 605)

def get(url):
    for i in range(7):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'muslim-build'})
            with urllib.request.urlopen(req, timeout=60) as r:
                j = json.load(r)
            if j.get('code') == 200 and j['data']['ayahs']:
                return j['data']['ayahs']
        except Exception:
            pass
        time.sleep(2 * (i + 1))
    raise SystemExit('FAILED: ' + url)

def job(a):
    kind, ed, p = a
    path = f'{OUT}/{kind}/{p}.json'
    if os.path.exists(path):
        return
    rows = [[x['number'], x['numberInSurah'], x['surah']['number'], x['text']] for x in get(f'{BASE}{p}/{ed}')]
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, separators=(',', ':'))
    os.replace(tmp, path)

os.makedirs(f'{OUT}/t', exist_ok=True)
os.makedirs(f'{OUT}/m', exist_ok=True)
jobs = [('t', 'quran-tajweed', p) for p in PAGES] + [('m', 'ar.muyassar', p) for p in PAGES]
with ThreadPoolExecutor(6) as ex:
    list(ex.map(job, jobs))

MARK = re.compile(r'\[[a-z](?::\d+)?\[|\]')
STRIP = re.compile('[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u0640]')
def norm(s):
    s = STRIP.sub('', s)
    s = re.sub('[أإآٱ]', 'ا', s).replace('ة', 'ه').replace('ى', 'ي')
    return s

idx, total_t, total_m = [], 0, 0
for p in PAGES:
    t = json.load(open(f'{OUT}/t/{p}.json', encoding='utf-8'))
    m = json.load(open(f'{OUT}/m/{p}.json', encoding='utf-8'))
    total_t += len(t); total_m += len(m)
    for num, n, s, text in t:
        d = MARK.sub('', text)
        w = d.split(' ')
        if n == 1 and s not in (1, 9) and len(w) > 4 and norm(d).startswith('بسم'):
            d = ' '.join(w[4:])
        idx.append([num, s, n, p, norm(d), d])
if total_t != 6236 or total_m != 6236:
    raise SystemExit(f'BAD COUNT tajweed={total_t} muyassar={total_m} (expected 6236)')
with open(f'{OUT}/idx.json', 'w', encoding='utf-8') as f:
    json.dump(idx, f, ensure_ascii=False, separators=(',', ':'))
print('OK', total_t, total_m)
