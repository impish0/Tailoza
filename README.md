# Simple Static Blog Generator

A minimal, zero-dependency static site generator that converts Markdown to HTML with RSS feed support.

## Features

- **Markdown Support**: Write posts in Markdown with YAML frontmatter
- **Images**: Local (`/images/`) and external images with automatic styling
- **Syntax Highlighting**: Beautiful code blocks with Prism.js (optional)
- **SEO Optimized**: Meta tags, Open Graph, and Twitter Cards
- **RSS Feed**: Automatically generated
- **Fast & Simple**: No JavaScript required (except optional features)
- **Self-Contained**: No external dependencies or CDN requirements

## Quick Start

1. **Setup**
   ```bash
   # Clone or download this project
   # Python 3.6+ required (for building only)
   ```

2. **Configure** - Edit `config.json`:
   ```json
   {
       "site_title": "My Blog",
       "site_url": "https://yourdomain.com",
       "site_description": "Your blog description",
       "author": "Your Name",
       "footer_text": "© 2025 Your Name"
   }
   ```

3. **Write Posts** - Create `.md` files in `posts/`:
   ```markdown
   ---
   title: My First Post
   date: 2025-01-19
   description: A brief description
   keywords: blog, static, markdown
   author: John Doe
   image: https://example.com/preview.jpg
   ---

   Your content here...

   ![Local image](/images/photo.jpg)
   [Download PDF](/documents/guide.pdf)
   ```

4. **Add Syntax Highlighting** (Optional):
   - Download Prism.js and Prism.css from https://prismjs.com
   - Place `prism.css` in `/assets/`
   - Place `prism.js` in `/assets/js/`

5. **Build**:
   ```bash
   python3 build.py
   ```

6. **Deploy**: Upload the entire `output/` folder to your web server

## Directory Structure

```
blog/
├── posts/          # Your markdown posts
├── images/         # Local images
├── assets/         # CSS and Prism files
│   ├── style.css
│   ├── prism.css   # (optional)
│   └── js/
│       └── prism.js # (optional)
├── output/         # Generated site (upload this)
├── config.json     # Site configuration
└── build.py        # Build script
```

## Post Format

### Required Fields
- `title`: Post title
- `date`: Publication date (YYYY-MM-DD)

### Optional Fields
- `description`: Brief description for SEO
- `keywords`: Comma-separated keywords
- `author`: Override default author
- `image`: Preview image URL for social media

### Markdown Features

```markdown
# Headers
**Bold** and *italic* text
[Links](https://example.com)
![Images](/images/photo.jpg)

- Lists
- Work
- Great

`inline code` and:

```python
# Code blocks with syntax highlighting
def hello():
    print("Hello, World!")
```
```

## Deployment

### FTP/SFTP
Upload the contents of `output/` to your web server's public directory

### GitHub Pages
1. Build locally with `python3 build.py`
2. Commit the `output/` folder
3. Set GitHub Pages to serve from the `output/` directory

### Netlify/Vercel
1. Build command: `python3 build.py`
2. Publish directory: `output`

## Tips

- **Performance**: The generator handles hundreds of posts efficiently
- **Images**: Store in `/images/` for local hosting
- **URLs**: Use absolute paths (`/images/file.jpg`) for images and downloads
- **Drafts**: Prefix filenames with `_` to exclude from build
- **Order**: Posts are sorted by date (newest first)

## Troubleshooting

**"posts directory not found"**
- Create a `posts/` folder in the project root

**Images not showing**
- Ensure images are in the `images/` folder
- Use format: `/images/filename.jpg` in markdown

**Syntax highlighting not working**
- Download and place Prism files as described above
- Use language hints: ` ```python ` for Python code

**Build errors**
- Check that Python 3.6+ is installed
- Ensure all `.md` files have valid frontmatter

## License

This project is open source. Feel free to use and modify as needed.