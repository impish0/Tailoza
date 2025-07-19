#!/usr/bin/env python3
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

def generate_rss(posts, blog_title, blog_url, blog_description):
    """Generate RSS feed from posts"""
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    
    # Channel metadata
    ET.SubElement(channel, "title").text = blog_title
    ET.SubElement(channel, "link").text = blog_url
    ET.SubElement(channel, "description").text = blog_description
    ET.SubElement(channel, "language").text = "en-us"
    ET.SubElement(channel, "lastBuildDate").text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")
    
    # Add posts
    for post in posts[:10]:  # Latest 10 posts
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = post['title']
        ET.SubElement(item, "link").text = f"{blog_url}/posts/{post['filename']}"
        ET.SubElement(item, "description").text = post.get('description', post['title'])
        ET.SubElement(item, "pubDate").text = format_rss_date(post['date'])
        ET.SubElement(item, "guid").text = f"{blog_url}/posts/{post['filename']}"
    
    # Pretty print XML
    rough_string = ET.tostring(rss, encoding='unicode')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def format_rss_date(date_str):
    """Convert YYYY-MM-DD to RSS date format"""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%a, %d %b %Y 00:00:00 +0000")
    except:
        return datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")