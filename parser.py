#!/usr/bin/env python3
import re
from datetime import datetime
import html

def parse_frontmatter(content):
    """Extract frontmatter from markdown content"""
    if not content:
        return {}, content
        
    lines = content.strip().split('\n')
    if not lines or lines[0] != '---':
        return {}, content
    
    frontmatter = {}
    end_index = 1
    
    for i in range(1, len(lines)):
        if lines[i] == '---':
            end_index = i + 1
            break
        if ':' in lines[i]:
            try:
                key, value = lines[i].split(':', 1)
                key = key.strip()
                value = value.strip()
                
                # Handle categories as comma-separated list
                if key == 'categories':
                    frontmatter[key] = [cat.strip() for cat in value.split(',') if cat.strip()]
                else:
                    frontmatter[key] = value
            except ValueError:
                # Skip malformed frontmatter lines
                continue
    
    body = '\n'.join(lines[end_index:]) if end_index < len(lines) else ''
    return frontmatter, body

def markdown_to_html(text):
    """Convert markdown to HTML - enhanced implementation"""
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
    text = re.sub(r'^###### (.*?)$', r'<h6>\1</h6>', text, flags=re.MULTILINE)
    text = re.sub(r'^##### (.*?)$', r'<h5>\1</h5>', text, flags=re.MULTILINE)
    text = re.sub(r'^#### (.*?)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    
    # Strikethrough
    text = re.sub(r'~~(.*?)~~', r'<del>\1</del>', text)
    
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
    
    # Tables (simple implementation)
    lines = text.split('\n')
    new_lines = []
    in_table = False
    
    for i, line in enumerate(lines):
        if '|' in line and line.strip().startswith('|') and line.strip().endswith('|'):
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            
            # Check if this is a separator line
            if all(re.match(r'^-+$', cell.replace(':', '')) for cell in cells):
                continue
            
            if not in_table:
                new_lines.append('<table>')
                new_lines.append('<thead>')
                in_table = True
                is_header = True
            
            if is_header and i + 1 < len(lines) and '|' in lines[i + 1]:
                next_cells = [cell.strip() for cell in lines[i + 1].split('|')[1:-1]]
                if all(re.match(r'^:?-+:?$', cell) for cell in next_cells):
                    new_lines.append('<tr>')
                    for cell in cells:
                        new_lines.append(f'<th>{cell}</th>')
                    new_lines.append('</tr>')
                    new_lines.append('</thead>')
                    new_lines.append('<tbody>')
                    is_header = False
                    continue
            
            new_lines.append('<tr>')
            for cell in cells:
                new_lines.append(f'<td>{cell}</td>')
            new_lines.append('</tr>')
        else:
            if in_table:
                new_lines.append('</tbody>')
                new_lines.append('</table>')
                in_table = False
            new_lines.append(line)
    
    if in_table:
        new_lines.append('</tbody>')
        new_lines.append('</table>')
    
    text = '\n'.join(new_lines)
    
    # Blockquotes (handle nested)
    lines = text.split('\n')
    new_lines = []
    blockquote_level = 0
    
    for line in lines:
        match = re.match(r'^(>+)\s*(.*)', line)
        if match:
            level = len(match.group(1))
            content = match.group(2)
            
            # Open blockquotes if needed
            while blockquote_level < level:
                new_lines.append('<blockquote>')
                blockquote_level += 1
            
            # Close blockquotes if needed
            while blockquote_level > level:
                new_lines.append('</blockquote>')
                blockquote_level -= 1
            
            new_lines.append(content)
        else:
            # Close all blockquotes
            while blockquote_level > 0:
                new_lines.append('</blockquote>')
                blockquote_level -= 1
            new_lines.append(line)
    
    # Close remaining blockquotes
    while blockquote_level > 0:
        new_lines.append('</blockquote>')
        blockquote_level -= 1
    
    text = '\n'.join(new_lines)
    
    # Task lists
    text = re.sub(r'^- \[ \] (.*?)$', r'<li><input type="checkbox" disabled> \1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'^- \[x\] (.*?)$', r'<li><input type="checkbox" checked disabled> \1</li>', text, flags=re.MULTILINE)
    
    # Process lists (handle nested lists)
    lines = text.split('\n')
    new_lines = []
    list_stack = []  # Track open lists: ('ul'/'ol', indent_level)
    
    for line in lines:
        # Check for unordered list item
        ul_match = re.match(r'^(\s*)[-*+]\s+(.+)$', line)
        # Check for ordered list item
        ol_match = re.match(r'^(\s*)(\d+)\.\s+(.+)$', line)
        # Check for already processed list items (from task lists)
        li_match = re.match(r'^(\s*)<li>(.+)</li>$', line)
        
        if ul_match or ol_match or li_match:
            if ul_match:
                indent = len(ul_match.group(1))
                content = ul_match.group(2)
                list_type = 'ul'
                item_html = f'<li>{content}</li>'
            elif ol_match:
                indent = len(ol_match.group(1))
                content = ol_match.group(3)
                list_type = 'ol'
                item_html = f'<li>{content}</li>'
            else:  # li_match
                indent = len(li_match.group(1))
                content = li_match.group(2)
                list_type = 'ul'  # Task lists are unordered
                item_html = f'<li>{content}</li>'
            
            # Calculate indent level (assuming 2 spaces per level)
            level = indent // 2
            
            # Close lists that are deeper than current level
            while list_stack and list_stack[-1][1] > level:
                closed_list = list_stack.pop()
                new_lines.append('  ' * closed_list[1] + f'</{closed_list[0]}>')
            
            # Open new list if needed
            if not list_stack or list_stack[-1][1] < level:
                new_lines.append('  ' * level + f'<{list_type}>')
                list_stack.append((list_type, level))
            elif list_stack[-1][0] != list_type:
                # Different list type at same level, close and open new
                closed_list = list_stack.pop()
                new_lines.append('  ' * closed_list[1] + f'</{closed_list[0]}>')
                new_lines.append('  ' * level + f'<{list_type}>')
                list_stack.append((list_type, level))
            
            new_lines.append('  ' * level + item_html)
        else:
            # Close all open lists
            while list_stack:
                closed_list = list_stack.pop()
                new_lines.append('  ' * closed_list[1] + f'</{closed_list[0]}>')
            
            new_lines.append(line)
    
    # Close remaining lists
    while list_stack:
        closed_list = list_stack.pop()
        new_lines.append('  ' * closed_list[1] + f'</{closed_list[0]}>')
    
    text = '\n'.join(new_lines)
    
    # Horizontal rules
    text = re.sub(r'^---+$', '<hr>', text, flags=re.MULTILINE)
    text = re.sub(r'^\*\*\*+$', '<hr>', text, flags=re.MULTILINE)
    
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
        if p and not re.match(r'^<(?:h[1-6]|ul|ol|li|blockquote|pre|table|hr)', p):
            # Don't wrap if it's already an HTML element
            p = f'<p>{p}</p>'
        formatted_paragraphs.append(p)
    
    return '\n\n'.join(formatted_paragraphs)

def extract_headings(html_content):
    """Extract headings from HTML content for TOC generation"""
    # Remove code blocks to avoid extracting headings from code
    temp_content = re.sub(r'<pre><code.*?>.*?</code></pre>', '', html_content, flags=re.DOTALL)
    
    # Find all headings
    headings = []
    for match in re.finditer(r'<h([1-6])>(.*?)</h\1>', temp_content):
        level = int(match.group(1))
        text_with_html = match.group(2)
        # Strip any HTML tags from heading text for display
        clean_text = re.sub(r'<[^>]+>', '', text_with_html)
        # Create anchor ID from heading text
        anchor_id = re.sub(r'[^\w\s-]', '', clean_text.lower())
        anchor_id = re.sub(r'[-\s]+', '-', anchor_id).strip('-')
        
        headings.append({
            'level': level,
            'text': clean_text,
            'text_with_html': text_with_html,  # Keep original HTML for matching
            'id': anchor_id
        })
    
    return headings

def generate_toc(headings):
    """Generate table of contents HTML from headings"""
    if not headings:
        return ""
    
    # Filter out H1s
    headings = [h for h in headings if h['level'] > 1]
    if not headings:
        return ""
    
    toc_html = '<div class="toc-card">\n'
    toc_html += '<h2 class="toc-title">Table of Contents</h2>\n'
    toc_html += '<nav class="toc">\n'
    
    # Build nested structure
    stack = []  # Stack to track open ul elements
    prev_level = 1
    
    for heading in headings:
        level = heading['level']
        
        # Close deeper levels if we're going back up
        while prev_level > level and stack:
            toc_html += stack.pop()
            prev_level -= 1
        
        # Open new levels if we're going deeper
        while prev_level < level:
            toc_html += '<ul>\n'
            stack.append('</ul>\n')
            prev_level += 1
        
        # Add the item
        toc_html += f'<li><a href="#{heading["id"]}">{heading["text"]}</a></li>\n'
    
    # Close all remaining open lists
    while stack:
        toc_html += stack.pop()
    
    toc_html += '</nav>\n</div>\n'
    return toc_html

def add_heading_ids(html_content, headings):
    """Add IDs to headings in HTML content"""
    for heading in headings:
        # Use the original HTML content to match exactly
        old_heading = f'<h{heading["level"]}>{heading["text_with_html"]}</h{heading["level"]}>'
        new_heading = f'<h{heading["level"]} id="{heading["id"]}">{heading["text_with_html"]}</h{heading["level"]}>'
        # Simple string replacement
        html_content = html_content.replace(old_heading, new_heading, 1)
    
    return html_content

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