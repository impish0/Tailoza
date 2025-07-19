#!/usr/bin/env python3
import re
import os
from datetime import datetime
import html

def parse_frontmatter(content):
    """Extract frontmatter from markdown content"""
    lines = content.strip().split('\n')
    if lines[0] != '---':
        return {}, content
    
    frontmatter = {}
    end_index = 1
    
    for i in range(1, len(lines)):
        if lines[i] == '---':
            end_index = i + 1
            break
        if ':' in lines[i]:
            key, value = lines[i].split(':', 1)
            frontmatter[key.strip()] = value.strip()
    
    body = '\n'.join(lines[end_index:])
    return frontmatter, body

def markdown_to_html(text):
    """Convert markdown to HTML - simple implementation"""
    # First, extract code blocks and inline code to protect them
    code_blocks = []
    inline_codes = []
    
    # Extract code blocks
    def save_code_block(match):
        content = match.group(1).strip()
        # Check if first line is a language hint
        lines = content.split('\n', 1)
        if lines and lines[0] and not ' ' in lines[0] and lines[0].isalpha():
            lang = lines[0].lower()
            code = html.escape(lines[1] if len(lines) > 1 else '')
            code_blocks.append((lang, code))
        else:
            code_blocks.append(('', html.escape(content)))
        return f'___CODEBLOCK_{len(code_blocks)-1}___'
    
    text = re.sub(r'```(.*?)```', save_code_block, text, flags=re.DOTALL)
    
    # Extract inline code
    def save_inline_code(match):
        inline_codes.append(html.escape(match.group(1)))
        return f'___INLINECODE_{len(inline_codes)-1}___'
    
    text = re.sub(r'`([^`]+)`', save_inline_code, text)
    
    # Now process markdown on the remaining text
    # Images (before links to avoid conflicts)
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" loading="lazy">', text)
    
    # Headers
    text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    
    # Bold and italic
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    
    # Links (with download detection)
    def process_link(match):
        text = match.group(1)
        url = match.group(2)
        # Check if it's a download link (common file extensions)
        download_exts = ['.pdf', '.zip', '.tar', '.gz', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx']
        if any(url.lower().endswith(ext) for ext in download_exts):
            return f'<a href="{url}" download>{text} ⬇</a>'
        return f'<a href="{url}">{text}</a>'
    
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', process_link, text)
    
    # Lists
    text = re.sub(r'^- (.*?)$', r'<li>\1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'(<li>.*?</li>\n?)+', lambda m: '<ul>\n' + m.group(0) + '</ul>\n', text, flags=re.DOTALL)
    
    # Restore code blocks and inline codes
    for i, (lang, code) in enumerate(code_blocks):
        if lang:
            text = text.replace(f'___CODEBLOCK_{i}___', f'<pre><code class="language-{lang}">{code}</code></pre>')
        else:
            text = text.replace(f'___CODEBLOCK_{i}___', f'<pre><code>{code}</code></pre>')
    
    for i, code in enumerate(inline_codes):
        text = text.replace(f'___INLINECODE_{i}___', f'<code>{code}</code>')
    
    # Paragraphs
    paragraphs = text.split('\n\n')
    formatted_paragraphs = []
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<') and not p.startswith('- '):
            p = f'<p>{p}</p>'
        formatted_paragraphs.append(p)
    
    return '\n\n'.join(formatted_paragraphs)

def get_post_date(frontmatter, filename):
    """Get date from frontmatter or filename"""
    if 'date' in frontmatter:
        return frontmatter['date']
    
    # Try to extract date from filename (e.g., 2024-01-15-post-title.md)
    match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
    if match:
        return match.group(1)
    
    # Default to today's date
    return datetime.now().strftime('%Y-%m-%d')