---
title: CSS For This Site
date: 2025-07-16
keywords: Calude, Email Marketing, Email Copy
author: Dustin Hogate
description: An introduction system prompts I use for email marketing content.
---

## Intro To Email Copy

I spent the last 3 years building high converting email content for D2C Ecommerce.

This is the Claude system prompt I use to aid in email writing copy.

```
:root {
    --bg-color: #ffffff;
    --text-color: #333333;
    --link-color: #0066cc;
    --border-color: #e0e0e0;
    --code-bg: #f5f5f5;
    --max-width: 700px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--bg-color);
    padding: 20px;
}

header, main, footer {
    max-width: var(--max-width);
    margin: 0 auto;
}

header {
    margin-bottom: 40px;
    padding-bottom: 20px;
    border-bottom: 1px solid var(--border-color);
}

header h1 {
    font-size: 2em;
    font-weight: 600;
    margin-bottom: 10px;
}

header nav a {
    color: var(--link-color);
    text-decoration: none;
    margin-right: 20px;
}

header nav a:hover {
    text-decoration: underline;
}

article h1 {
    font-size: 2em;
    font-weight: 600;
    margin-bottom: 10px;
}

article h2 {
    font-size: 1.5em;
    font-weight: 600;
    margin: 30px 0 15px;
}

article h3 {
    font-size: 1.2em;
    font-weight: 600;
    margin: 25px 0 10px;
}

article .post-meta {
    color: #666;
    font-size: 0.9em;
    margin-bottom: 20px;
}

article .post-meta time {
    display: inline;
}

article .post-meta .author {
    font-style: italic;
}

article p {
    margin-bottom: 15px;
}

article a {
    color: var(--link-color);
    text-decoration: none;
}

article a:hover {
    text-decoration: underline;
}

article ul, article ol {
    margin-bottom: 15px;
    padding-left: 30px;
}

article li {
    margin-bottom: 5px;
}

article code {
    background-color: var(--code-bg);
    padding: 2px 5px;
    border-radius: 3px;
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    font-size: 0.9em;
}

article pre {
    background-color: var(--code-bg);
    padding: 15px;
    border-radius: 5px;
    overflow-x: auto;
    margin-bottom: 15px;
    white-space: pre-wrap;
    word-wrap: break-word;
    position: relative;
}

article pre code {
    background-color: transparent;
    padding: 0;
    white-space: pre-wrap;
    word-wrap: break-word;
}

article blockquote {
    border-left: 4px solid var(--border-color);
    padding-left: 20px;
    margin: 20px 0;
    font-style: italic;
    color: #666;
}

article img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    margin: 20px 0;
    display: block;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.post-preview {
    margin-bottom: 30px;
    padding-bottom: 30px;
    border-bottom: 1px solid var(--border-color);
}

.post-preview:last-child {
    border-bottom: none;
}

.post-preview h2 {
    font-size: 1.5em;
    margin-bottom: 5px;
}

.post-preview h2 a {
    color: var(--text-color);
    text-decoration: none;
}

.post-preview h2 a:hover {
    color: var(--link-color);
}

.post-preview time {
    color: #666;
    font-size: 0.9em;
}

.post-preview p {
    margin-top: 10px;
}

footer {
    margin-top: 60px;
    padding-top: 20px;
    border-top: 1px solid var(--border-color);
    text-align: center;
    color: #666;
    font-size: 0.9em;
}

footer a {
    color: var(--link-color);
    text-decoration: none;
}

footer a:hover {
    text-decoration: underline;
}

@media (max-width: 600px) {
    body {
        padding: 10px;
    }
    
    article h1 {
        font-size: 1.5em;
    }
    
    article h2 {
        font-size: 1.3em;
    }
}
```