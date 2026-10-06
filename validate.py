#!/usr/bin/env python3
"""Validate rendered site routes, assets, metadata, and XML feeds."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET

root=Path(__file__).resolve().parent/'dist'
issues=[]
class Inspector(HTMLParser):
    def __init__(self):
        super().__init__();self.refs=[];self.ids=set();self.h1=0;self.title=False;self.description=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids:issues.append('Duplicate ID: '+a['id'])
            self.ids.add(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='title':self.title=True
        if tag=='meta' and a.get('name')=='description':self.description=True
        if tag=='img' and 'alt' not in a:issues.append('Missing image alternative text')
        for attr in ['href','src','poster']:
            if attr in a:self.refs.append(a[attr])

parsed={}
for path in root.rglob('*.html'):
    parser=Inspector();parser.feed(path.read_text());parsed[path.resolve()]=parser
    assert parser.h1==1,f'{path}: expected one H1'
    assert parser.title and parser.description,f'{path}: missing metadata'
checks=0
for path,parser in parsed.items():
    for value in parser.refs:
        url=urlsplit(value)
        if url.scheme or url.netloc:continue
        target=(root/url.path.lstrip('/') if url.path.startswith('/') else path.parent/unquote(url.path)).resolve() if url.path else path
        if target.is_dir():target/='index.html'
        if not target.exists():issues.append(f'{path.relative_to(root)}: missing {value}')
        elif url.fragment and target.suffix=='.html' and url.fragment not in parsed[target].ids:issues.append(f'{path}: missing fragment {value}')
        checks+=1
for filename in ['sitemap.xml']:ET.parse(root/filename)
assert not issues,'\n'.join(issues)
print(f'PASS: {len(parsed)} pages, {checks} local references, image alt text, headings, metadata, sitemap XML.')
