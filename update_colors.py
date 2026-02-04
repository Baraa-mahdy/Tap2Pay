#!/usr/bin/env python3
import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace old CSS variable names with new simplified ones
replacements = [
    # Old color variables to new primary color
    (r'--color-primary\b', '--primary-color'),
    (r'--color-secondary', '--primary-color'),
    (r'--color-accent(?!-rgb)', '--primary-color'),
    (r'--color-primary-rgb', '--primary-rgb'),
    (r'--color-accent-rgb', '--primary-rgb'),
    
    # Glow variables
    (r'--glow-accent', '--glow'),
    (r'--glow-primary(?!-[a-z])', '--glow'),
    (r'--glow-primary-lg', '--glow-lg'),
    (r'--glow-primary-sm', '--glow-sm'),
    
    # Shadow variables
    (r'--shadow-primary-pulse', '--shadow-pulse'),
    (r'--shadow-primary-xl', '--shadow-xl'),
    (r'--shadow-primary-lg', '--shadow-lg'),
    (r'--shadow-primary-md', '--shadow-md'),
    (r'--shadow-primary-sm', '--shadow-sm'),
    
    # Remove gradients with primary color - replace with solid var(--primary-color)
    (r'linear-gradient\(135deg, var\(--primary-color\), var\(--primary-color\)[^)]*\)', 'var(--primary-color)'),
    (r'linear-gradient\(135deg, var\(--primary-color\)[^)]*\)', 'var(--primary-color)'),
    
    # Replace hardcoded red colors with var(--primary-color)
    (r'#FF3B3B', 'var(--primary-color)'),
    (r'#ff6b6b', 'var(--primary-color)'),
    (r'#E63131', 'var(--primary-color)'),
    (r'#ff4444', 'var(--primary-color)'),
    (r'#e63131', 'var(--primary-color)'),
    (r'#cc2f2f', 'var(--primary-color)'),
    
    # Replace yellow/accent colors with var(--primary-color)
    (r'#ffd700', 'var(--primary-color)'),
    (r'#ffed4e', 'var(--primary-color)'),
    (r'#e6b800', 'var(--primary-color)'),
    (r'#ff8c00', 'var(--primary-color)'),
    
    # Replace rgba red colors with rgba primary
    (r'rgba\(255, 59, 59,', 'rgba(var(--primary-rgb),'),
]

for old_pattern, new_text in replacements:
    content = re.sub(old_pattern, new_text, content, flags=re.IGNORECASE)

# Write the file back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Color updates completed!")
