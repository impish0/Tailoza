#!/usr/bin/env python3

def post_template(title, content, date, description="", keywords="", author="", image=""):
    """Generate HTML for a blog post with enhanced SEO"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{description or title}">
    <title>{title}</title>
    
    <!-- SEO Meta Tags -->
    <meta name="author" content="{author or 'Dustin Hogate'}">
    {f'<meta name="keywords" content="{keywords}">' if keywords else ''}
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description or title}">
    <meta property="og:type" content="article">
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
            </div>
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
        // Add copy buttons to all code blocks
        document.querySelectorAll('pre').forEach(function(pre) {{
            // Create copy button
            var button = document.createElement('button');
            button.className = 'copy-button';
            button.textContent = '📋';
            button.title = 'Copy code';
            
            // Add click handler
            button.addEventListener('click', function() {{
                var code = pre.querySelector('code');
                var text = code.textContent || code.innerText;
                
                // Copy to clipboard
                navigator.clipboard.writeText(text).then(function() {{
                    button.textContent = '✓';
                    setTimeout(function() {{
                        button.textContent = '📋';
                    }}, 2000);
                }});
            }});
            
            // Add button to pre element
            pre.appendChild(button);
        }});
    }});
    </script>
</body>
</html>"""

def index_template(posts, config):
    """Generate HTML for the index page"""
    post_list = ""
    for post in posts:
        post_list += f"""
        <article class="post-preview">
            <h2><a href="posts/{post['filename']}">{post['title']}</a></h2>
            <time datetime="{post['date']}">{post['date']}</time>
            {f"<p>{post['description']}</p>" if post.get('description') else ""}
        </article>"""
    
    return f"""<!DOCTYPE html>
<html lang="en">
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