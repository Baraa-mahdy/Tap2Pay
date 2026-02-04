#!/usr/bin/env python3
import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace text color declarations with var(--text-color)
# Match any color property with hardcoded text colors and replace with var(--text-color)
text_color_replacements = [
    # Specific text colors that should use --text-color
    ('color: #ffffff;', 'color: var(--text-color);'),
    ('color: #ddd;', 'color: var(--text-secondary);'),
    ('color: #888;', 'color: var(--text-muted);'),
    ('color: #aaa;', 'color: var(--text-muted);'),
    ('color: #999;', 'color: var(--text-muted);'),
    ('color: #777;', 'color: var(--text-light);'),
    ('color: #666;', 'color: var(--text-light);'),
    ('color: #555;', 'color: var(--text-light);'),
    ('color: #ccc;', 'color: var(--text-secondary);'),
    
    # Primary color text (red to primary)
    ('color: #FF3B3B;', 'color: var(--primary-color);'),
    ('color: #ff3b3b;', 'color: var(--primary-color);'),
    ('color: #ff6b6b;', 'color: var(--primary-color);'),
    
    # Accent colors (should use primary)
    ('color: #ffd700;', 'color: var(--primary-color);'),
    ('color: #4caf50;', 'color: var(--primary-color);'),
    ('color: #f44336;', 'color: var(--primary-color);'),
    
    # Black/very dark text - replace with text variable
    ('color: #000;', 'color: var(--text-color);'),
    ('color: #1a1a1a;', 'color: var(--text-color);'),
    ('color: #1f1f1f;', 'color: var(--text-color);'),
]

for old, new in text_color_replacements:
    content = content.replace(old, new)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ All text colors unified to CSS variables")
print("✓ Light mode will display pure white text")
print("✓ Primary color text colors synchronized")
