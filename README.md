# Simple Static Blog Generator

A fast, minimal static site generator that converts Markdown to HTML with zero runtime dependencies. Perfect for personal blogs, documentation, or any content-focused website.

## ✨ Features

- **📝 Markdown Support**: Write in Markdown with YAML frontmatter
- **🖼️ Smart Image Handling**: Local and external images with automatic styling
- **🎨 Syntax Highlighting**: Beautiful code blocks with Prism.js (150+ languages)
- **📑 Table of Contents**: Auto-generated, nested TOC from your headings
- **🏷️ Categories**: Organize posts by topic with auto-generated category pages
- **🔍 SEO Optimized**: Meta tags, Open Graph, and Twitter Cards
- **📡 RSS Feed**: Automatically generated for all posts
- **📱 Responsive**: Mobile-first design that looks great everywhere
- **⚡ Lightning Fast**: No JavaScript required (except optional features)
- **🔒 Self-Contained**: No external dependencies or CDN requirements
- **🎯 Native Fonts**: Uses system fonts for instant loading
- **🌙 Theme Support**: Choose between light or dark theme at build time

## 🚀 Quick Start

### 1. Setup

```bash
# Clone or download this project
# Requires Python 3.6+ (for building only - not needed for the output)
```

### 2. Configure Your Site

Edit `config.json` with your details:

```json
{
    "site_title": "My Awesome Blog",
    "site_url": "https://yourdomain.com",
    "site_description": "A blog about things I love",
    "author": "Your Name",
    "footer_text": "© 2025 Your Name | Built with ❤️",
    "theme": "light"
}
```

### 3. Create Your First Post

Create a `.md` file in the `posts/` directory:

```markdown
---
title: My First Blog Post
date: 2025-01-20
description: This is my very first blog post using this amazing static site generator
keywords: blog, first post, static site
author: Jane Doe
image: /images/featured-image.jpg
categories: Technology, Programming
toc: true
---

# Welcome to My Blog!

This is my first paragraph. It supports **bold**, *italic*, and ***both***.

## Getting Started

Here's what you can do...

### Subsection Example

More content here...

## Code Examples

```python
def hello_world():
    print("Hello, World!")
```

## Images

![Local image](/images/my-photo.jpg)
![External image](https://example.com/image.jpg)

## Links and Downloads

Check out [my website](https://example.com) or [download my resume](/documents/resume.pdf).
```

### 4. Add Syntax Highlighting (Optional)

For beautiful code blocks:

1. Download a custom Prism bundle from [prismjs.com](https://prismjs.com/download.html)
2. Select your theme and languages
3. Place `prism.css` in `/assets/`
4. Place `prism.js` in `/assets/js/`

### 5. Build Your Site

```bash
python3 build.py
```

### 6. Deploy

Upload the entire `output/` folder to your web server. That's it!

## 📁 Directory Structure

```
your-blog/
├── posts/              # Your markdown posts go here
├── images/             # Local images
├── assets/             # CSS and JavaScript
│   ├── style.css       # Main stylesheet (included)
│   ├── prism.css       # Syntax highlighting (optional)
│   └── js/
│       └── prism.js    # Syntax highlighting (optional)
├── output/             # Generated site (upload this!)
├── config.json         # Site configuration
├── build.py            # Build script
├── parser.py           # Markdown parser
├── templates.py        # HTML templates
└── rss_generator.py    # RSS feed generator
```

## 📝 Post Format

### Complete Post Template

Copy this template for new posts:

```markdown
---
# Required fields
title: Your Post Title
date: 2025-01-20

# Optional fields
description: A compelling description for SEO and social sharing
keywords: comma, separated, keywords, for, SEO
author: Your Name (overrides default from config.json)
image: /images/hero-image.jpg (or https://external.com/image.jpg)
categories: Technology, Programming (comma-separated list)
toc: true (enables table of contents for this post)
---

Your post content starts here...

# This is an H1 (usually just one per post)

## This is an H2 (main sections)

### This is an H3 (subsections)

**Bold text** and *italic text* and ***bold italic***

[Link text](https://example.com)

![Image alt text](/images/local-image.jpg)

> This is a blockquote
> It can span multiple lines

- Unordered list item 1
- Unordered list item 2
  - Nested item

`Inline code` looks like this

```javascript
// Code block with syntax highlighting
function greet(name) {
    console.log(`Hello, ${name}!`);
}
```
```

### Frontmatter Fields Explained

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| `title` | ✅ | Post title | `title: My Amazing Post` |
| `date` | ✅ | Publication date | `date: 2025-01-20` |
| `description` | ❌ | SEO meta description | `description: Learn how to...` |
| `keywords` | ❌ | SEO keywords | `keywords: python, web, tutorial` |
| `author` | ❌ | Override default author | `author: Jane Doe` |
| `image` | ❌ | Social media preview | `image: /images/preview.jpg` |
| `categories` | ❌ | Post categories | `categories: Tech, Tutorial` |
| `toc` | ❌ | Enable table of contents | `toc: true` |

## 🎨 Features in Detail

### Table of Contents

When `toc: true` is set, a table of contents is auto-generated from your headings:
- Appears in a styled card after the post metadata
- Shows hierarchy with nested lists
- Only appears if you have 3+ headings (excluding H1)
- Smooth scroll to sections (instant, not slow)
- Ignores headings inside code blocks

### Categories

Organize your content with categories:
- Add `categories: Tech, Tutorial, Python` to frontmatter
- Categories appear on index page and individual posts
- Each category gets its own page at `/categories/category-name.html`
- Category pages list all posts in that category
- Multiple categories per post supported
- Categories are case-sensitive but URLs are lowercase

### Image Handling

- **Local images**: Store in `/images/`, reference as `/images/filename.jpg`
- **External images**: Use full URLs `https://example.com/image.jpg`
- All images get:
  - Responsive sizing (max-width: 100%)
  - 8px border radius
  - Subtle shadow
  - Lazy loading for performance

### Syntax Highlighting

Supports 150+ languages. Always specify the language for highlighting:

````markdown
```python
# This will be highlighted
def example():
    return "Hello"
```

```
# This won't be highlighted (no language specified)
def example():
    return "Hello"
```
````

Common languages: `python`, `javascript`, `css`, `html`, `bash`, `json`, `markdown`, `yaml`

### Smart Link Detection

- Regular links: `[text](url)`
- Download links: Automatically detected by file extension
  - Adds download attribute
  - Shows ⬇ indicator
  - Supported: `.pdf`, `.zip`, `.doc`, `.docx`, `.xls`, `.xlsx`, etc.

### Theme Support

Choose between light and dark themes by setting `"theme"` in config.json:
- `"theme": "light"` - Clean, bright theme (default)
- `"theme": "dark"` - Beautiful dark theme with carefully chosen colors

The theme is set at build time, ensuring optimal performance with no JavaScript theme switching overhead.

## 🚀 Deployment Options

### FTP/SFTP
```bash
# Build locally
python3 build.py

# Upload contents of output/ to your server's public directory
```

### GitHub Pages
1. Build locally: `python3 build.py`
2. Commit the `output/` folder
3. Settings → Pages → Source: Deploy from branch
4. Select folder: `/output`

### Netlify/Vercel
- Build command: `python3 build.py`
- Publish directory: `output`

### Local Preview
```bash
# Build the site
python3 build.py

# Serve locally
cd output && python3 -m http.server 8000

# Visit http://localhost:8000
```

## 💡 Pro Tips

### Performance
- The generator handles hundreds of posts efficiently
- Images are lazy-loaded automatically
- No JavaScript = instant page loads
- System fonts = no font downloads

### Organization
- **Naming**: Use dates in filenames: `2025-01-20-my-post.md`
- **Drafts**: Prefix with underscore: `_draft-post.md` (ignored by build)
- **Order**: Posts are sorted by date (newest first)

### Writing Tips
- One H1 per post (usually the title)
- Use H2 for main sections
- Use H3 for subsections
- Keep paragraphs short for web reading
- Use lists for scannable content

## 🔧 Troubleshooting

### "posts directory not found"
Create a `posts/` folder in the project root

### Images not showing
- Ensure images are in the `images/` folder
- Use absolute paths: `/images/filename.jpg`
- Check file extensions (case-sensitive on some servers)

### Syntax highlighting not working
- Did you download Prism.js and Prism.css?
- Did you specify the language? ` ```python ` not just ` ``` `
- Check that files are in correct locations

### Build errors
- Python 3.6+ required: `python3 --version`
- Check frontmatter has proper YAML syntax
- Ensure dates are formatted: `YYYY-MM-DD`

### TOC not appearing
- Set `toc: true` in frontmatter
- Need at least 3 headings (H2-H6)
- H1 is excluded (assumed to be post title)

## 🛠️ Advanced Customization

### Styling
Edit `assets/style.css`:
- Colors: Change CSS variables in `:root`
- Fonts: Already using system fonts
- Layout: Adjust `--max-width` variable
- TOC: Customize `.toc-card` styles

### Templates
Edit `templates.py` to modify:
- Post layout
- Index page design
- HTML structure

### Build Process
Edit `build.py` to:
- Add custom processing
- Change output structure
- Add new features

## 📝 Markdown Support

The parser supports all common markdown features:

- **Headers**: H1-H6 with `#` syntax
- **Bold/Italic**: `**bold**`, `*italic*`, `***both***`
- **Strikethrough**: `~~strikethrough~~`
- **Links**: `[text](url)` with automatic download detection
- **Images**: `![alt](url)` with lazy loading
- **Code**: Inline `` `code` `` and fenced blocks with syntax highlighting
- **Lists**: Unordered (`-`), ordered (`1.`), nested (2-space indent)
- **Task Lists**: `- [ ]` unchecked, `- [x]` checked
- **Blockquotes**: `>` with nesting support
- **Tables**: Full table support with headers
- **Horizontal Rules**: `---` or `***`

## 📦 What's Included

- ✅ Complete static site generator
- ✅ Responsive CSS framework
- ✅ SEO optimization
- ✅ RSS feed generation
- ✅ Table of contents generator
- ✅ Smart markdown parser
- ✅ Image handling
- ✅ Download detection

## 🤝 Contributing

This is open source! Feel free to:
- Report issues
- Suggest features
- Submit pull requests
- Fork and customize

## 📄 License

This project is open source. Use it however you like!

---

Made with ❤️ for people who love to write