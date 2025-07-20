#!/usr/bin/env python3

def post_template(title, content, date, description="", keywords="", author="", image="", toc="", url="", config={}, categories=[]):
    """Generate HTML for a blog post with enhanced SEO"""
    theme = config.get('theme', 'light')
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="{theme}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{description or title}">
    <title>{title}</title>
    
    <!-- SEO Meta Tags -->
    <meta name="robots" content="index, follow">
    <meta name="author" content="{author or 'Dustin Hogate'}">
    {f'<meta name="keywords" content="{keywords}">' if keywords else ''}
    {f'<link rel="canonical" href="{url}">' if url else ''}
    
    <!-- Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description or title}">
    <meta property="og:type" content="article">
    {f'<meta property="og:url" content="{url}">' if url else ''}
    {f'<meta property="og:image" content="{image}">' if image else ''}
    <meta property="article:published_time" content="{date}">
    {f'<meta property="article:author" content="{author}">' if author else ''}
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description or title}">
    {f'<meta name="twitter:image" content="{image}">' if image else ''}
    
    <link rel="stylesheet" href="../assets/style.css">
    <link rel="stylesheet" href="../assets/prism.css">
    <link rel="alternate" type="application/rss+xml" title="RSS Feed" href="../rss.xml">
    
    <!-- Structured Data -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{title}",
        "description": "{description or title}",
        "datePublished": "{date}",
        "dateModified": "{date}",
        {f'"image": "{image}",' if image else ''}
        "author": {{
            "@type": "Person",
            "name": "{author or config.get('author', 'Dustin Hogate')}"
        }},
        "publisher": {{
            "@type": "Person",
            "name": "Dustin Hogate"
        }},
        "mainEntityOfPage": {{
            "@type": "WebPage",
            "@id": "{url}"
        }}
    }}
    </script>
</head>
<body>
    <header>
        <nav>
            <a href="../index.html">← Home</a>
        </nav>
    </header>
    <main>
        <article>
            <h1>{title}</h1>
            <div class="post-meta">
                <time datetime="{date}">{date}</time>
                {f' • <span class="author">{author}</span>' if author else ''}
                {' • <span class="categories">' + ', '.join([f'<a href="../categories/{cat.lower().replace(" ", "-")}.html">{cat}</a>' for cat in categories]) + '</span>' if categories else ''}
            </div>
            {toc}
            {content}
        </article>
    </main>
    <footer>
        <p>© {date[:4]} | <a href="../rss.xml">RSS</a></p>
    </footer>
    
    <!-- Prism.js for syntax highlighting -->
    <script src="../assets/js/prism.js"></script>
    
    <!-- Copy code functionality -->
    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        // Process all code blocks
        document.querySelectorAll('pre').forEach(function(pre) {{
            var code = pre.querySelector('code');
            if (!code) return;
            
            var language = '';
            
            // Extract language from class name
            var classes = code.className.split(' ');
            for (var i = 0; i < classes.length; i++) {{
                if (classes[i].startsWith('language-')) {{
                    language = classes[i].replace('language-', '');
                    break;
                }}
            }}
            
            if (language && language !== 'language-') {{
                // Create wrapper div
                var wrapper = document.createElement('div');
                wrapper.className = 'code-block-wrapper';
                
                // Create header
                var header = document.createElement('div');
                header.className = 'code-block-header';
                
                var langSpan = document.createElement('span');
                langSpan.className = 'code-language';
                langSpan.textContent = language;
                
                var button = document.createElement('button');
                button.className = 'copy-button';
                button.textContent = '📋';
                button.title = 'Copy code';
                
                header.appendChild(langSpan);
                header.appendChild(button);
                
                // Insert wrapper and move pre into it
                pre.parentNode.insertBefore(wrapper, pre);
                wrapper.appendChild(header);
                wrapper.appendChild(pre);
                
                // Add click handler
                button.addEventListener('click', function() {{
                    var text = code.textContent || code.innerText;
                    navigator.clipboard.writeText(text).then(function() {{
                        button.textContent = '✓';
                        setTimeout(function() {{
                            button.textContent = '📋';
                        }}, 2000);
                    }});
                }});
            }} else {{
                // No language, add button directly to pre
                var button = document.createElement('button');
                button.className = 'copy-button';
                button.textContent = '📋';
                button.title = 'Copy code';
                
                pre.appendChild(button);
                
                // Add click handler
                button.addEventListener('click', function() {{
                    var text = code.textContent || code.innerText;
                    navigator.clipboard.writeText(text).then(function() {{
                        button.textContent = '✓';
                        setTimeout(function() {{
                            button.textContent = '📋';
                        }}, 2000);
                    }});
                }});
            }}
        }});
    }});
    </script>
</body>
</html>"""

def index_template(posts, config, categories=None):
    """Generate HTML for the index page"""
    theme = config.get('theme', 'light')
    post_list = ""
    for post in posts:
        categories_html = ""
        if post.get('categories'):
            category_links = [f'<a href="categories/{cat.lower().replace(" ", "-")}.html">{cat}</a>' for cat in post['categories']]
            categories_html = f' • <span class="categories">{", ".join(category_links)}</span>'
        
        post_list += f"""
        <article class="post-preview">
            <h2><a href="posts/{post['filename']}">{post['title']}</a></h2>
            <time datetime="{post['date']}">{post['date']}</time>{categories_html}
            {f"<p>{post['description']}</p>" if post.get('description') else ""}
        </article>"""
    
    # Build category navigation
    category_nav = ""
    if categories:
        category_links = []
        for category in categories:
            category_url = f"categories/{category.lower().replace(' ', '-')}.html"
            category_links.append(f'<a href="{category_url}">{category}</a>')
        category_nav = ''.join(category_links)
        if category_nav:
            category_nav += '<span class="nav-separator">|</span>'
    
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="{theme}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{config['site_description']}">
    <title>{config['site_title']}</title>
    <link rel="stylesheet" href="assets/style.css">
    <link rel="alternate" type="application/rss+xml" title="RSS Feed" href="rss.xml">
</head>
<body>
    <header>
        <h1>{config['site_title']}</h1>
        <nav>
            {category_nav}
            <a href="rss.xml">RSS</a>
        </nav>
    </header>
    <main>
        <section class="posts">
            {post_list}
        </section>
    </main>
    <footer>
        <p>{config['footer_text']}</p>
    </footer>
</body>
</html>"""

def category_template(category_name, posts, config):
    """Generate HTML for a category page"""
    theme = config.get('theme', 'light')
    post_list = ""
    for post in posts:
        post_list += f"""
        <article class="post-preview">
            <h2><a href="../posts/{post['filename']}">{post['title']}</a></h2>
            <time datetime="{post['date']}">{post['date']}</time>
            {f"<p>{post['description']}</p>" if post.get('description') else ""}
        </article>"""
    
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="{theme}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Posts in {category_name} category">
    <title>{category_name} - {config['site_title']}</title>
    <link rel="stylesheet" href="../assets/style.css">
    <link rel="alternate" type="application/rss+xml" title="RSS Feed" href="../rss.xml">
</head>
<body>
    <header>
        <nav>
            <a href="../index.html">← Home</a>
        </nav>
    </header>
    <main>
        <h1>Category: {category_name}</h1>
        <section class="posts">
            {post_list}
        </section>
    </main>
    <footer>
        <p>{config['footer_text']}</p>
    </footer>
</body>
</html>"""