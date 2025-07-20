#!/usr/bin/env python3
import os
import sys
import shutil
import json
from pathlib import Path
from parser import parse_frontmatter, markdown_to_html, get_post_date, extract_headings, generate_toc, add_heading_ids
from templates import post_template, index_template, category_template
from rss_generator import generate_rss
from sitemap_generator import generate_sitemap

def load_config():
    """Load configuration from config.json or use defaults"""
    default_config = {
        "site_title": "My Blog",
        "site_url": "https://example.com",
        "site_description": "A simple static blog",
        "author": "Your Name",
        "footer_text": "Built with a simple static site generator"
    }
    
    config_path = Path('config.json')
    if config_path.exists():
        try:
            with open(config_path, 'r') as f:
                user_config = json.load(f)
                default_config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config.json: {e}")
    
    return default_config

def ensure_directories():
    """Ensure all required directories exist"""
    dirs = ['posts', 'output', 'output/posts', 'output/assets', 'output/assets/js', 'output/images', 'output/categories', 'images', 'assets', 'assets/js']
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)

def build_site():
    """Build the static site from markdown files"""
    config = load_config()
    ensure_directories()
    posts = []
    categories = {}  # Dict to store posts by category
    
    # Process all markdown files in posts directory
    posts_dir = Path('posts')
    if not posts_dir.exists():
        print("Error: 'posts' directory not found")
        return False
    
    for post_file in sorted(posts_dir.glob('*.md')):
        try:
            with open(post_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            filename = post_file.name
            
            # Parse frontmatter and content
            frontmatter, body = parse_frontmatter(content)
            
            # Get post metadata
            title = frontmatter.get('title', filename.replace('.md', '').replace('-', ' ').title())
            date = get_post_date(frontmatter, filename)
            description = frontmatter.get('description', '')
            keywords = frontmatter.get('keywords', '')
            author = frontmatter.get('author', '')
            image = frontmatter.get('image', '')
            post_categories = frontmatter.get('categories', [])
            
            # Convert markdown to HTML
            html_content = markdown_to_html(body)
            
            # Generate TOC if enabled in frontmatter
            toc_html = ""
            if frontmatter.get('toc', '').lower() == 'true':
                headings = extract_headings(html_content)
                # Only show TOC if there are at least 3 headings (excluding H1)
                MIN_HEADINGS_FOR_TOC = 3
                if len([h for h in headings if h['level'] > 1]) >= MIN_HEADINGS_FOR_TOC:
                    toc_html = generate_toc(headings)
                    html_content = add_heading_ids(html_content, headings)
            
            # Generate HTML filename
            html_filename = filename.replace('.md', '.html')
            
            # Create post HTML
            post_url = f"{config['site_url']}/posts/{html_filename}"
            post_html = post_template(title, html_content, date, description, keywords, author, image, toc_html, post_url, config, post_categories)
            
            # Write post HTML file
            with open(Path('output/posts') / html_filename, 'w', encoding='utf-8') as f:
                f.write(post_html)
            
            # Add to posts list for index and RSS
            posts.append({
                'title': title,
                'date': date,
                'description': description,
                'filename': html_filename,
                'content': html_content,
                'categories': post_categories
            })
            
            # Track posts by category
            for category in post_categories:
                if category not in categories:
                    categories[category] = []
                categories[category].append({
                    'title': title,
                    'date': date,
                    'description': description,
                    'filename': html_filename
                })
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            continue
    
    # Sort posts by date (newest first)
    posts.sort(key=lambda x: x['date'], reverse=True)
    
    # Generate index page
    index_html = index_template(posts, config, sorted(categories.keys()))
    with open('output/index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    # Generate category pages
    for category_name, category_posts in categories.items():
        # Sort posts in category by date
        category_posts.sort(key=lambda x: x['date'], reverse=True)
        
        # Generate category page
        category_html = category_template(category_name, category_posts, config)
        
        # Create safe filename for category
        category_filename = category_name.lower().replace(' ', '-') + '.html'
        
        # Write category page
        with open(Path('output/categories') / category_filename, 'w', encoding='utf-8') as f:
            f.write(category_html)
    
    print(f"✓ Generated {len(categories)} category pages")
    
    # Generate RSS feed
    rss_xml = generate_rss(posts, config['site_title'], config['site_url'], config['site_description'])
    with open('output/rss.xml', 'w', encoding='utf-8') as f:
        f.write(rss_xml)
    
    # Generate sitemap
    sitemap_xml = generate_sitemap(posts, config)
    with open('output/sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)
    
    # Generate robots.txt
    robots_txt = f"""User-agent: *
Allow: /

Sitemap: {config['site_url']}/sitemap.xml"""
    with open('output/robots.txt', 'w', encoding='utf-8') as f:
        f.write(robots_txt)
    
    # Copy static assets
    try:
        # Copy CSS files
        shutil.copy2('assets/style.css', 'output/assets/style.css')
        print("✓ Copied style.css")
        
        prism_css = Path('assets/prism.css')
        if prism_css.exists():
            shutil.copy2(prism_css, 'output/assets/prism.css')
            print("✓ Copied prism.css")
        
        # Copy JS files
        prism_js = Path('assets/js/prism.js')
        if prism_js.exists():
            shutil.copy2(prism_js, 'output/assets/js/prism.js')
            print("✓ Copied prism.js")
        
        # Copy images
        images_dir = Path('images')
        if images_dir.exists() and any(images_dir.iterdir()):
            for img in images_dir.glob('*'):
                if img.is_file():
                    shutil.copy2(img, f'output/images/{img.name}')
            print("✓ Copied images")
    
    except Exception as e:
        print(f"Error copying assets: {e}")
        return False
    
    print(f"✓ Built {len(posts)} posts")
    print("✓ Generated index.html")
    print("✓ Generated rss.xml")
    print("✓ Generated sitemap.xml")
    print("✓ Copied CSS files")
    print("\nSite built successfully in 'output' directory!")
    return True

if __name__ == "__main__":
    try:
        success = build_site()
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\nBuild cancelled")
        sys.exit(1)
    except Exception as e:
        print(f"Error building site: {e}")
        sys.exit(1)