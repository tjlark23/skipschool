# Skip School Curriculum Packet System

## What This Is

A production system for generating weekly, printable, TEKS-aligned curriculum packets for homeschool families (grades K-5). This is the engine behind Skip School's paid subscription product.

## How It Works

1. **Content generation:** Claude uses the skill (in `skill/SKILL.md`) and reference files to generate structured JSON content for a specific grade and week.
2. **HTML rendering:** The `scripts/generate_packet.py` script reads the JSON and produces a styled HTML file using the template in `templates/worksheet-template.html`.
3. **Delivery:** The HTML is either printed directly by parents or converted to PDF.

## Directory Structure

```
curriculum/
  skill/
    SKILL.md                           # The Claude skill (generation rules, voice, design system)
    references/
      teks-scope-sequence.md           # K-5 weekly pacing, 36 weeks per grade
      page-templates.md                # Structural templates per page type
      focus-area-banks.md              # Problem banks for Tier 2 supplements
  templates/
    worksheet-template.html            # v4 HTML/CSS template
  scripts/
    generate_packet.py                 # JSON-to-HTML renderer
  output/                              # Generated packets go here
  README.md                            # This file
```

## Usage

```bash
# Generate a packet from a content JSON file
python curriculum/scripts/generate_packet.py \
  curriculum/output/grade3-week1.json \
  curriculum/output/grade3-week1.html \
  --logo images/img-01-logo.png \
  --footer-logo images/img-01-logo.png
```

## Design System (v4)

- Two-bar header: white logo bar + colored subject banner
- Five subject colors: Navy (computation), Green (reading), Coral (grammar), Teal (geometry), Purple (fractions)
- Gold extension page (premium tier)
- "Try This at Home" box on every worksheet page
- Fixed 11in pages for clean printing
- Fonts: Fraunces (titles), DM Sans (body)

## Subscription Tiers

- **Tier 1 ($19/mo):** Weekly grade-level packet (Math + ELA)
- **Tier 2 ($29/mo):** Tier 1 + focus track supplements
- **Tier 3 ($49/mo):** Tier 2 + personalized with child's name, calibrated difficulty, monthly boost packet
