#!/usr/bin/env python3
import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replacement pairs - order matters!
replacements = [
    # Replace old CSS variables with new ones
    ('--color-primary-light', '--primary-color'),  # Must be before --color-primary
    ('--color-primary-dark', '--primary-color'),   # Must be before --color-primary
    ('--color-primary-rgb', '--primary-rgb'),      # RGB variant
    ('--color-primary', '--primary-color'),        # Main primary
    ('--color-secondary', '--primary-color'),      # All secondary colors become primary
    ('--color-accent-rgb', '--primary-rgb'),       # Accent RGB becomes primary RGB
    ('--color-accent', '--primary-color'),         # All accent colors become primary
    
    # Replace glow variables
    ('--glow-primary-sm', '--glow-sm'),
    ('--glow-primary-lg', '--glow-lg'),
    ('--glow-accent', '--glow'),
    ('--glow-primary', '--glow'),
    
    # Replace shadow variables
    ('--shadow-primary-pulse', '--shadow-pulse'),
    ('--shadow-primary-xl', '--shadow-xl'),
    ('--shadow-primary-lg', '--shadow-lg'),
    ('--shadow-primary-md', '--shadow-md'),
    ('--shadow-primary-sm', '--shadow-sm'),
]

# Apply replacements
for old_var, new_var in replacements:
    content = content.replace(old_var, new_var)

# Replace hardcoded colors with var(--primary-color) - be careful with order
hardcoded_colors = [
    ('#FF3B3B', 'var(--primary-color)'),
    ('#ff3b3b', 'var(--primary-color)'),
    ('#ff6b6b', 'var(--primary-color)'),
    ('#E63131', 'var(--primary-color)'),
    ('#e63131', 'var(--primary-color)'),
    ('#ff4444', 'var(--primary-color)'),
    ('#cc2f2f', 'var(--primary-color)'),
    ('#4caf50', 'var(--primary-color)'),  # Green accent becomes primary
    ('#ffd700', 'var(--primary-color)'),  # Yellow accent becomes primary
    ('#ffed4e', 'var(--primary-color)'),
    ('#e6b800', 'var(--primary-color)'),
    ('#ff8c00', 'var(--primary-color)'),
]

for color_hex, new_var in hardcoded_colors:
    content = content.replace(color_hex, new_var)

# Replace gradients with primary color - simple case
content = re.sub(
    r'linear-gradient\s*\(\s*135deg\s*,\s*var\(--primary-color\)\s*,\s*var\(--primary-color\)[^)]*\)',
    'var(--primary-color)',
    content,
    flags=re.IGNORECASE
)

# Replace rgba(255, 59, 59, with rgba(var(--primary-rgb),
content = content.replace('rgba(255, 59, 59,', 'rgba(var(--primary-rgb),')

# Replace rgba(255, 215, 0, (accent gold) with rgba(var(--primary-rgb),
content = content.replace('rgba(255, 215, 0,', 'rgba(var(--primary-rgb),')

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ All CSS variable names updated to single primary color system")
print("✓ All hardcoded colors replaced with var(--primary-color)")
print("✓ All gradients with primary color replaced with solid var(--primary-color)")
