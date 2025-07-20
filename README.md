# 🎨 Tailoza

A beautifully simple static blog generator that makes publishing uncomplicated. Built over a weekend to prove that blogging doesn't need to be complex.

<p align="center">
  <strong>Write in Markdown → Build → Deploy → Done</strong>
</p>

## ✨ Why Tailoza?

I'm Dustin Hogate, and I built Tailoza because I wanted a blog that was:
- **Dead simple** to use - no databases, no complex configs
- **Beautiful** out of the box - with a modern shadcn-inspired theme
- **Lightning fast** - pure static HTML with zero JavaScript bloat
- **SEO ready** - because your content deserves to be found

This is a passion project born from frustration with overly complex blogging platforms. Sometimes you just want to write and publish without the hassle.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/impish0/Tailoza.git
cd Tailoza

# Create your first post
echo "---
title: Hello World
date: 2025-01-20
---

Welcome to my blog!" > posts/hello-world.md

# Build your site
python3 build.py

# Preview locally
cd output && python3 -m http.server 8000
```

That's it! Your blog is ready at `http://localhost:8000`

## 📝 Features

### For Writers
- **Markdown**: Write naturally with full CommonMark support
- **Frontmatter**: Simple YAML metadata for posts
- **Categories**: Organize your content effortlessly
- **Table of Contents**: Auto-generated from your headings
- **Code Highlighting**: Beautiful syntax highlighting with Prism.js
- **Draft Mode**: Prefix files with `_` to keep them private

### For Developers
- **Zero Dependencies**: Just Python 3.6+ standard library
- **shadcn Theme**: Modern violet theme with light/dark modes
- **100% Static**: No JavaScript required (except optional features)
- **SEO Optimized**: Meta tags, Open Graph, sitemap, RSS feed
- **Responsive**: Mobile-first design that works everywhere
- **Fast Builds**: Handles hundreds of posts efficiently

### For Readers
- **Lightning Fast**: No database queries, no render delays
- **Accessible**: Semantic HTML, proper contrast, keyboard navigation
- **RSS Support**: Follow your favorite blogs the classic way
- **Clean Design**: Focus on content, not chrome

## 🎯 Usage

### Writing Posts

Create markdown files in the `posts/` directory:

```markdown
---
title: My Awesome Post
date: 2025-01-20
description: A brief description for SEO
categories: Technology, Programming
toc: true
---

# Your content starts here

Write in **Markdown** with all the features you love!
```

### Configuration

Edit `config.json` to customize your blog:

```json
{
    "site_title": "My Blog",
    "site_url": "https://yourdomain.com",
    "site_description": "A blog about things I love",
    "author": "Your Name",
    "footer_text": "© 2025 Your Name",
    "theme": "light"  // or "dark"
}
```

### Building

```bash
python3 build.py
```

This generates your entire site in the `output/` directory. Upload it anywhere that serves static files!

## 🎨 Theming

Tailoza uses a beautiful shadcn-inspired violet theme with both light and dark modes. The theme uses modern oklch colors for perfect perceptual uniformity.

### Light Mode
Clean and professional with subtle purple accents.

### Dark Mode
Easy on the eyes with excellent contrast.

Switch themes by changing `"theme"` in config.json and rebuilding.

## 📁 Project Structure

```
tailoza/
├── posts/          # Your markdown posts
├── images/         # Post images
├── assets/         # CSS and JS
├── output/         # Generated site (git ignored)
├── config.json     # Site configuration
├── build.py        # Build script
└── README.md       # You are here!
```

## 🛠️ Advanced Features

### Categories
Organize posts with categories:
```yaml
categories: Web Development, Tutorial, Python
```

Each category gets its own archive page at `/categories/category-name.html`

### Table of Contents
Add `toc: true` to any post with 3+ headings to auto-generate a table of contents.

### Syntax Highlighting
Specify the language for beautiful code blocks:
````markdown
```python
def hello():
    print("Hello, Tailoza!")
```
````

### Smart Links
- Regular links: `[text](url)`
- Download links: Automatically detected with ⬇ indicator
- Email links: `[Email me](mailto:you@example.com)`

## 🚢 Deployment

### GitHub Pages
1. Build locally: `python3 build.py`
2. Push the `output/` folder
3. Enable Pages in repository settings

### Netlify/Vercel
- Build command: `python3 build.py`
- Publish directory: `output`

### Traditional Hosting
Just upload the `output/` folder to any web server!

## 🤝 Contributing

Contributions are welcome! Whether it's:
- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🎨 Theme variations

Feel free to open an issue or submit a pull request.

## 💡 Philosophy

Tailoza believes in:
- **Simplicity over features** - Do one thing well
- **Content over chrome** - Your words matter most
- **Speed over everything** - Respect your readers' time
- **Beauty by default** - Good design shouldn't be optional

## 📜 License

MIT License - Use it however you want!

## 🙏 Acknowledgments

- Inspired by the simplicity of early web
- Theme inspired by [shadcn/ui](https://ui.shadcn.com/)
- Built with love over a weekend

---

<p align="center">
  Made with ❤️ by <a href="https://dustinhogate.com">Dustin Hogate</a>
</p>

<p align="center">
  <strong>Stop configuring. Start writing.</strong>
</p>