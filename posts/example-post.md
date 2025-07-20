---
title: Welcome to Tailoza
date: 2025-01-20
description: Get started with the simplest static blog generator
categories: Tutorial, Getting Started
toc: true
---

# Welcome to Tailoza!

This is an example post showing all the features of Tailoza. Feel free to delete this and start writing your own content!

## Markdown Features

### Text Formatting

You can write in **bold**, *italic*, or ***both***. You can also use ~~strikethrough~~ text.

### Lists

Unordered lists:
- First item
- Second item
  - Nested item
  - Another nested item
- Third item

Ordered lists:
1. First step
2. Second step
3. Third step

Task lists:
- [x] Install Tailoza
- [x] Create first post
- [ ] Deploy to production

### Links and Images

Create [links to websites](https://github.com/impish0/Tailoza) or [download files](/documents/guide.pdf).

Add images from the `/images/` folder or external URLs:
```markdown
![Alt text](/images/example.jpg)
```

### Code Blocks

Inline code: `python3 build.py`

Fenced code blocks with syntax highlighting:

```python
def greet(name):
    """A simple greeting function"""
    return f"Hello, {name}! Welcome to Tailoza!"

print(greet("World"))
```

### Blockquotes

> "The best time to plant a tree was 20 years ago. The second best time is now."
> 
> — Chinese Proverb

### Tables

| Feature | Status | Notes |
|---------|--------|-------|
| Markdown | ✅ | Full CommonMark support |
| Categories | ✅ | Organize your content |
| RSS Feed | ✅ | For your readers |
| SEO | ✅ | Built-in optimization |

## Building Your Blog

1. Write posts in the `posts/` directory
2. Run `python3 build.py`
3. Deploy the `output/` folder

That's it! No complex configuration, no database setup, just write and publish.

---

Happy blogging with Tailoza! 🎨