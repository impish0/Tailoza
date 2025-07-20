# Tailoza Static Blog

I spent a weekend building this because I wanted a actually simple blog with a markdown backend.

The cognitive load required to lob my un-filtered thoughts onto the internet seemed unnecessary...

Of course, you could pay a subscription to a hosting provider, but I don't want to.

<p align="center">
  <img src="tailoza-blog-home.png" alt="Tailoza Blog Home" width="100%">
</p>

## Here's the Deal

I built Tailoza because I wanted to write, not wrestle with config files.

**Tailoza Lets You:**
- Write in Markdown (eg. [Obsidian](https://obsidian.md/))

- Run one command

- Get a beautiful site

- Deploy anywhere

That's it. No React. No databases. No subscriptions!

## The 2-Minute Setup (I'm Not Kidding)

```bash

git clone https://github.com/impish0/Tailoza.git

cd Tailoza

```

Now write your first post:

```bash

echo "---

title: My First Post
date: 2025-01-20

---

Hello world. I'm blogging!" > posts/my-first-post.md

```

Build it:

```bash

python3 build.py

```

Done. Your blog is in the `output/` folder.

Upload that folder literally anywhere that serves HTML. GitHub Pages, Netlify, your old shared hosting from 2003 - doesn't matter.

(if you don't know how to do that, i'll make some tutorials soon)

## What You're Getting

<p align="center">
  <img src="tailoza-blog-page.png" alt="Tailoza Blog Features" width="100%">
</p>

**The Good Stuff:**

- Beautiful shadcn-inspired design (light & dark mode)

- Categories For Posts

- Auto-generated table of contents

- Decent SEO 

- RSS feed

- Syntax highlighting


## How to Use This Thing

### Writing Posts

Drop your markdown files in `posts/`:

```markdown

---

title: Why Your Business Needs This

date: 2025-01-20

description: The truth about static sites

categories: Business, Tech

---

Your content here. Write like a human.

```


### Make It Yours

Edit `config.json`:

```json

{

"site_title": "Your Blog Name",

"site_url": "https://yourdomain.com",

"site_description": "What you're about",

"author": "You",

"theme": "dark" // or "light" if you're into that

}

```

### Categories (They Just Work)

Add categories to any post:

```yaml

categories: Marketing, Business, Whatever

```

Boom. Automatic category pages at `/categories/marketing.html`.

### Table of Contents

Got a long post? Add `toc: true` to the frontmatter. It'll generate a nice floating TOC from your headings. Your readers will thank you.

## The Philosophy (Why I Built This)

I've built million-dollar businesses. I've also wasted countless hours on "modern" blogging platforms (all of them)

Here's what I learned:

- **Simple beats complex** - Every. Single. Time.

- **Fast beats features** - Your readers don't care about your framework

- **Writing beats configuring** - Spend time on content, not setup

This tool does one thing: **turns markdown into a beautiful blog**.

No more. No less.

## Deploy This Thing

### GitHub Pages

1. Build: `python3 build.py`
2. Push the `output/` folder
3. Turn on Pages in settings
4. You're live

### Anywhere Else

1. Build: `python3 build.py`
2. Upload the `output/` folder
3. That's it

I'm not kidding. It's just HTML files.

## Want to Contribute?

Cool. I built this in a weekend, so there's probably room for improvement.

- Find a bug? Open an issue
- Want a feature? PR it
- Think something sucks? Tell me why

Just keep it simple. That's the whole point.

## One More Thing

Stop overthinking your blog setup.

Write some things that matter to you, and send it somewhere.

Tailoza gets out of your way so you can focus on what matters: **your content**.

Now stop reading this README and go write something.

---

Built with 🔥 by [Dustin Hogate](https://dustinhogate.com)

P.S. - If this saves you time, use that time to hug your kids, walk your dog, or kiss your SO.

P.P.S. - If you are mad about yet another blog repo - consider this: I built it for me, not you. But you are free to use it, copy it or ignore it.