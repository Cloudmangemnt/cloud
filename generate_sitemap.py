from pathlib import Path
from urllib.parse import urljoin
import sys
from xml.sax.saxutils import escape

root=Path(__file__).resolve().parent
if len(sys.argv)!=2 or not sys.argv[1].startswith(('https://','http://')):
    raise SystemExit('Usage: python generate_sitemap.py https://username.github.io/repository/')
base=sys.argv[1].rstrip('/')+'/'
files=[p for p in root.rglob('*.html') if p.name!='404.html']
urls=[]
for p in files:
    url=urljoin(base,p.relative_to(root).as_posix())
    urls.append(f'  <url><loc>{escape(url)}</loc></url>')
xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+ '\n'.join(urls)+'\n</urlset>\n'
(root/'sitemap.xml').write_text(xml,encoding='utf-8')
(root/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+urljoin(base,'sitemap.xml')+'\n',encoding='utf-8')
print('Generated',len(files),'URLs for',base)
