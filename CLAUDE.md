# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Core Commands

**Build the site:**
```bash
python3 build.py
```
This processes all markdown files in `posts/`, generates HTML pages, RSS feeds, sitemaps, and copies assets to the `output/` directory.

**Development server with auto-rebuild:**
```bash
python3 serve.py
```
Runs a local server at http://localhost:8000 with automatic rebuilding when files change. Watches `posts/`, `assets/`, `images/`, and core Python files.

## Architecture Overview

Tailoza is a static blog generator with a modular Python architecture:

### Core Components

- **`build.py`** - Main build orchestrator that processes markdown posts, generates HTML, handles pagination, and copies assets
- **`parser.py`** - Markdown parsing, frontmatter extraction, HTML conversion, TOC generation, and heading ID management
- **`templates.py`** - HTML template generation for posts, index pages, and category pages
- **`rss_generator.py`** - RSS feed generation with proper timezone handling
- **`sitemap_generator.py`** - XML sitemap generation for SEO
- **`serve.py`** - Development server with file watching and auto-rebuild functionality

### Data Flow

1. **Input**: Markdown files in `posts/` with YAML frontmatter
2. **Processing**: `build.py` orchestrates parsing via `parser.py`, applies templates from `templates.py`
3. **Output**: Static HTML files in `output/` with proper URL structure based on `post_url_prefix`

### Key Architecture Patterns

- **Pipeline-Based Processing**: Sequential build pipeline with clear data flow from markdown to static HTML
- **No External Dependencies**: Uses only Python standard library for maximum portability
- **Clean Builds**: Output directory is completely recreated on each build ensuring consistency
- **Modular Processing**: Each component has a single responsibility (parsing, templating, RSS, etc.)
- **Compiled Patterns**: `parser.py` pre-compiles regex patterns for performance optimization
- **Security-First Design**: All HTML generation properly escapes content, no database = no injection risks
- **Zero-Config Defaults**: Sensible defaults with minimal required configuration

### Key Features

- **Pagination**: Configurable posts per page for index and category pages
- **Categories**: Auto-generated category pages from post frontmatter
- **Search**: Client-side search with JSON index generation
- **Draft Posts**: Files starting with `_` are ignored during build
- **URL Structure**: Configurable via `post_url_prefix` in config.json
- **Reading Time**: Auto-calculated based on word count (200 WPM)
- **TOC**: Auto-generated table of contents for posts with `toc: true`

### Configuration

Primary config in `config.json` with these key settings:
- `site_title`, `site_url`, `site_description` - Required site metadata (validated on build)
- `post_url_prefix` - Controls URL structure (e.g., "/posts", "/blog", or "")
- `posts_per_page` - Pagination setting
- `theme` - "dark" or "light" mode
- `timezone` - For RSS feed timestamps (format: "+/-HHMM")
- `footer_text` - Footer content with **HTML link support**

#### Adding Links in Configuration

The `footer_text` field supports HTML links while keeping other content secure:

```json
{
  "footer_text": "© 2025 | Built with ❤️ by <a href=\"https://yoursite.com\">Your Name</a>"
}
```

**Security Features:**
- Only `<a href="...">...</a>` tags are allowed  
- All other HTML is automatically escaped for security
- URLs and link text are properly sanitized
- Multiple links are supported

**Examples:**
```json
"footer_text": "© 2025 | <a href=\"https://github.com/user\">GitHub</a> | <a href=\"mailto:hello@example.com\">Contact</a>"
```

### Asset Management

- **CSS/JS**: Files in `assets/` are copied to `output/assets/`
- **Images**: Files in `images/` are copied and referenced in posts
- **Favicon**: Auto-detected from `assets/` or root directory

### Post Structure

Posts use YAML frontmatter with markdown content:
```yaml
---
title: Required post title
date: 2024-01-20  # Required YYYY-MM-DD format
description: Optional SEO description
categories: Optional, Comma, Separated
author: Optional author override
image: Optional social preview image
toc: true  # Optional table of contents
keywords: Optional SEO keywords
---

Markdown content here...
```

### Markdown Processing Details

The parser supports:
- Headers (h1-h6) with automatic ID generation
- Code blocks with syntax highlighting (via Prism.js)
- Inline code, bold, italic, strikethrough
- Task lists with checkboxes
- Images (local and external)
- Links with proper escaping
- Horizontal rules
- Nested lists (ordered and unordered)

### Development Server Features

`serve.py` implements:
- File watching with 1-second polling interval
- Automatic rebuilds on changes to posts, assets, images, or core Python files
- Quiet HTTP handler to reduce console noise
- Runs on port 8000 by default

## Development Notes

### Build Process
- All builds are clean builds (output directory is recreated)
- Sequential pipeline: Config → Parse → Template → Generate → Assets
- Error handling includes validation for required config fields and file operations
- The build process generates search index JSON for client-side search functionality

### Performance Features
- Pre-compiled regex patterns in parser for fast markdown processing
- Efficient file watching with 1-second polling in development server
- Minimal HTTP request logging during development
- Static output with no server-side processing required

### SEO and Content
- RSS feeds include only the latest 10 posts
- Sitemaps include homepage and all published posts with proper SEO metadata
- Structured data (JSON-LD) automatically added to posts
- Open Graph and Twitter Card meta tags for social sharing

### Testing
- **No automated tests currently exist** - validation occurs through:
  - Configuration validation on build
  - Development server provides immediate feedback
  - Clean builds ensure consistency and prevent stale files